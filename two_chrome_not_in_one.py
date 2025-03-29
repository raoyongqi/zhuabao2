import shutil
import os

# 指定要删除的目录路径
folder_path = r"C:\Users\r\AppData\Local\Chromium\User Data"

# 检查目录是否存在
if os.path.exists(folder_path):
    try:
        # 使用shutil.rmtree删除文件夹及其中的所有内容
        shutil.rmtree(folder_path)
        print(f"文件夹已成功删除: {folder_path}")
    except Exception as e:
        print(f"删除过程中出现错误: {e}")
else:
    print(f"指定的文件夹不存在: {folder_path}")
