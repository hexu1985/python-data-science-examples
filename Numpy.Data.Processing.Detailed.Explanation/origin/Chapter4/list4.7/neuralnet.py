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