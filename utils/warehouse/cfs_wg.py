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

#将货物数据分类为托盘，散货
def classify_goods(goods):
    #托盘
    pallets =[]
    #散货
    loss_goods = []
    for each in goods:
        if each['pkgs_type'] == True:
            #托盘
            pallets.append(each)
        else:
            #散货
            loss_goods.append(each)
    return pallets, loss_goods

def main(data, stander):
    #将总数据中每辆车数据提取出来
    for each_cargo in data:
        #将货物数据分类为托盘，散货
        pallets, loss_goods = classify_goods(each_cargo['goods'])
    


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