import os
import glob

dataset_base = os.path.join('cat_and_dog_dataset')
train_dataset_base = os.path.join(dataset_base, 'train')
val_dataset_base = os.path.join(dataset_base, 'val')
animal_list = ['cat', 'dog']
label_list = [0, 1]


# 将目标文件和对应的标签做合并，最后导出成妈妈classification支持的格式
def combine_txt_out(base_path: str,
                    sub_path_list: list, label_list: list,
                    txt_out_path: str):
    with open(txt_out_path, 'w') as f:
        for i, sub_path in enumerate(sub_path_list):
            total_path = os.path.join(base_path, sub_path, '*')
            label = label_list[i]
            for img in glob.glob(total_path):
                img_name = os.path.basename(img)
                input_path = os.path.join(sub_path, img_name) \
                    .replace(os.path.sep, '/')
                f.writelines(input_path + ' ' + str(label) + '\n')


if __name__ == '__main__':
    # 训练集导出
    combine_txt_out(base_path=train_dataset_base,
                    sub_path_list=animal_list, label_list=label_list,
                    txt_out_path=os.path.join(dataset_base, 'train.txt'))

    # 验证集导出
    combine_txt_out(base_path=val_dataset_base,
                    sub_path_list=animal_list, label_list=label_list,
                    txt_out_path=os.path.join(dataset_base, 'val.txt'))
