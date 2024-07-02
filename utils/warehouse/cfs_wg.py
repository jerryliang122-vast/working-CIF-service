import logging
from decimal import Decimal, ROUND_UP
import re
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
    #上下车费,超大，夜间算法
    def warehouse_in_ows_night(self,data):
        #获取货物数据，按照超大修改OWS单价
        ows = Decimal(self.cfs_stander['']



    def main(self):
        #按车分离数据
        for i in self.cfs_wg_data: 
            #判断入库时间，修改cfs-price 的标准
            self.warehouse_time(i[0])
            
                #上下车费+10块
                pkgs_price = Decimal(self.cfs_stander['cfs_yg_pkgs_charge']) + Decimal(10)
                weight_price = Decimal(self.cfs_stander['cfs_yg_weight_charge']) + Decimal(10) 
                volume_price = Decimal(self.cfs_stander['cfs_yg_cmb_charge']) + Decimal(10) 

            