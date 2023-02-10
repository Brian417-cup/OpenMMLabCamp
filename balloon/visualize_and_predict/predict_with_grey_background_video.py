from mmdet.apis import init_detector, inference_detector
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
# model = init_detector(config_file, checkpoint_file, device='cuda:0')

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
        .view(h, w, 1).numpy()
    # cv2.imwrite(os.path.join(output_save_path,f'{os.path.basename(img_path)}'), single_mask)

    # 原图数据
    img_data = cv2.imread(img_path)
    img_data = cv2.cvtColor(img_data, cv2.COLOR_BGR2RGB) / 255
    img_data_gray = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE) / 255

    img_data_gray = torch.tensor(img_data_gray).view(h, w, 1).numpy()
    combine_output = single_mask * img_data + img_data_gray * (1 - single_mask)

    # combine_output=combine_output*255
    return combine_output


def predict_video_mask_with_gray(video_path: str, save_path: str):
    video_reader = cv2.VideoCapture(video_path)

    frame_num = int(video_reader.get(cv2.CAP_PROP_FRAME_COUNT))
    frame_width = int(video_reader.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(video_reader.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = int(video_reader.get(cv2.CAP_PROP_FPS))
    # 针对mp4格式的制作
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    video_writer = cv2.VideoWriter(save_path, fourcc, fps, (frame_width, frame_height))

    print(f'总帧数为{frame_num}')

    cur_frame_cnt = 0

    while cur_frame_cnt < frame_num:
        ret_result, frame_init_data = video_reader.read()
        if ret_result == False:
            print('返回不成功')
            break

        if frame_init_data is None:
            print('内容为空')
            continue

        # cv2.imshow('title',frame_init_data)
        # # 推理得到掩码
        result = inference_detector(model, frame_init_data)
        mask_out = result[1]

        mask_out = np.array(mask_out)
        h, w = mask_out.shape[2], mask_out.shape[3]

        single_mask = np.empty((1, h, w))
        np.sum(mask_out, 1, dtype=np.uint8, out=single_mask)

        # 0~1的掩码
        single_mask = torch.tensor(single_mask > 0.5, dtype=torch.uint8) \
            .view(h, w, 1).numpy()
        # # ------------------------------------------------
        h, w = frame_init_data.shape[0], frame_init_data.shape[1]

        frame_init_data = cv2.cvtColor(frame_init_data, cv2.COLOR_BGR2RGB)
        frame_foreground = frame_init_data.copy() / 255
        frame_background = cv2.cvtColor(frame_init_data.copy(), cv2.COLOR_RGB2GRAY)

        # cv2.imwrite(os.path.join(output_save_base_path,'test.jpg'),frame_background)
        # break

        frame_background = torch.tensor(frame_background) \
            .view(h, w, 1).numpy()/255

        combine_frame = single_mask * frame_foreground + frame_background * (1 - single_mask)
        combine_frame = combine_frame.astype(np.float32) * 255
        combine_frame = cv2.cvtColor(combine_frame, cv2.COLOR_RGB2BGR)
        combine_frame = combine_frame.astype(np.uint8)

        video_writer.write(combine_frame)

        # cv2.imshow('gray', combine_frame)
        # print('ok')
        cur_frame_cnt = cur_frame_cnt + 1
        print(cur_frame_cnt)


if __name__ == '__main__':
    predict_video_mask_with_gray(os.path.join(test_base_path, 'test_video.mp4'),
                                 save_path=os.path.join(output_save_base_path, 'test_out.mp4'))
