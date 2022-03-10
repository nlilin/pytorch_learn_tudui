import torchvision
from torch.utils.tensorboard import SummaryWriter
from torchvision import transforms
# from PIL import Image

dataset_transforms=transforms.Compose([transforms.ToTensor()])

train_set=torchvision.datasets.CIFAR10(root="./data",train=True,transform=dataset_transforms,download=True)
test_set=torchvision.datasets.CIFAR10(root="./data",train=False,transform=dataset_transforms,download=True)

# img,target=test_set[0]
# img.show()

writer=SummaryWriter("log3")
for i in range(10):
    img,target=test_set[i]
    writer.add_image("dataset",img,i)

writer.close()
