import os
import random
import shutil
from glob import glob


def get_image_files(folder):
    valid_ext = ["jpg", "jpeg", "png", "tif", "tiff", "bmp"]
    return [file for ext in valid_ext for file in glob(os.path.join(folder, f"*.{ext}"))]


# 원본 데이터 폴더 설정
data_folder = "/home/ccm/data-set/1-kcity-flag-dataset/img/"

# train, valid, test 데이터 폴더 설정
train_folder = "/home/ccm/data-set/1-kcity-flag-dataset/train/"
valid_folder = "/home/ccm/data-set/1-kcity-flag-dataset/valid/"
test_folder = "/home/ccm/data-set/1-kcity-flag-dataset/test/"

# 비율 설정
train_ratio = 0.8
valid_ratio = 0.1
test_ratio = 0.1

# 이미지와 텍스트 파일 리스트 가져오기
image_list = get_image_files(data_folder)
file_list = [os.path.join(data_folder, os.path.splitext(img_filename)[0] + ".txt") for img_filename in image_list]

# 랜덤하게 파일을 분할
random.shuffle(image_list)

total_images = len(image_list)
train_num = int(total_images * train_ratio)
valid_num = int(total_images * valid_ratio)
test_num = total_images - train_num - valid_num

# 폴더 생성
for folder in [train_folder, valid_folder, test_folder]:
    if not os.path.exists(folder):
        os.makedirs(folder)

# 분할된 파일을 각각의 폴더에 복사
for idx, img_filename in enumerate(image_list):
    label_filename = os.path.splitext(img_filename)[0] + ".txt"
    ext = os.path.splitext(img_filename)[1]

    if idx < train_num:
        dst_folder = train_folder
    elif idx < train_num + valid_num:
        dst_folder = valid_folder
    else:
        dst_folder = test_folder

    # 이미지 파일 복사
    shutil.copy2(img_filename, os.path.join(dst_folder, f"img{idx + 1}{ext}"))

    # 라벨 파일 복사
    shutil.copy2(label_filename, os.path.join(dst_folder, f"img{idx + 1}.txt"))

print("Data split and copy is completed.")
