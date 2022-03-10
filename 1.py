import torchvision

vgg_true=torchvision.models.vgg16(pretrained=True)
vgg_false=torchvision.models.vgg16(pretrained=False)

# print(vgg_true)
print(vgg_false)