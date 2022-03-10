# dataset怎末获取数据，进行编号
# 图片的路径
from torch.utils.data import Dataset
from PIL import Image
import os

class mydata(Dataset):
        def __init__(self,root_dir,label_dir):
                self.root_dir=root_dir
                self.label_dir=label_dir
                self.path=os.path.join(self.root_dir,self.label_dir)
                self.img_path=os.listdir(self.path)

        def __getitem__(self, idx):
                img_name=self.img_path[idx]
                img_item_path=os.path.join(self.path,img_name)
                img=Image.open(img_item_path)
                label=self.label_dir
                return img,label

        def __len__(self):
                return len(self.img_path)

root_dir="dataset/train"
ant_dir="ants"
bee_dir="bees"
ant_dataset=mydata(root_dir,ant_dir)
bee_dataset=mydata(root_dir,bee_dir)
dataset=bee_dataset+ant_dataset
len(dataset)