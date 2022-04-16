# 数据集处理，从不同路径读取图片并输出到同一目录
import os
import numpy as np
import cv2

file_root = 'D:\\大海大\\数据集\\MoCA_Video\\TrainDataset_per_sq\\'  # 当前文件夹下的所有图片
file_list = os.listdir(file_root)
save_out = "D:\\大海大\\数据集\\MoCA\\test1\\"  # 保存图片的文件夹名称

# folderlist = os.listdir(file_root)  # 列举文件夹

list_1 = ['elephant']  # 列举所有需要选择的子文件夹
for folder in list_1:
    base_dir = os.path.join(file_root, folder)
    # print(base_dir)
    path_Imgs = os.path.join(base_dir, "Imgs")  # D:\大海大\数据集\MoCA_Video\TrainDataset_per_sq\crab\Imgs
    path_GT = os.path.join(base_dir, "GT")

    total_num_folder = len(list_1)  # 文件夹的总数
    print('total have %d folders' % total_num_folder)  # 打印文件夹的总数
    # print(path_Imgs)
    # exit()
    filelist = os.listdir(path_Imgs)  # 列举图片
    i = 0
    for item in filelist:
        total_num_file = len(filelist)  # 单个文件夹内图片的总数
        if item.endswith('.jpg'):
            src = os.path.join(os.path.abspath(path_Imgs), item)  # 原图的地址
            dst = os.path.join(os.path.abspath(save_out), str(folder) + '_' + str(
                i) + '.jpg')  # 新图的地址（这里可以把str(folder) + '_' + str(i) + '.jpg'改成你想改的名称）


            try:
                os.rename(src, dst)
                print('converting %s to %s ...' % (src, dst))
                i += 1
            except:
                continue

    print('total %d to rename & converted %d jpgs' % (total_num_file, i))
