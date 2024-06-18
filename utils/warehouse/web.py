import httpx
from bs4 import BeautifulSoup
import datetime
import re
from decimal import Decimal, ROUND_UP
import logging

logger = logging.getLogger("my_logger")


def big_calculator(dims):
    # 检查输入的是10*10*10还是10x10x10
    if re.match(r"^\d+(\.\d+)?[.*xX×]\d+(\.\d+)?[.*xX×]\d+(\.\d+)?$", dims):
        dims = re.sub(r"[.*xX×]", "x", dims).split("x")
    else:
        # 引发异常
        raise ValueError("输入的尺寸格式不正确")
    # 计算该货物是否超大,如果大于3M
    if (
        Decimal(dims[0]) > Decimal("300")
        or Decimal(dims[1]) > Decimal("300")
        or Decimal(dims[2]) > Decimal("300")
    ):
        return True
    elif Decimal(dims[0]) * Decimal(dims[1]) * Decimal(dims[2]) > Decimal("3000000"):
        return True
    else:
        return False
    
# 构建一个正常浏览器型号
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
}


# 构建凤威地址
def fengwei_url(no):
    url = f"http://h5qa.izuiyou.com/Public/InWhsRecord.aspx?no={no}"
    return url


# 构建洋山地址
def yangshan_url(no):
    url = f"http://47.103.36.170/Public/InWhsRecord.aspx?no={no}"
    return url


# 读取地址的HTML 信息使用HTTPS
def get_html(url):
    with httpx.Client() as client:
        # 访问URL并获取响应
        response = client.get(url=url, headers=headers, timeout=30)
        # 解析html
        html = response.text
        return html


# 解析有几个
# 解析异常情况
def parse_html(html):
    # 使用beautifulsoup4 解析html
    soup = BeautifulSoup(html, "html.parser")
    # 初始化id的后缀
    suffix = 1
    # 初始化列表
    exceptions = []
    while True:
        # 构建id
        id = f"ctl00_content_rptReceiptData_ctl{str(suffix).zfill(2)}_psqk"
        # 查找元素
        element = soup.find("td", id=id)
        # 如果元素不存在，跳出循环
        if element is None:
            break
        # 否则，获取文本并添加到列表中
        exception_text = element.get_text(strip=True)
        exceptions.append(exception_text)
        # id后缀加1
        suffix += 1
    # 返回异常列表
    return suffix


# 获取长宽高测量信息
def get_measurement(html, suffix):
    # 使用BeautifulSoup解析HTML
    soup = BeautifulSoup(html, "html.parser")

    id = f"ctl00_content_rptReceiptData_ctl0{suffix}_receiptDetail"
    # 找到表格
    table = soup.find("tr", id=id)
    # 找到包含'长×宽×高'的表头
    header_ckg = table.find("th", string=lambda s: "长×宽×高" in s)
    header_js = table.find("th", string=lambda s: "件数" in s)
    header_bz = table.find("th", string=lambda s: "包装" in s)
    header_zl = table.find("th", string=lambda s: "重量" in s)
    header_tj = table.find("th", string=lambda s: "体积" in s)
    # 获取'长×宽×高'所在的列索引
    column_index_ckg = header_ckg.parent.find_all("th").index(header_ckg)
    # 获取 测量件数 所在的列索引
    column_index_js = header_js.parent.find_all("th").index(header_js)
    column_index_bz = header_bz.parent.find_all("th").index(header_bz)
    column_index_zl = header_zl.parent.find_all("th").index(header_zl)
    column_index_tj = header_tj.parent.find_all("th").index(header_tj)

    # 找到包含具体数值的数据行
    data_rows = table.find_all("tr")
    # 准备一个列表
    measurements = []
    for row in data_rows:
        cells = row.find_all("td")
        if len(cells) > column_index_ckg:
            # 获取'长×宽×高'所在的单元格
            bz = cells[column_index_bz]
            ckg = cells[column_index_ckg]
            js = cells[column_index_js]
            zl = cells[column_index_zl]
            tj = cells[column_index_tj]
            # 获取单元格的文本内容并添加到列表中
            measurements.append(
                [
                    bz.get_text(strip=True),
                    js.get_text(strip=True),
                    zl.get_text(strip=True),
                    tj.get_text(strip=True),
                    ckg.get_text(strip=True),
                ]
            )
    
    return measurements


# 获取收货入库的主程序
def get_data(html, suffix):
    # 使用BeautifulSoup解析HTML
    soup = BeautifulSoup(html, "html.parser")
    # 登记时间
    registration_time = f"ctl00_content_rptReceiptData_ctl0{suffix}_djsj"
    # 车型
    cx = f"ctl00_content_rptReceiptData_ctl0{suffix}_cx"
    # 进仓编号
    jcbh = f"ctl00_content_rptReceiptData_ctl0{suffix}_jcbh"

    element_registration_time = soup.find("td", id=registration_time)
    element_cx = soup.find("td", id=cx)
    element_jcbh = soup.find("td", id=jcbh)
    return [
        element_registration_time.get_text(strip=True),
        element_cx.get_text(strip=True),
        element_jcbh.get_text(strip=True),
    ]


class web_grasp:
    def __init__(self, warehouse, no):
        """
        类的初始化方法。

        :param warehouse: 布尔值，true表示使用洋山仓库，false表示使用凤威仓库。
        :param no: 字符串，仓库或场地的编号。
        :return: 无返回值。
        """
        if warehouse == True:
            url = yangshan_url(no)
        else:
            url = fengwei_url(no)
        self.data_html = get_html(url)

    # 修改时间
    def change_time(self, data):
        # 2023-11-04 21:35 将这个时间转化成datatime
        data_time = datetime.datetime.strptime(data, "%Y-%m-%d %H:%M")
        # 读取data_time中的时间
        return data_time.hour

    def get_data(self):
        """
        获取收货入库的数据。
        """
        suffix = parse_html(self.data_html)
        data = []
        for i in range(1, suffix):
            data_list = []
            cargo_data = get_data(self.data_html, i)
            cargo_data_list = get_measurement(self.data_html, i)
            date_time = self.change_time(cargo_data[0])
            # 更换cargo_data[0]的值为date_time
            cargo_data[0] = date_time
            if cargo_data[1] == "厢式车":
                cargo_data[1] = True
            else:
                cargo_data[1] = False
            # 修改data列表 中的托盘判断
            cargo_data_list_new = []
            for i in cargo_data_list:
                if i[0] == "托":
                    i[0] = True
                else:
                    i[0] = False
                cargo_data_list_new.append(i)
            data_list.append(cargo_data_list_new)
            data.append([cargo_data, data_list])
        return data

if __name__ == "__main__":
    data = web_grasp(False, "HWMAA2400934N-MF")
    print(data.get_data())