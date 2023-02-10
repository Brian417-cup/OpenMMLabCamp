import os
import glob
import cv2
import numpy as np

predict_base_path = os.path.join('test_output')
combine_out_base_path = os.path.join('combine_output')

target_h = 400
target_w = 600


def combine_by_predict_output_per_class(class_tag: str):
    i = 0
    print(class_tag)
    img1_data, img2_data = None, None
    for item in glob.glob(os.path.join(predict_base_path, '*')):
        if item.__contains__(class_tag):
            if img1_data is None:
                img1_data = cv2.imread(item)
                # cv2.imread(item,img1_data)
            elif img2_data is None:
                img2_data = cv2.imread(item)
                # cv2.imread(item,img2_data)
            else:
                break

    img1_data = cv2.resize(img1_data, (target_w, target_h))
    img2_data = cv2.resize(img2_data, (target_w, target_h))
    combine_data = np.concatenate((img1_data, img2_data), 1)
    cv2.imwrite(os.path.join(combine_out_base_path,
                             f'{class_tag}.jpg'),combine_data)


CLASSES = ('bird', 'cat', 'cow', 'dog', 'horse', 'person', 'sheep')


if __name__ == '__main__':
    for item in CLASSES:
        combine_by_predict_output_per_class(item)
