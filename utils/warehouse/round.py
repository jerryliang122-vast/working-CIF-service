from decimal import Decimal, ROUND_UP
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
