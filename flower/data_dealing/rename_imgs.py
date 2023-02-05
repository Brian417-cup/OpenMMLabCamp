import os
import glob

dataset_name = 'flower_dataset'

base_path = os.path.join('..', dataset_name)

# 对对应目录下的文件进行有规律的命名
def rename_img_file(base_dir: str, detail_sub_path: str, pattern_file_str: str):
    total_path_with_pattern = os.path.join(base_dir, detail_sub_path, pattern_file_str)
    base_path=os.path.join(base_dir,detail_sub_path)
    print(total_path_with_pattern)

    for i, item in enumerate(glob.glob(total_path_with_pattern)):
        before_name=item
        file_name_with_suffix=os.path.basename(item)
        file_suffix=file_name_with_suffix.split('.')[1]
        file_name=file_name_with_suffix.split('.')[0]
        after_name=detail_sub_path+'_'+str(i+1)+'.'+file_suffix
        os.rename(before_name,os.path.join(base_path,after_name))


if __name__ == '__main__':
    # rose目录下
    # rename_img_file(base_path, 'rose', '*.jpg')
    # daisy目录下
    # rename_img_file(base_path, 'daisy', '*.jpg')
    # sunflow目录下
    # rename_img_file(base_path, 'sunflower', '*.jpg')
    # dandelion目录下
    # rename_img_file(base_path, 'dandelion', '*.jpg')
    # tulip目录下
    rename_img_file(base_path, 'tulip', '*.jpg')