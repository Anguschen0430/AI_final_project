import os
import shutil

# 定義情感標識符對應的情感名稱
emotion_map = {
    '01': 'neutral',
    '02': 'calm',
    '03': 'happy',
    '04': 'sad',
    '05': 'angry',
    '06': 'fearful',
    '07': 'disgust',
    '08': 'surprised'
}

def organize_files(src_folder, dest_folder):
    # 檢查並創建目標文件夾中的情感文件夾
    for emotion in emotion_map.values():
        emotion_folder = os.path.join(dest_folder, emotion)
        if not os.path.exists(emotion_folder):
            os.makedirs(emotion_folder)
            print(f"創建文件夾: {emotion_folder}")

    # 遍歷源目錄中的所有文件
    for root, dirs, files in os.walk(src_folder):
        for file in files:
            if file.endswith('.wav'):
                # 解析文件名
                parts = file.split('-')
                emotion_code = parts[2]  # 第三部分是情感標識符
                emotion_name = emotion_map.get(emotion_code, 'unknown')

                # 構建源文件和目標文件的路徑
                src_file = os.path.join(root, file)
                dest_file = os.path.join(dest_folder, emotion_name, file)

                try:
                    # 移動文件
                    shutil.move(src_file, dest_file)
                    print(f"移動文件: {src_file} 到 {dest_file}")
                except Exception as e:
                    print(f"移動 {src_file} 失敗: {e}")

# 使用示例
source_directory = "source"
destination_directory = "datasets"
organize_files(source_directory, destination_directory)
