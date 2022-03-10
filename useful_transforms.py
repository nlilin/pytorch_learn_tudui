from PIL import Image
from torch.utils.tensorboard import SummaryWriter
from torchvision import transforms

writer=SummaryWriter("log1")

img=Image.open("dataset/train/ants/20935278_9190345f6b.jpg")


#Totensor使用
trans_totensor=transforms.ToTensor()
tensor_img=trans_totensor(img)
writer.add_image("tensor_img",tensor_img)
writer.close()

#normalize
trans_norm=transforms.Normalize([1,2,3],[1,3,2])
img_nor=trans_norm(tensor_img)
writer.add_image("normalize",img_nor,2)
writer.close()

#resize
print(img.size)
trans_resize=transforms.Resize((512,512))
img_resize=trans_resize(img)
img_resize=trans_totensor(img_resize)
writer.add_image("resize",img_resize,0)
writer.close()

# compose
trans_resize_2=transforms.Resize(512)
trans_compose=transforms.Compose([trans_resize_2,trans_totensor])
img_resize_2=trans_compose(img)
writer.add_image("resize_2",img_resize_2,1)
writer.close()

#randomcrop
trans_random=transforms.RandomCrop((200,200))
trans_compose_2=transforms.Compose([trans_random,trans_totensor])
for i in range(10):
    img_crop=trans_compose_2(img)
    writer.add_image("img_random",img_crop,i)
writer.close()