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
            #将CFS_price中的PKGS WEIGHT 和volume增加30%
            self.cfs_price["cfs_yg_pkgs_charge"] = Decimal(Decimal(self.cfs_price["cfs_yg_pkgs_charge"]) * Decimal(1.30)).quantize=ROUND_UP  # PKGS WEIGHT 增加30%
            self.cfs_price["cfs_yg_weight_charge"] = Decimal(Decimal(self.cfs_price["cfs_yg_weight_charge"]) * Decimal(1.30)).quantize=ROUND_UP
        else:
            return False
    #判断是否超大
    def warehous_ows(self,data):
        #获取货物数据，检查是否有超大的
        pattern = re.compile(r'(\d+(\.\d+)?)([xX*\.](\d+(\.\d+)?))+')
        for i in data:
            match = pattern.match(i[4])
            dimensions = [float(num) for num in re.findall(r'\d+(\.\d+)?', match)]
            if any(dim > 300 for dim in dimensions) or i[3] >=3.00:
                return True
        
        return False
    #上下车费
    def warehouse_in(self,data,big,night,pallet):
        if big == True:
            #获取货物数据，按照超大修改OWS单价
            pkgs_unit_price  = Decimal(self.cfs_stander['cfs_yg_pkgs_charge']) +Decimal(10)
            weight_unit_price = Decimal(self.cfs_stander['cfs_yg_weight_charge']) +Decimal(10)
            volume_unit_price = Decimal(self.cfs_stander['cfs_yg_cmb_charge']) +Decimal(10)
        else:
            pkgs_unit_price =Decimal(self.cfs_stander['cfs_yg_pkgs_charge'])
            weight_unit_price = Decimal(self.cfs_stander['cfs_yg_weight_charge'])
            volume_unit_price = Decimal(self.cfs_stander['cfs_yg_cmb_charge'])
        if night == True: #判断是否夜间
            pkgs_unit_price = Decimal(pkgs_unit_price) * Decimal(1.30) #增加30%
            weight_unit_price = Decimal(weight_unit_price) * Decimal(1.30) #增加30% 
            volume_unit_price = Decimal(volume_unit_price) * Decimal(1.30) #增加30%  
        #计算上下车费，按照货物数据，计算出PKGS WEIGHT 和VOLUME 然后相加，返回结果。
        if pallet:
            pkgs_charge = Decimal(pkgs_unit_price)*Decimal(data['pkgs'])
        else:
            pkgs_charge = Decimal(0)
        weight_charge = Decimal(weight_unit_price)*Decimal(data['weight'])
        volume_charge = Decimal(volume_unit_price) * Decimal(data['volume'])
        #比大小
        max_price = Decimal.max(pkgs_charge,weight_charge)
        max_price = Decimal.max(max_price,volume_charge)   
        #进十位
        return price_to_ten(max_price)


    #上下车费,超大，夜间算法
    def warehouse_in_ows_night(self,data):
        #清洗数据，单独计算超大货的上下车费。
        pattern = re.compile(r'(\d+(\.\d+)?)([xX*\.](\d+(\.\d+)?))+')
        ows_data = []
        normal_data = []
        for i in data:
            match = pattern.match(i[4])
            dimensions = [float(num) for num in re.findall(r'\d+(\.\d+)?', match)]
            if any(dim > 300 for dim in dimensions) or i[3] >=3.00:
                #将超大货的数据信息移动到OWS_DATA中
                ows_data.append(i)
            else:
                normal_data.append(i)
        


    def main(self):
        #按车分离数据
        for i in self.cfs_wg_data: 
            #判断入库时间，修改cfs-price 的标准
            self.warehouse_time(i[0])
            
                #上下车费+10块
                pkgs_price = Decimal(self.cfs_stander['cfs_yg_pkgs_charge']) + Decimal(10)
                weight_price = Decimal(self.cfs_stander['cfs_yg_weight_charge']) + Decimal(10) 
                volume_price = Decimal(self.cfs_stander['cfs_yg_cmb_charge']) + Decimal(10) 

            