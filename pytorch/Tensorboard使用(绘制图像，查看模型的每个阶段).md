## Tensorboard使用

绘制图像，查看模型的每个阶段的不同输出

### 函数

from utils.tensorboard  import  Summarywriter

writer.summarywriter("   ")

writer.add_image()

writer.add_scalar()

### 安装Tensorboard

tensorboard --logdir=logs

tensorboard --logdir=logs --port=6060



