import os
import numpy as np
# from libro import libro as lf
import libro as lf
from lstm import DNN, LSTM
import plot
import configs
import warnings
warnings.filterwarnings("ignore")

def predict(config, audio_path: str, model) -> None:
    """ predict the emotion frequency """

    # utils.play_audio(audio_path)


    test_feature = lf.get_data(config, audio_path, train=False)

    result = model.predict(test_feature)
    result_prob = model.predict_proba(test_feature)
    print('Recogntion: ', config.class_labels[int(result)])
    print('Probability: ', result_prob)
    plot.radar(result_prob, config.class_labels)


if __name__ == '__main__':
    audio_path = '/Users/angus/Downloads/新錄音 22.m4a'
    
    # audio_path = input("Input audio_path: ")
    # if os.path.exists(audio_path):
    #     print("文件存在")
    # else:
    #     print("文件不存在")
    # config = utils.parse_opt()
    # 搭建模型

    model = LSTM.load(configs.checkpoint_path,configs.checkpoint_name)
    predict(configs, audio_path, model)
