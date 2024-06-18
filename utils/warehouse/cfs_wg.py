import logging
from decimal import Decimal, ROUND_UP

logger = logging.getLogger("my_logger")


class calculate_cfs_wg():
    def __init__(self, cfs_wg_data,cfs_stander):
        """
        需要写入列表[[[10, True, 'HWMAA2400934N-MF'], [[[False, '20', '200.000', '0.661', '36.0×34.0×27.0']]]], [[16, True, 'HWMAA2400934N-MF'], [[[False, '24', '175.000', '0.800', '35.0×34.0×28.0']]]]]
        """
        self.cfs_wg_data = cfs_wg_data
        self.cfs_stander = cfs_stander 
    
    #检查货物是否是夜间
    def time_type(self,data):
        
        