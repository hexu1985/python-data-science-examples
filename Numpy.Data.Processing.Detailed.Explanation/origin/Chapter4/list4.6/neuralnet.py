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

