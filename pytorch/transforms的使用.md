## transforms的使用

图像的转化裁剪

transforms.py工具箱

from torchvision import transforms

输入   PIL   Image.open()

输出    tensor  totensor()

作用    narrays   cv.imread()



transrorms.totensor()

transforms.normalize()：``output[channel] = (input[channel] - mean[channel]) / std[channel]``