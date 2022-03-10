pytorch加载数据有两个类dataset和dataloader

dataset:提供获取数据及其label方式

​		如何获取每个数据及其label

​		告诉我们总共有多少数据

​		**告诉我们每个数据在哪里，每个数据是什么**

dataloader：为后面的网络提供不同的数据形式

dataset:下载数据集

from PIL import Image

img.open()打开地址的图片

img.show()展示图片