import os

# 이미지 폴더 경로 설정
image_folder = "/home/ccm/ros2_ws/saved_images_b_2/"

# 이미지 파일 형식 지정 (예: .jpg, .png 등)
image_format = ".jpg"

# 이미지 파일 순서대로 이름을 변경
start_number = 170

# 이미지 폴더에서 파일 리스트 가져오기
file_list = os.listdir(image_folder)

# 파일 리스트를 정렬
file_list.sort()

# 이미지 파일 이름 변경
for idx, filename in enumerate(file_list):
    old_path = os.path.join(image_folder, filename)
    new_path = os.path.join(image_folder, f"deli{start_number + idx}{image_format}")

    os.rename(old_path, new_path)

print(f"{len(file_list)} images renamed.")
