import glob
import os
import random
import shutil
import numpy as np

data_root = '../dataset/archive'
merge_root = '../dataset/after_dealt'
img_dir = 'images'
ann_dir = 'labels'


splits_base_path = 'splits'
train_dir='train'
train_split_txt = os.path.join(merge_root, splits_base_path, 'train.txt')

val_dir='val'
val_split_txt = os.path.join(merge_root, splits_base_path, 'val.txt')

train_pertentage = 0.9
val_percentage = 0.1


def shuffle_and_splie():
    all_list = []
    for img_name in glob.glob(os.path.join(data_root, img_dir, '*')):
        all_list.append(os.path.basename(img_name))

    random.shuffle(all_list)
    total_cnt = len(all_list)
    train_cnt = int(total_cnt * train_pertentage)
    val_cnt = total_cnt - train_cnt

    # 训练集划分
    with open(train_split_txt, 'w') as f:
        for item in all_list[0:train_cnt]:
            filename_number = item.split('.')[0].split('_')[1]

            shutil.copyfile(os.path.join(data_root, img_dir, f'img_{filename_number}.jpeg'),
                            os.path.join(merge_root, train_dir,img_dir, f'{filename_number}.jpg'))

            shutil.copyfile(os.path.join(data_root, ann_dir, f'seg_{filename_number}.png'),
                            os.path.join(merge_root, train_dir, ann_dir, f'{filename_number}.png'))

            f.writelines(f"{filename_number}\n")

    # 测试集、验证集划分
    with open(val_split_txt, 'w') as f:
        for item in all_list[train_cnt:]:
            filename_number = item.split('.')[0].split('_')[1]

            shutil.copyfile(os.path.join(data_root, img_dir, f'img_{filename_number}.jpeg'),
                            os.path.join(merge_root, val_dir, img_dir, f'{filename_number}.jpg'))

            shutil.copyfile(os.path.join(data_root, ann_dir, f'seg_{filename_number}.png'),
                            os.path.join(merge_root, val_dir, ann_dir, f'{filename_number}.png'))

            f.writelines(f"{filename_number}\n")


if __name__ == '__main__':
    shuffle_and_splie()
