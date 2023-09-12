#!python
# -*-coding:utf-8 -*-
'''
@File    :   folderSplitting.py
@Time    :   2023/09/12 15:06:57
@Author  :   sourcedream
@Contact :   admin@sourcedream.cn
@License :   (C)Copyright 2023, sourcedream
@Desc    :   文件夹一键拆包
'''
import os
import shutil

folder = input("请输入你要拆包的文件夹\n")

for root, dirs, files in os.walk(folder):
    for file in files:
        source_file = os.path.join(root, file)
        target_file = os.path.join(folder, file)
        count = 1
        while os.path.exists(target_file):
            base_name, ext = os.path.splitext(file)
            new_file_name = f"{base_name}_{count}{ext}"
            target_file = os.path.join(folder, new_file_name)
            count += 1
        shutil.move(source_file, target_file)
for root, dirs, files in os.walk(folder, topdown=False):
    for dir_name in dirs:
        folder_path = os.path.join(root, dir_name)
        if not os.listdir(folder_path):
            try:
                os.rmdir(folder_path)
            except Exception as e:
                print(f'删除空的子文件夹 {folder_path} 时出错：{e}')