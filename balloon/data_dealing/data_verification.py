# 验证参考
# https://zhuanlan.zhihu.com/p/431215846

import os
from pycocotools.coco import COCO

verify_data_path_base=os.path.join('..','balloon_dataset')
verify_train_data_path_base=os.path.join\
    (verify_data_path_base,'train')
verify_val_data_path_base=os.path.join\
    (verify_data_path_base,'val')

# json_file=os.path.join(verify_train_data_path_base,'out.json')
json_file=os.path.join(verify_val_data_path_base,'out.json')

balloon_category_id = 0

if __name__ == '__main__':
    coco = COCO(json_file)
    print(coco.getCatIds())
    print(coco.getAnnIds())
    print(coco.getImgIds())