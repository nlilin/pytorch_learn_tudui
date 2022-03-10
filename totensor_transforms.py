from torch.utils.tensorboard import SummaryWriter
from torchvision import transforms
from PIL import Image


#2.为什莫我们需要tensor数据类型


img_path="dataset/train/ants/0013035.jpg"
img=Image.open(img_path)

writer=SummaryWriter("log2")

#1.transforms该如何使用(python)
#装换成tensor类型的img
trans_ten=transforms.ToTensor()
tensor_img=trans_ten(img)
print(type(tensor_img))



writer.add_image("tensor_img",tensor_img)

writer.close()