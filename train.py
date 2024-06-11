from tensorflow.keras.utils import to_categorical
import libro as lf
from lstm import LSTM
import numpy as np
import configs
import matplotlib.pyplot as plt

def curve(train: list, val: list, title: str, y_label: str) -> None:

    plt.plot(train)
    plt.plot(val)
    plt.title(title)
    plt.ylabel(y_label)
    plt.xlabel("epoch")
    plt.legend(["train", "test"], loc="upper left")
    plt.show()

def train(config) -> None:
    """
    训练模型

    Args:
        config: 配置项

    Returns:
        model: 训练好的模型
    """

    # 加载被 preprocess.py 预处理好的特征

    x_train, x_test, y_train, y_test = lf.load_feature(config, train=True)

    # x_train, x_test (n_samples, n_feats)
    # y_train, y_test (n_samples)

    # 搭建模型
    # print(x_train.shape[1])
    model = LSTM.make(x_train.shape[1],configs.rnn_size, configs.hidden_size, configs.dropout, configs.nums_labels, configs.lr)

    # 训练模型
    print('----- start training', config.model, '-----')
    if config.model in ['lstm', 'cnn1d', 'cnn2d']:
        y_train, y_val = to_categorical(y_train), to_categorical(y_test)  # 独热编码
        unique_labels_train = np.unique(y_train)
        unique_labels_test = np.unique(y_test)
        print("Unique labels in training set:", unique_labels_train)
        print("Unique labels in test set:", unique_labels_test)

        
        
        model.train(
            x_train, y_train,
            x_test, y_val,
            batch_size = config.batch_size,
            n_epochs = config.epochs
        )
    else:
        model.train(x_train, y_train)
    print('----- end training ', config.model, ' -----')

    # 验证模型
    model.evaluate(x_test, y_test)
    # 保存训练好的模型
    model.save(config.checkpoint_path, config.checkpoint_name)


if __name__ == '__main__':
    train(configs)
