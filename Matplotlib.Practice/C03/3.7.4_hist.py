
# -*- coding:utf-8 -*-

import matplotlib as mpl

mpl.rcParams["font.sans-serif"] = ["SimHei"]
mpl.rcParams["axes.unicode_minus"] = False

import matplotlib.pyplot as plt
import numpy as np

# set test scores
scoresT1 = np.random.randint(0,100,100)
scoresT2 = np.random.randint(0,100,100)

x = [scoresT1, scoresT2]
colors = ["#8dd3c7", "#bebada"]
labels = ["班级A", "班级B"]

# plot histogram
bins = range(0,101,10)

plt.hist(x, bins=bins,
        color=colors,
        histtype="bar",
        rwidth=10,
        stacked=True,
        label=labels)

# set x,y-axis label
plt.xlabel("测试成绩")
plt.ylabel("学生人数")

plt.title("不同班级的测试成绩的直方图")

plt.legend(loc="upper left")

plt.show()
