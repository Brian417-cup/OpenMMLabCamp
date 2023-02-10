import os
import glob

ballon_dataset_base = os.path.join('..','balloon_dataset')
train_dataset_base = os.path.join(ballon_dataset_base, 'train')
val_dataset_base = os.path.join(ballon_dataset_base, 'val')
img_suffic = '*.jpg'


def rename_all_imgs(base_path: str):
    for i, item in enumerate(glob.glob(os.path.join(base_path, img_suffic))):
        os.rename(item, os.path.join(base_path,f'{i}.jpg'))
        # print(i)


if __name__ == '__main__':
    # rename_all_imgs(train_dataset_base)
    rename_all_imgs(val_dataset_base)
