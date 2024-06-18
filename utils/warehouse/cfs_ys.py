import logging
from decimal import Decimal, ROUND_UP

logger = logging.getLogger("my_logger")


class calculate_cfs_YS():
    def __init__(self, cfs_wg_data,cfs_stander):
        """
        需要写入一个字典。字典需要定义件数pkgs，重量weight，体积volume，尺寸dims，超大超重货物oversize，
        是否是托盘货物pallets，时间times
        """
        self.cfs_wg_data = cfs_wg_data
        self.cfs_stander = cfs_stander 
    
    def warehouse_in_out(self):
        """
        计算上下车费
        """
        # 如果是超大费，则直接把超大费的单价加到普通费用中
        if self.cfs_wg_data['oversize'] == True:  # 
            self.cfs_stander['pkgs'] = Decimal(self.cfs_stander['pkgs']) + Decimal(self.cfs_stander['oversize'])  # 超大费的件数费用
            self.cfs_stander['weight'] = Decimal(self.cfs_stander['weight']) + Decimal(self.cfs_stander['oversize'])  # 超大费的重量费用
            self.cfs_stander['volume'] = Decimal(self.cfs_stander['volume']) + Decimal(self.cfs_stander['oversize'])  # 超大费的体积费用
        #如果是夜间
        if self.cfs_wg_data['times'] == True:  # 夜间费率
            self.cfs_stander['pkgs'] = Decimal(Decimal(self.cfs_stander['pkgs']) * Decimal(1.3)).quantize(Decimal(1),rounding=ROUND_UP)  # 夜间费的件数费用
            self.cfs_stander['weight'] = Decimal(Decimal(self.cfs_stander['weight']) * Decimal(1.3)).quantize(Decimal(1),rounding=ROUND_UP)  # 夜间费的重量费用
            self.cfs_stander['volume'] = Decimal(Decimal(self.cfs_stander['volume']) * Decimal(1.3)).quantize(Decimal(1),rounding=ROUND_UP)  # 夜间费的体积费用
        # 查看是否是托盘货物，如果是托盘货物，计算托盘费用，否者直接为0
        if self.cfs_wg_data['pallets'] == True:  # 托盘货物
            pkgs_price = Decimal(self.cfs_wg_data['pkgs']) * Decimal(self.cfs_stander['pkgs'])  # 托盘费用
        else:
            pkgs_price = Decimal(0)  # 不是托盘货物，费用为0
        # 计算重量费用
        weight_price = Decimal(self.cfs_wg_data['weight'])/Decimal(1000) * Decimal(self.cfs_stander['weight'])  # 重量费用
        # 计算体积费用
        volume_price = Decimal(self.cfs_wg_data['volume'])* Decimal(self.cfs_stander['volume'])  # 体积费用

        #开始取大小
        price = Decimal.max(pkgs_price, weight_price)  # 取最大值，即取最大费用
        price = Decimal.max(price, volume_price)  # 取最大值，即取最大费用
        #如果是夜间
        if self.cfs_wg_data['times'] == True:  # 夜间费率
            price = Decimal(price) * Decimal(1.3)  # 夜间费

        #进行进位取整