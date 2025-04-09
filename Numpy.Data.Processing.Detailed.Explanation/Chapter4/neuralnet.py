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

def sigmoid(x): # Sigmoid函数
    return 1/(1+np.exp(-x))

def inner_product(X, w, b): #  在这里将内积与偏置相加
    return np.dot(X, w)+ b

def activation(X, w, b):
    return sigmoid(inner_product(X, w, b))

# 返回保存了每个网络层的计算结果的数组
def calculate(X, w_list, b_list, t):
    val_list = {}
    a_1 = inner_product(X, w_list[0], b_list[0]) # (N, 1000)
    y_1 = sigmoid(a_1) # (N, 100)
    a_2 = inner_product(y_1, w_list[1], b_list[1]) # (N, 10)
    #  这是原本想要得到的值(N,10)
    y_2 = sigmoid(a_2)
    # 在这里加入简单的归一化处理
    y_2 /= np.sum(y_2, axis=1, keepdims=True)
    S = 1/(2*len(y_2))*(y_2 - t)**2
    L = np.sum(S)
    val_list['a_1'] = a_1
    val_list['y_1'] = y_1
    val_list['a_2'] = a_2
    val_list['y_2'] = y_2
    val_list['S'] = S
    val_list['L'] = L
    return val_list

#在这里进行预测
def predict(X, w_list, b_list, t):
    val_list = calculate(X, w_list, b_list, t)
    y_2 = val_list['y_2']
    result = np.zeros_like(y_2)
    #  相当于样本数
    for i in range(y_2.shape[0]):
        result[i, np.argmax(y_2[i])] = 1
    return result

def accuracy(X, w_list, b_list, t):
    pre = predict(X, w_list, b_list, t)
    result = np.where(np.argmax(t, axis=1)==np.argmax(pre, axis=1), 1, 0)
    acc = np.mean(result)
    return acc
def loss(X, w_list, b_list, t):
    L = calculate(X, w_list, b_list, t)['L']
    return L

#eta为学习率，这里将实现参数的更新操作
def update(X, w_list, b_list, t, eta):
    val_list = {}
    val_list = calculate(X, w_list, b_list, t)
    a_1 = val_list['a_1']
    y_1 = val_list['y_1']
    a_2 = val_list['a_2']
    y_2 = val_list['y_2']
    S = val_list['S']
    L = val_list['L']
    dL_dS = 1.0
    dS_dy_2 = 1/X.shape[0]*(y_2 - t)
    dy_2_da_2 = y_2*(1.0 - y_2)
    da_2_dw_2 = np.transpose(y_1)
    da_2_db_2 = 1.0
    da_2_dy_1 = np.transpose(w_list[1])
    dy_1_da_1 = y_1 * (1 - y_1)
    da_1_dw_1 = np.transpose(X)
    da_1_db_1 = 1.0
    # 从这里开始进行参数的更新操作
    dL_da_2 =  dL_dS * dS_dy_2 * dy_2_da_2
    b_list[1] -= eta*np.sum(dL_da_2 * da_2_db_2, axis=0)
    w_list[1] -= eta*np.dot(da_2_dw_2, dL_da_2)
    dL_dy_1 = np.dot(dL_da_2, da_2_dy_1)
    dL_da_1 = dL_dy_1 * dy_1_da_1
    b_list[0] -= eta*np.sum(dL_da_1 * da_1_db_1, axis=0)
    w_list[0] -= eta*np.dot(da_1_dw_1, dL_da_1)
    return w_list, b_list
