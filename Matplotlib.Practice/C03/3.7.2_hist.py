# -*- coding:utf-8 -*-

import matplotlib as mpl

mpl.rcParams["font.sans-serif"] = ["SimHei"]
mpl.rcParams["axes.unicode_minus"] = False

import matplotlib.pyplot as plt
import numpy as np

# set test scores
scoresT = np.random.randint(0,100,100)

x = scoresT

# plot histogram
bins = range(0,101,10)

plt.hist(x, bins=bins,
        color="#377eb8",
        histtype="bar",
        rwidth=10)

# set x,y-axis label
plt.xlabel("测试成绩")
plt.ylabel("学生人数")

plt.show()
