import glob
import os
import random
import shutil

dataset_name = 'flower_dataset'
dataset_name_after = 'flower_dataset_imagenet'

base_path = os.path.join('..', dataset_name)
divide_path = os.path.join('..', dataset_name_after)

train_percentage = 8 / (8 + 2)
val_percentage = 2 / (8 + 2)


# 将文件按照对应比例划分为训练集和测试集
def shuffle_and_divide(base_path: str, detail_sub_path: str, pattern_file_str: str):
    total_path_with_pattern = os.path.join(base_path, detail_sub_path, pattern_file_str)

    all_list = []

    for i, item in enumerate(glob.glob(total_path_with_pattern)):
        all_list.append(item)

    random.shuffle(all_list)

    file_cnts = len(all_list)

    train_file_list = all_list[:int(file_cnts * train_percentage) + 1]
    val_file_list = all_list[-int(file_cnts * val_percentage):]

    return train_file_list, val_file_list


# 将打乱好的训练集和测试集放到对应的文件夹目录中
def copy_file_with_train_and_val_respectively(target_base_path: str,sub_path:str,
                                              train_dir: str, val_dir: str,
                                              train_list: list, val_list: list):
    base_path = os.path.join(target_base_path)
    # 训练集目录创建
    target_train_path = os.path.join(base_path, train_dir,sub_path)
    if os.path.exists(target_train_path) == False:
        os.makedirs(target_train_path)



    for i, item in enumerate(train_list):
        shutil.copy(item, target_train_path)

    # 验证集目录创建
    target_val_path = os.path.join(base_path, val_dir,sub_path)
    if os.path.exists(target_val_path) == False:
        os.makedirs(target_val_path)

    for i, item in enumerate(val_list):
        shutil.copy(item, target_val_path)


if __name__ == '__main__':
    # flower_name='rose'
    # flower_name='daisy'
    flower_name='dandelion'
    # flower_name='sunflower'
    # flower_name='tulip'

    train_list, val_list = shuffle_and_divide(base_path, flower_name, '*.jpg')

    copy_file_with_train_and_val_respectively(target_base_path=divide_path, sub_path=flower_name,
                                              train_dir='train', val_dir='val',
                                              train_list=train_list, val_list=val_list)
