from mmdet.apis import init_detector, inference_detector
import os
import numpy as np
import torch
import cv2
import glob

config_base_path = os.path.join('config')
config_file = os.path.join(config_base_path, 'main_config.py')

checkpoint_base_path = os.path.join('checkpoint')
checkpoint_file = os.path.join(checkpoint_base_path, 'epoch_final.pth')

test_base_path = os.path.join('test')

model = init_detector(config_file, checkpoint_file, device='cpu')

output_save_base_path = os.path.join('test_output')


def predict_img_mask(img_path: str):
    result = inference_detector(model, img_path)
    mask_out = result[1]

    mask_out = np.array(mask_out)
    h, w = mask_out.shape[2], mask_out.shape[3]

    single_mask = np.empty((1, h, w))
    np.sum(mask_out, 1, dtype=np.uint8, out=single_mask)

    single_mask = torch.tensor(single_mask > 0.5, dtype=torch.uint8) \
                      .view(h, w, 1).numpy() * 255
    cv2.imwrite(os.path.join(output_save_base_path, f'{os.path.basename(img_path)}'), single_mask)


def predict_img_mask_with_gray(img_path: str):
    result = inference_detector(model, img_path)
    mask_out = result[1]

    mask_out = np.array(mask_out)
    h, w = mask_out.shape[2], mask_out.shape[3]

    single_mask = np.empty((1, h, w))
    np.sum(mask_out, 1, dtype=np.uint8, out=single_mask)

    # 0~1的掩码
    single_mask = torch.tensor(single_mask > 0.5, dtype=torch.uint8) \
        .permute(1,2,0).numpy()
    # cv2.imwrite(os.path.join(output_save_path,f'{os.path.basename(img_path)}'), single_mask)

    # 原图数据
    img_data = cv2.imread(img_path)
    img_data = cv2.cvtColor(img_data, cv2.COLOR_BGR2RGB) / 255
    img_data_gray = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE) / 255

    img_data_gray = torch.tensor(img_data_gray).view(h, w, 1).numpy()
    combine_output = single_mask * img_data + img_data_gray * (1 - single_mask)

    combine_output = combine_output.astype(np.float32) * 255
    combine_output = cv2.cvtColor(combine_output, cv2.COLOR_RGB2BGR)

    tmp=os.path.basename(img_path).split('.')

    cv2.imwrite(os.path.join(output_save_base_path, f'{tmp[0]}_special_gray.{tmp[1]}'), combine_output)


if __name__ == '__main__':
    for item in glob.glob(os.path.join(test_base_path,'*.jpeg')):
        predict_img_mask_with_gray(item)

    # predict_img_mask_with_gray(os.path.join(test_base_path, 'img_test1.jpeg'))
    # predict_img_mask_with_gray(os.path.join(test_base_path, 'img_test2.png'))
