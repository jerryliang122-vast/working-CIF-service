import logging
from decimal import Decimal, ROUND_UP
import re
from utils.warehouse.round import price_to_ten
logger = logging.getLogger("my_logger")


class calculate_cfs_wg():
    def __init__(self, cfs_wg_data,cfs_stander):
        """
        需要写入列表[[[10, True, 'HWMAA2400934N-MF'], [[[False, '20', '200.000', '0.661', '36.0×34.0×27.0']]]], [[16, True, 'HWMAA2400934N-MF'], [[[False, '24', '175.000', '0.800', '35.0×34.0×28.0']]]]]
        """
        self.cfs_wg_data = cfs_wg_data
        self.cfs_stander = cfs_stander 

    def warehouse_time(self,data):
        self.cfs_price = self.cfs_stander
        #判断时间在18年之后早上8点之前
        if data[0] >=18 or data[0] <= 8: 
            return True
        else:
            return False
    #判断是否超大
    def warehous_ows(self,data):
        #获取货物数据，检查是否有超大的
        pattern = re.compile(r'(\d+(\.\d+)?)([xX*\.](\d+(\.\d+)?))+')
        match = pattern.match(data[4])
        dimensions = [float(num) for num in re.findall(r'\d+(\.\d+)?', match)]
        if any(dim > 300 for dim in dimensions) or data[3] >=3.00:
            return True
        return False
    #上下车费
    def warehouse_in(self,data,discount):
        """
        计算仓库入仓费用。
        
        :param data: 包含货物相关信息的字典，包括是否为大件、是否为夜间、托盘数量、重量和体积。
        :param discount: 折扣率，用于计算最终费用。
        :return: 返回计算出的最大费用，保留到10的最小整数。
        """
        # 根据货物是否为大件，确定包装、重量和体积的单价
        if data['big'] == True:
            #获取货物数据，按照超大修改OWS单价
            pkgs_unit_price  = Decimal(self.cfs_stander['cfs_yg_pkgs_charge']) +Decimal(10)
            weight_unit_price = Decimal(self.cfs_stander['cfs_yg_weight_charge']) +Decimal(10)
            volume_unit_price = Decimal(self.cfs_stander['cfs_yg_cmb_charge']) +Decimal(10)
        else:
            pkgs_unit_price =Decimal(self.cfs_stander['cfs_yg_pkgs_charge'])
            weight_unit_price = Decimal(self.cfs_stander['cfs_yg_weight_charge'])
            volume_unit_price = Decimal(self.cfs_stander['cfs_yg_cmb_charge'])
        
        # 如果是夜间入仓，费用增加30%
        if data['night'] == True: #判断是否夜间
            pkgs_unit_price = Decimal(pkgs_unit_price) * Decimal(1.30) #增加30%
            weight_unit_price = Decimal(weight_unit_price) * Decimal(1.30) #增加30% 
            volume_unit_price = Decimal(volume_unit_price) * Decimal(1.30) #增加30%  
        
        # 计算包装费，如果无托盘，则包装费为0
        #计算上下车费，按照货物数据，计算出PKGS WEIGHT 和VOLUME 然后相加，返回结果。
        if data['pallet'] == True:
            pkgs_charge = Decimal(pkgs_unit_price)*Decimal(data['pkgs'])
        else:
            pkgs_charge = Decimal(0)
        
        # 计算重量费和体积费
        weight_charge = Decimal(weight_unit_price)*Decimal(data['weight'])
        volume_charge = Decimal(volume_unit_price) * Decimal(data['volume'])
        
        # 应用折扣
        #打折费率
        pkgs_charge = Decimal(pkgs_charge) * Decimal(discount)
        weight_charge = Decimal(weight_charge) * Decimal(discount)
        volume_charge = Decimal(volume_charge) * Decimal(discount)
        
        # 计算最大费用，考虑到最小费用门槛
        # 比大小,mini
        max_price = Decimal.max(pkgs_charge,weight_charge)
        max_price = Decimal.max(max_price,volume_charge)   
        max_price = Decimal.max(max_price,Decimal(self.cfs_stander['cfs_yg_mini_charge']))
        
        # 返回最大费用，保留到10的最小整数
        #进十位
        return price_to_ten(max_price)

    # 合并货物数据
    # 该方法用于计算给定数据集中所有货物的总件数、总重量和总体积。
    # 参数:
    #   data - 一个包含货物信息的列表，每个元素都是一个列表，包含四个项目：
    #          0: 货物ID，1: 货物件数，2: 货物重量，3: 货物体积。
    # 返回:
    #   一个字典，包含货物的总件数（pkgs）、总重量（weight）和总体积（volume）。
    #合并货物数据
    def merge_data(self,data):
        # 初始化货物件数、重量和体积的累加器
        pkgs = Decimal(0)
        weight = Decimal(0)
        volume = Decimal(0)
        # 遍历数据集，累加每个货物的件数、重量和体积
        for i in data:
            pkgs += Decimal(i[1])
            weight += Decimal(i[2])
            volume += Decimal(i[3])
        # 返回包含总件数、总重量和总体积的字典
        return {'pkgs':pkgs,'weight':weight,'volume':volume}
    
    #上下车费,超大，夜间算法
    def warehouse_in_charge(self,data,night):
        """
        计算仓库装卸费用。
        
        根据货物类型（普通、托盘、超大）和是否夜间操作，计算相应的装卸费用。
        参数:
        - data: 货物数据列表，每个元素包含货物的信息。
        - night: 布尔值，指示是否为夜间操作。
        
        返回:
        - price_total: 字典，包含各类货物的装卸费用总和。
        """
        
        # 筛选出超大货物的数据
        # 清洗数据，单独计算超大货的上下车费。
        ows_data = [i for i in data if self.warehous_ows(i)] #超大货物
        
        # 筛选出普通货物的数据
        normal_data = [i for i in data if not self.warehous_ows(i) and not i[0]] #普通货物
        
        # 筛选出托盘货物的数据
        pallet_data = [i for i in data if not self.warehous_ows(i) and i[0]] #托盘货物。

        # 如果有普通货物，计算其装卸费用
        #如果normal_data中有数据则计算，否则不计算。
        if normal_data:
            normal_data_dict = self.merge_data(normal_data)
            #将数据做成字典
            normal_data_dict['big'] = False
            normal_data_dict['pallet'] = False
            normal_data_dict['night'] = night
            normal_price = self.warehouse_in(normal_data_dict) #计算normal_data的上下车费。
        else:
            normal_price = Decimal(0)
        
        # 如果有托盘货物，计算其装卸费用
        #如果pallet_data中有数据则计算，否则不计算。
        if pallet_data:
            pallet_data_dict = self.merge_data(pallet_data)
            #将数据做成字典
            pallet_data_dict['big'] = False
            pallet_data_dict['pallet'] = True
            pallet_data_dict['night'] = night
            pallet_price = self.warehouse_in(pallet_data_dict) #计算pallet_data的上下车费。
        else:
            pallet_price = Decimal(0)
        
        # 如果有超大货物，计算其装卸费用
        #如果ows_data中有数据则计算，否则不计算。
        if ows_data:
            ows_data_dict = self.merge_data(ows_data)
            #将数据做成字典
            ows_data_dict['big'] = True
            ows_data_dict['pallet'] = False
            ows_data_dict['night'] = night
            ows_price = self.warehouse_in(ows_data_dict) #计算ows_data的上下车费。
        else:
            ows_price = Decimal(0)
        
        # 计算所有货物的装卸费用总和
        #将所有结果相加
        price_total = normal_price + pallet_price + ows_price

    def main(self):
        #按车分离数据
        for i in self.cfs_wg_data: 
            #判断入库时间，修改cfs-price 的标准
            night = self.warehouse_time(i[0])