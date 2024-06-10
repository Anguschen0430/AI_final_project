# config.py

# 模型類型
model = "lstm"

# 數據集路徑
data_path = "datasets"  # 數據集存儲位置
class_labels = ["neutral", "calm", "happy", "sad", "angry", "fearful", "disgust", "surprised"]  # 情感標籤
# class_labels:
#   - "01"  # Neutral
#   - "02"  # Calm
#   - "03"  # Happy
#   - "04"  # Sad
#   - "05"  # Angry
#   - "06"  # Fearful
#   - "07"  # Disgust
#   - "08"  # Surprised

# 特徵
feature_folder = "features/8-category"  # 特徵存儲文件夾
feature_method = "l"  # 'o': opensmile, 'l': librosa  # 特徵提取方式


# 檢查點
checkpoint_path = "checkpoints/"  # 檢查點存儲路徑
checkpoint_name = "LSTM_LIBROSA_IS10"  # 檢查點文件名

# 訓練參數
epochs = 20  # 訓練的 epoch 數量
batch_size = 32  # 批次大小
lr = 0.001  # 學習率

# 模型參數
rnn_size = 128  # LSTM 隱藏層大小
hidden_size = 32
dropout = 0.5
