# -*- coding:utf-8 -*-

import matplotlib as mpl
import matplotlib.pyplot as plt

mpl.rcParams["font.sans-serif"] = ["SimHei"]
mpl.rcParams["axes.unicode_minus"] = False

elements = ["面粉", "砂糖", "奶油", "草莓酱", "坚果"]

weight = [40, 15, 20, 10, 15]

colors = ["#1b9e77", "#d95f02", "#7570b3", "#66a61e", "#e6ab02"]

wedges, texts, autotexts = plt.pie(weight,
                                autopct="%3.1f%%",
                                textprops=dict(color="w"),
                                colors=colors)

plt.legend(wedges,
        elements,
        fontsize=12,
        title="配料表",
        loc="center left",
        bbox_to_anchor=(0.91, 0, 0.3, 1))

plt.setp(autotexts, size=15, weight="bold")
plt.setp(texts, size=12)

plt.title("果酱面包配料比例表")

plt.show()

