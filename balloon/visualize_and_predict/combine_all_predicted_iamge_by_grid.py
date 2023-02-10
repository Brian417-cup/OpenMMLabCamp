import os
import glob
import cv2
import numpy as np
import torch

img_combine_out_path = 'test_output'
total_img_cnt = 4
target_w = 300
target_h = 224
out_name = 'combine_result.jpg'
h_grid_cnt = 2
v_grid_cnt = 2


def combine_to_a_line_horizontal():
    out_tensor = []
    for i, img_name in enumerate(glob.glob(os.path.join(img_combine_out_path, '*.jpeg'))):
        img = cv2.imread(img_name)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img = cv2.resize(img, (target_w, target_h))
        out_tensor.append(img)

    out_tensor = np.array(out_tensor)


    out_tensor1 = np.concatenate((out_tensor[0], out_tensor[1]), 1)
    out_tensor2 = np.concatenate((out_tensor[2], out_tensor[3]), 1)
    out_tensor=np.concatenate((out_tensor1,out_tensor2),0)
    # print(out_tensor.shape)
    # out_tensor = out_tensor.reshape((target_h, total_img_cnt * target_w, 3))
    # out_tensor = out_tensor.reshape((total_img_cnt * target_h, target_w, 3))
    out_tensor = cv2.cvtColor(out_tensor, cv2.COLOR_RGB2BGR)
    cv2.imwrite(os.path.join(img_combine_out_path, out_name), out_tensor)


if __name__ == '__main__':
    combine_to_a_line_horizontal()
