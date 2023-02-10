import os
import fitz


# pdf 转图片
def pdf_to_jpg(pdf_path):
    # 创建这个文件文件名的文件夹
    file_name = pdf_path.split("\\")[-1].split(".")[0]
    # 读取当前工作目录
    current_path = os.getcwd()
    # 创建文件夹
    if not os.path.exists(os.path.join(current_path, "data", "BL-JPG", file_name)):
        os.mkdir(os.path.join(current_path, "data", "BL-JPG", file_name))
    # 配置图片保存路径
    imgPath = os.path.join(current_path, "data", "BL-JPG", file_name) + "\\"
    # 打开pdf文件
    doc = fitz.open(pdf_path)
    # 设置图片分辨率
    zoom_x = 2.0
    zoom_y = 2.0
    # 设置图片旋转角度
    rotation_angle = 0
    # 逐页读取PDF
    for pg in range(doc.pageCount):
        page = doc[pg]
        trans = fitz.Matrix(zoom_x, zoom_y).preRotate(rotation_angle)
        pm = page.getPixmap(matrix=trans, alpha=False)
        # 开始写图像
        pm.writePNG(imgPath + str(pg) + ".png")
        doc.close()
