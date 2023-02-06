import glob
import cv2
import os
import numpy as np

img_combine_out_path = 'predict_img_combine'
total_img_cnt = 10
target_w = 300
target_h = 224
out_name = 'combine_result.jpg'


def combine_to_a_line():
    out_tensor = []
    for i, img_name in enumerate(glob.glob(os.path.join(img_combine_out_path, '*'))):
        img = cv2.imread(img_name)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img = cv2.resize(img, (target_w, target_h))
        out_tensor.append(img)

    out_tensor = np.array(out_tensor)
    out_tensor = out_tensor.reshape((total_img_cnt * target_h, target_w, 3))
    out_tensor = cv2.cvtColor(out_tensor, cv2.COLOR_RGB2BGR)
    cv2.imwrite(os.path.join(img_combine_out_path, out_name), out_tensor)


if __name__ == '__main__':
    combine_to_a_line()
