# -*- coding:utf-8 -*-

import matplotlib as mpl
import matplotlib.pyplot as plt

mpl.rcParams["font.sans-serif"] = ["SimHei"]
mpl.rcParams["axes.unicode_minus"] = False

# some simple data
x = [1,2,3,4,5]
y = [6,10,4,5,1]

# create bar
plt.barh(x,y,align="center",color="c",tick_label=["A","B","C","D","E"])

# set x,y_axis label
plt.xlabel("测试难度")
plt.ylabel("试卷份数")

# set yaxis grid
plt.grid(True,axis="x",ls=":",color="r",alpha=0.3)

plt.show()
