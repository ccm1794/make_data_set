import os
import shutil
from glob import glob

# 원본 데이터 폴더 설정
data_folder = "/home/ccm/data-set/1-kcity-flag-dataset/valid/"

# 이미지와 라벨을 저장할 폴더 설정
image_folder = os.path.join(data_folder, "image")
label_folder = os.path.join(data_folder, "label")

# 폴더가 없으면 생성
if not os.path.exists(image_folder):
    os.makedirs(image_folder)

if not os.path.exists(label_folder):
    os.makedirs(label_folder)

# jpg 파일 리스트 가져오기 및 옮기기
jpg_files = glob(os.path.join(data_folder, "*.jpg"))

for jpg_file in jpg_files:
    shutil.move(jpg_file, os.path.join(image_folder, os.path.basename(jpg_file)))

# txt 파일 리스트 가져오기 및 옮기기
txt_files = glob(os.path.join(data_folder, "*.txt"))

for txt_file in txt_files:
    shutil.move(txt_file, os.path.join(label_folder, os.path.basename(txt_file)))

print("jpg files and txt files sorted into their respective folders.")
