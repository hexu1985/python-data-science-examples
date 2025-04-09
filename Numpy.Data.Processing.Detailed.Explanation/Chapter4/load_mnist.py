import pickle
import numpy as np
import gzip

key_file = {
    'x_train':'train-images-idx3-ubyte.gz',
    't_train':'train-labels-idx1-ubyte.gz',
    'x_test':'t10k-images-idx3-ubyte.gz',
    't_test':'t10k-labels-idx1-ubyte.gz'
}

def load_label(file_name):
    file_path = file_name
    with gzip.open(file_path, 'rb') as f:
        #开头的8字节数据并非是需要的内容，因此跳过
        labels = np.frombuffer(f.read(), np.uint8, offset=8)
    one_hot_labels = np.zeros((labels.shape[0], 10))
    for i in range(labels.shape[0]):
        one_hot_labels[i, labels[i]] = 1
    return one_hot_labels

def load_image(file_name):
    file_path = file_name
    with gzip.open(file_path, 'rb') as f:
        #  需要跳过图像本身的16字节的内容
        images = np.frombuffer(f.read(), np.uint8, offset=16)
    return images

def convert_into_numpy(key_file):
    dataset = {}

    dataset['x_train'] = load_image(key_file['x_train'])
    dataset['t_train'] = load_label(key_file['t_train'])
    dataset['x_test'] = load_image(key_file['x_test'])
    dataset['t_test'] = load_label(key_file['t_test'])

    return dataset

def load_mnist():
    # 读取mnist并将其输出为NumPy数组
    dataset = convert_into_numpy(key_file)
    # 指定数据类型为float32
    dataset['x_train'] = dataset['x_train'].astype(np.float32)
    dataset['x_test'] = dataset['x_test'].astype(np.float32)
    dataset['x_train'] /= 255.0
    # 简单的归一化处理
    dataset['x_test'] /= 255.0
    dataset['x_train'] = dataset['x_train'].reshape(-1, 28*28)
    dataset['x_test'] = dataset['x_test'].reshape(-1, 28*28)
    return dataset