import os
import glob

base_dir = 'flower_dataset_imagenet'
train_dir = 'train'
val_dir = 'val'

train_path_base = os.path.join('..', base_dir, train_dir)
train_txt_path = os.path.join('..', base_dir, 'train.txt')

val_path_base = os.path.join('..', base_dir, val_dir)
val_txt_path = os.path.join('..', base_dir, 'val.txt')


def get_combine_txt_from_all_classes(base_path: str, file_pattern: str, out_txt_path: str):
    detailed_sub_dirs = glob.glob(os.path.join(base_path, '*'))
    with open(out_txt_path, 'w') as f:
        # base目录打开
        for class_index, dir in enumerate(detailed_sub_dirs):
            cur_dir = dir.split(os.path.sep)[-1]
            print(cur_dir)
            # 遍历各个目录中的文件
            for file_name in glob.glob(os.path.join(dir, file_pattern)):
                input_file_name = os.path.join(cur_dir, os.path.basename(file_name))

                # 这里文件分隔符要换一下，统一为'/'
                input_file_name = input_file_name.replace(os.path.sep, '/')

                f.writelines(input_file_name + ' ' + str(class_index) + '\n')


if __name__ == '__main__':
    get_combine_txt_from_all_classes(base_path=train_path_base, file_pattern='*.jpg',
                                     out_txt_path=train_txt_path)

    get_combine_txt_from_all_classes(base_path=val_path_base, file_pattern='*.jpg',
                                     out_txt_path=val_txt_path)
