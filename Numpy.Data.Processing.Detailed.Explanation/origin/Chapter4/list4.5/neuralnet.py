import numpy as np

# 使用类似shape_list = [784, 100, 10]的语句，将每个网络层中神
# 经元的数量作为数组进行输入
def make_params(shape_list):
    weight_list = []
    bias_list = []
    for i in range(len(shape_list)-1):
        # 将服从标准正态分布的随机数作为初始值
        weight = np.random.randn(shape_list[i], shape_list[i+1])
        # 将初始值全部设置为0.1
        bias = np.ones(shape_list[i+1])/10.0
        weight_list.append(weight)
        bias_list.append(bias)
    return weight_list, bias_list