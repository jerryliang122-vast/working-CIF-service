import logging
from decimal import Decimal, ROUND_UP
import re
logger = logging.getLogger("my_logger")

def price_to_ten(price: str):
    """
    这是一个进十位的函数
    """
    # 将price转换成decimal
    price = Decimal(price)
    # 先去除小数点
    new_price = price.quantize(Decimal("1"), rounding=ROUND_UP)
    # 除以10
    new_price /= Decimal("10")
    # 去除小数点
    new_price = new_price.quantize(Decimal("1"), rounding=ROUND_UP)
    # 重新乘以10
    new_price *= Decimal("10")
    return new_price

class warehouse_in_out():
    def __init__(self, data,stander):
        self.data = data
        self.stander = stander
    def in_out(self):
        data = self.data
        stander = self.stander
        pkgs_unit_price =Decimal(stander['pkgs_charge'])
        weight_unit_price = Decimal(stander['weight_charge'])
        volume_unit_price = Decimal(stander['volume_charge'])
        # 计算包装费，如果无托盘，则包装费为0
        #计算上下车费，按照货物数据，计算出PKGS WEIGHT 和VOLUME 然后相加，返回结果。
        if data['pkgs_type'] == True:
            pkgs_charge = Decimal(pkgs_unit_price)*Decimal(data['pkgs'])
        else:
            pkgs_charge = Decimal(0)
        # 计算重量费和体积费
        weight_charge = Decimal(weight_unit_price)*Decimal(data['weight'])
        volume_charge = Decimal(volume_unit_price) * Decimal(data['volume'])
        # 计算最大费用，考虑到最小费用门槛
        # 比大小,mini
        max_price = Decimal.max(pkgs_charge,weight_charge)
        max_price = Decimal.max(max_price,volume_charge)   
        max_price = Decimal.max(max_price,Decimal(self.cfs_stander['cfs_yg_mini_charge']))
        # 返回最大费用，保留到10的最小整数
        #进十位
        return price_to_ten(max_price)
    
class cargo_handle():
    """
    货物处理类，用于处理货物数据的合并、分解以及判断是否满足超大费条件。
    """
    def __init__(self,data):
        """
        初始化函数，存储货物数据。

        :param data: 货物数据
        """
        self.data = data

    # 货物数据合并
    def merge_data(self,data):
        """
        合并货物数据，计算总件数、总重量和总体积。

        :param data: 待合并的货物数据列表
        :return: 包含总件数、总重量和总体积的字典，如果数据为空则返回False
        """
        if len(data) == 0:
            return False
        # 初始化货物件数、重量和体积的累加器
        pkgs = Decimal(0)
        weight = Decimal(0)
        volume = Decimal(0)
        # 遍历数据集，累加每个货物的件数、重量和体积
        for i in data:
            pkgs += Decimal(i["pkgs"])
            weight += Decimal(i["weight"])
            volume += Decimal(i["volume"])
        # 返回包含总件数、总重量和总体积的字典
        return {'pkgs':pkgs,'weight':weight,'volume':volume}

    # 判断超大费条件
    def warehous_ows(self,data):
        """
        判断货物是否满足超大费条件，如尺寸超过300cm或体积大于3立方米。

        :param data: 单个货物的数据
        :return: 如果货物满足超大费条件则返回True，否则返回False
        """
        # 正则表达式匹配尺寸数据
        pattern = re.compile(r'(\d+(\.\d+)?)([xX*\.](\d+(\.\d+)?))+')
        match = pattern.match(data["dims"])
        dimensions = [float(num) for num in re.findall(r'\d+(\.\d+)?', match.group())]
        # 检查是否有任一尺寸超过300cm或体积大于等于3立方米
        if any(dim > 300 for dim in dimensions) or float(data['volume']) >=3.00:
            return True
        return False
    
    # 分解货物数据
    def split_data(self):
        """
        分解货物数据，将普通货物、超大货物和托盘货物分开。

        :return: 包含超大货物、普通货物和托盘货物列表的元组
        """
        # 清洗数据，单独计算超大货的上下车费。
        ows_data = [i for i in self.data if self.warehous_ows(i)] # 超大货物
        # 筛选出普通货物的数据
        normal_data = [i for i in self.data if not self.warehous_ows(i) and not i['pkgs_type']] # 普通货物
        # 筛选出托盘货物的数据
        pallet_data = [i for i in self.data if not self.warehous_ows(i) and i['pkgs_type']] # 托盘货物。
        return ows_data,normal_data,pallet_data

    def main(self):
        """
        主处理函数，分解并整理货物数据。

        :return: 包含超大货物、普通货物和托盘货物的字典
        """
        # 合并货物数据
        data = self.split_data()
        ows_cargo_data = data[0]
        normal_cargo_data = data[1]
        pallet_cargo_data = data[2]
        if data[0]:
            ows_cargo_data = self.merge_data(ows_cargo_data)
            ows_cargo_data['pkgs_type'] = ows_cargo_data['pkgs_type']
        if data[1]:
            normal_cargo_data = self.merge_data(normal_cargo_data)
            normal_cargo_data['pkgs_type'] = normal_cargo_data['pkgs_type']
        if data[2]:
            pallet_cargo_data = self.merge_data(pallet_cargo_data)
            pallet_cargo_data['pkgs_type'] = pallet_cargo_data['pkgs_type']
        return {'ows_cargo':ows_cargo_data,'normal_cargo':normal_cargo_data,'pallet_data':pallet_cargo_data}
        
class calculate_warehouse_charge():
    def __init__(self,data,stander):
        self.data = data
        self.stander = stander
    def stander_change(self,night,ows):
        pkgs_charge = Decimal(self.stander['cfs_yg_pkgs_charge']) 
        weight_charge = Decimal(self.stander['cfs_yg_weight_charge']) 
        volume_charge = Decimal(self.stander['cfs_yg_cmb_charge']) 
        if night == True :
            pkgs_charge = pkgs_charge* Decimal(1.3)
            weight_charge = pkgs_charge * Decimal(1.3)
            volume_charge = pkgs_charge* Decimal(1.3)
        if ows == True:
            pkgs_charge = Decimal(pkgs_charge) + Decimal(self.stander['cfs_ows_charge'])
            weight_charge = Decimal(weight_charge) + Decimal(self.stander['cfs_ows_charge'])
            volume_charge = Decimal(volume_charge) + Decimal(self.stander['cfs_ows_charge'])
        return {'pkgs_charge':pkgs_charge,'weight_charge':weight_charge,'volume_charge':volume_charge}
        
    def warehouse_time(self,data):
        #判断时间在18年之后早上8点之前
        if data >=18 or data <= 8: 
            return True
        else:
            return False    
    def main(self):
        #查看货物时间
        warehouse_time = self.warehouse_time(self.data['time'])
        #清洗数据，将超大货物分开,并合并货物
        cargo_calculate_data = cargo_handle(self.data['goods'])
        data = cargo_calculate_data.main()
        #按照货物数据修改仓储标准，并计算仓库费用
        if data['ows_cargo']:
            stander = self.stander_change(warehouse_time,True)
            calculate_inout = warehouse_in_out(data['ows_cargo'],stander)
            print(calculate_inout.in_out())
        if data['normal_cargo']:
            stander = self.stander_change(warehouse_time,False)
            calculate_inout = warehouse_in_out(data['normal_cargo'],stander)
            print(calculate_inout.in_out())
        if data['pallet_data']:
            stander = self.stander_change(warehouse_time,False)
            calculate_inout = warehouse_in_out(data['pallet_data'],stander)
            print(calculate_inout.in_out())

class cargo_handle_yg():
    def __init__(self,data):
        self.data = data

def main(stander,data,discount):
    back_data= []
    #获取每次进仓的数据
    for i in data:
        


if __name__ == '__main__':
    data = [
    {
        'time': 10,
        'car_model': True,
        'cargo_id': 'HWMAA2400934N-MF',
        'goods': [
            {
                'pkgs_type': False,
                'pkgs': '20',
                'weight': '200.000',
                'volume': '0.661',
                'dims': '36.0×34.0×27.0'
            }
        ]
    },
    {
        'time': 16,
        'car_model': True,
        'cargo_id': 'HWMAA2400934N-MF',
        'goods': [
            {
                'pkgs_type': False,
                'pkgs': '24',
                'weight': '175.000',
                'volume': '0.800',
                'dims': '35.0×34.0×28.0'
            }
        ]
    }
    ]
    stander = {
    "BL_charge": 1,
    "cfs_Insurance_charge": 1,
    "cfs_ows_charge": 1,
    "cfs_van_charge": 1,
    "cfs_yg_cmb_charge": 1,
    "cfs_yg_mini_charge": 1,
    "cfs_yg_pkgs_charge": 1,
    "cfs_yg_weight_charge": 1,
    "cfs_ys_cbm_charge": 1,
    "cfs_ys_mini_charge": 1,
    "cfs_ys_pkgs_charge": 1,
    "cfs_ys_weight_charge": 1
    }
    main(stander,data,None)