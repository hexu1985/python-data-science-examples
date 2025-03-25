anaconda环境搭建:

首先安装anaconda

然后, 创建一个新的虚拟环境
```
# matplotlib_env是环境的名字 
$ conda create -n matplotlib_env python=3
```

激活环境
```
$ conda activate matplotlib_env
```

查看安装包
```
$ conda list
```

安装相关依赖
```
$ conda install numpy
$ conda install matplotlib
```

退出环境
```
$ conda deactivate
```
