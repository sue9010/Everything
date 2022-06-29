import os

folder_path = r"C:\Users\Sue\Desktop\2022 수입신고필증\원본\202204"

file_names = os.listdir(folder_path)
for name in file_names:
    n = name.split('_')
    print(n[1])
    