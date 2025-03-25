import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 500)
y1 = np.sin(x) # 向原有信号中混入噪声
y2 = y1 + np.random.randn(500)*0.3 #混合噪音
v = np.ones(5)/5.0  # 设置用于计算移动平均值的数组，这里将对前后5个
                             # 值取平均
y3 = np.convolve(y2, v, mode='same')
# 为了方便绘图，设置为'same'

plt.plot(x, y1, 'k', linestyle='solid', linewidth=2)
plt.plot(x, y2, 'b', linestyle='dotted',linewidth=1)
plt.plot(x, y3, 'b', linestyle='solid', linewidth=2)
plt.show()

