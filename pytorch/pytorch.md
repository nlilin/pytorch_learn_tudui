# Pytorch环境的配置及安装 

## anaconda安装

检验是否安装成功：
（1）点击开始菜单栏，打开Anaconda文件夹下的Anaconda Prompt

（2）在弹出的命令行窗口中看到base，即说明安装成功

## 查看GPU型号及其驱动是否正常安装

1、在窗口底部右击打开任务管理器

2、点击性能，找到GPU，如果能正常显示型号，则说明驱动已经正常安装

## 有序的管理环境（使用Anaconda集成的conda包）

（1）开始菜单->Anaconda文件夹->Anaconda Prompt

输入`conda create -n pytorch python=3.6`

查看环境中的工具包：`pip list`

## PyTorch的安装

（1）进入PyTorch官网首页：https://pytorch.org/

（2）下拉到安装页面

```
PyTorch Bulid：一般选择稳定版（Stable）
  Your OS：根据自己的操作系统进行选择
  Package：主要涉及安装方式，Windows系统一般选择Conda，Linux系统一般选择Pip
  Language:选择Python
  CUDA：情况一：无英伟达显卡或只有集显，选择None
        情况二：有英伟达显卡且支持CUDA，推荐使用9.2
  Run this Command：安装指令，复制后用来安装
```

（3）检查是否可以安装CUDA

①、 查询GPU是否支持CUDA：[查询GPU是否支持CUDA](https://www.cnblogs.com/ptxiaochen/p/13781936.html)
②、查看GPU驱动版本，因为CUDA9.2以上只支持驱动版本大于**392.26**的，查看GPU驱动版本的方法见博客：[Windows使用nvidia-smi查看GPU信息](https://www.cnblogs.com/ptxiaochen/p/13782457.html)，驱动版本低于**392.26**需要进行升级，升级方法见博客：[NVDIA的GPU驱动升级](https://www.cnblogs.com/ptxiaochen/p/13782647.html)

附：CUDA的介绍见:[CUDA](https://www.cnblogs.com/ptxiaochen/p/13781565.html)

（4）打开Anaconda Prompt，切换到pytorch环境（新环境）

（5）切换conda源为清华镜像源，参考博客：[conda更换为清华镜像源](https://www.cnblogs.com/ptxiaochen/p/13783102.html)

（6）安装cudnn（可能可以省略）

```go
`conda install cudnn`
```

（7）修改Anaconda文件夹权限(不然后面可能会出问题)

找到Anaconda文件夹，右击点击**属性**，点击安全，选择SYSTEM，点击**确定**

（8）输入复制的安装命令，但是要把命令后缀的-c pytorch **删除！！！**

（9）验证是否安装成功

输入`pip list`，发现torch的版本

输入`python`,输入`import torch`,没有报错

输入`torch.cuda.is_available()`,返回*True*

# pytorch介绍

