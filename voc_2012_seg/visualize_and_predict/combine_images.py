import os
import glob
import cv2
import numpy as np

test_base_path = 'test_imgs'
test_out_base_path = 'test_out'
combine_out_base_path = 'combine_out'

target_w = 350
target_h = 256


def combine_with_test_and_result():
    for full_file_name in glob.glob(os.path.join(test_base_path, '*')):
        file_name = os.path.basename(full_file_name)
        predict_file_name = os.path.join(test_out_base_path, file_name)

        print(predict_file_name)

        test_img = cv2.imread(full_file_name)
        predict_img = cv2.imread(predict_file_name)

        test_img = cv2.resize(test_img, (target_w, target_h))
        predict_img = cv2.resize(predict_img, (target_w, target_h))

        combine_img = np.concatenate([test_img, predict_img], 1)
        cv2.imwrite(
            os.path.join(combine_out_base_path, f"{file_name.split('.')[0]}_combine.jpg"),
            combine_img)


if __name__ == '__main__':
    combine_with_test_and_result()
