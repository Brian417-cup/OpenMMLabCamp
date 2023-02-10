from mmdet.apis import init_detector, inference_detector
import mmcv
import os
import numpy as np
import torch
import cv2

config_base_path = os.path.join('config')
config_file = os.path.join(config_base_path, 'main_config.py')

checkpoint_base_path = os.path.join('checkpoint')
checkpoint_file = os.path.join(checkpoint_base_path, 'epoch_final.pth')

test_base_path = os.path.join('test')

model = init_detector(config_file, checkpoint_file, device='cpu')


def predict_img_mask(img_path: str):
    result = inference_detector(model, img_path)
    mask_out = result[1]

    mask_out = np.array(mask_out)

    h, w = mask_out.shape[2], mask_out.shape[3]

    single_mask = np.empty((1, h, w))
    np.sum(mask_out, 1, dtype=np.uint8, out=single_mask)

    single_mask = torch.tensor(single_mask > 0.5, dtype=torch.uint8) \
                      .view(h, w, 1).numpy() * 255

    cv2.imwrite('out.jpg', single_mask)


if __name__ == '__main__':
    predict_img_mask(os.path.join(test_base_path, 'img_test1.jpeg'))
    # predict_img(os.path.join(test_base_path, 'img_test2.png'))
