import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D #在绘制三维图表时使用

x = np.linspace(-2,2,100)
y = np.linspace(-2,2,100)

xx, yy = np.meshgrid(x, y) #生成网格点的x、y坐标
ret = np.sin(xx**2+yy**2)
def plot1():
    plt.gca().set_aspect('equal', adjustable='box') #将图表的宽高比对齐的命令
    plt.contourf(xx, yy, ret>0, cmap=plt.cm.bone) #满足条件ret>0的部分为白色，不满足条件的部分为黑色。
    plt.show()
def plot2():
    fig = plt.figure()
    ax = Axes3D(fig)
    ax.plot_wireframe(xx, yy, ret)
    ax.axis("equal")
    plt.show()

plot1()
plot2()