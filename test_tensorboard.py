from torch.utils.tensorboard import SummaryWriter
import numpy as np
from PIL import Image

writer=SummaryWriter("logs")
img_path="dataset/train/ants/6743948_2b8c096dda.jpg"
img_PIL=Image.open(img_path)
img_array=np.array(img_PIL)#PIL转化为numpy


writer.add_image("train",img_array,2,dataformats='HWC')
# y=x
for i in range(100):
    writer.add_scalar("y=2x",2*i,i)

writer.close()