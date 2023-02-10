from mmdet.apis import init_detector,inference_detector,show_result_pyplot
import mmcv
import os
import glob
import numpy
import cv2

config_base_path = os.path.join('config')
config_file = os.path.join(config_base_path, 'main_config.py')

checkpoint_base_path = os.path.join('checkpoint')
checkpoint_file = os.path.join(checkpoint_base_path, 'best_mAP_epoch_100.pth')

test_base_path = os.path.join('test')
test_output_base_path=os.path.join('test_output')

model = init_detector(config_file, checkpoint_file, device='cpu')

def predict_img_with_detection_frame(img_path:str,output_path:str):
    result=inference_detector(model,img_path)
    show_result_pyplot(model,
                       img_path,
                       result,
                       out_file=output_path)

def predict_imgs_with_detection_frame(test_base_path:str):
    for item in glob.glob(os.path.join(test_base_path,'*')):
        predict_img_with_detection_frame(item,
                                         os.path.join(test_output_base_path,os.path.basename(item)))

if __name__ == '__main__':
    predict_imgs_with_detection_frame(test_base_path)