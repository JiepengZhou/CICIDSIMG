import os
import tarfile

def extract_images_and_count(data_dir, extract_dir):
    # 创建目标解压目录
    os.makedirs(extract_dir, exist_ok=True)

    # 用于记录每个类别的图片数量
    image_counts = {}

    # 遍历 tar.gz 文件
    for tar_file in os.listdir(data_dir):
        if tar_file.endswith(".tar.gz"):
            # 获取类别名
            class_name = tar_file.split(".tar.gz")[0]
            class_extract_path = os.path.join(extract_dir, class_name)

            # 解压当前 tar.gz 文件
            with tarfile.open(os.path.join(data_dir, tar_file), 'r:gz') as tar:
                tar.extractall(extract_dir)
                print(f"Extracted {tar_file} to {extract_dir}")

            # 统计该类别文件夹内的图片数量
            image_files = [f for f in os.listdir(class_extract_path) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
            image_counts[class_name] = len(image_files)

    # 打印统计结果
    print("\nImage Count Summary:")
    for class_name, count in image_counts.items():
        print(f"Category '{class_name}': {count} images")

# 运行代码
extract_images_and_count('dataset/tar_files', 'dataset/extracted')
