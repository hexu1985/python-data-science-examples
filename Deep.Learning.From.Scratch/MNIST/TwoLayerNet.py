import numpy as np
from collections import OrderedDict
import calculate


class TwoLayerNet:
    """有两个Affine层的全连接神经网络"""

    def __init__(self, input_size, hidden_size, output_size, weight_init_std=0.01):
        # 初始化权重
        self.params = {}
        self.params["W1"] = weight_init_std * np.random.randn(input_size, hidden_size)
        self.params["b1"] = np.zeros(hidden_size)
        self.params["W2"] = weight_init_std * np.random.randn(hidden_size, output_size)
        self.params["b2"] = np.zeros(output_size)

        # 生成层
        self.layers = OrderedDict()
        self.layers["Affine1"] = calculate.Affine(self.params["W1"], self.params["b1"])
        self.layers["Relu1"] = calculate.Relu()
        self.layers["Affine2"] = calculate.Affine(self.params["W2"], self.params["b2"])

        self.lastLayer = calculate.SoftmaxWithLoss()

    def predict(self, x):
        """前向传播推理(不包括输出层 )"""
        for layer in self.layers.values():
            x = layer.forward(x)

        return x

    def loss(self, x, t):
        """计算损失函数值-x:输入数据,t:监督数据"""
        y = self.predict(x)
        return self.lastLayer.forward(y, t)

    def accuracy(self, x, t):
        """计算识别精度"""
        y = self.predict(x)
        y = np.argmax(y, axis=1)
        if t.ndim != 1:
            t = np.argmax(t, axis=1)

        accuracy = np.sum(y == t) / float(x.shape[0])
        return accuracy

    def gradient(self, x, t):
        """通过反向传播法计算关于权重参数的梯度"""
        # 前向传播
        self.loss(x, t)

        # 反向传播
        dout = self.lastLayer.backward()

        layers = list(self.layers.values())
        layers.reverse()
        for layer in layers:
            dout = layer.backward(dout)

        # 设定
        grads = {}
        grads["W1"], grads["b1"] = self.layers["Affine1"].dW, self.layers["Affine1"].db
        grads["W2"], grads["b2"] = self.layers["Affine2"].dW, self.layers["Affine2"].db

        return grads
