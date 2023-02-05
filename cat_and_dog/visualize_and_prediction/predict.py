from mmcls.apis import inference_model, init_model, show_result_pyplot
import os
import glob
from tensorboardX import SummaryWriter
import cv2
import numpy as np

device = 'cpu'
img_file_base = 'test_data'
checkpoint_base = 'checkpoint'
config_base = 'config'
img_path = os.path.join(img_file_base, 'test1.jpeg')
checkpoit_path = os.path.join(checkpoint_base, 'final_epoch_43.pth')
config_path = os.path.join(config_base, 'main_config.py')

tensorboard_out_path = 'logs'

# 模型初始化
model = init_model(config=config_path,
                   checkpoint=checkpoit_path,
                   device='cpu')

prediction_tag = 'Prediction'


def predict():
    for item in glob.glob(os.path.join(img_file_base, '*')):
        # 结果推理
        result = inference_model(model, item)
        print(f'{item}  {result}')
        # 可视化
        # 原生openmmlab的方法
        # show_result_pyplot(model, item, result)


def predict_with_tensorboard():
    writer = SummaryWriter(tensorboard_out_path)
    for i, item in enumerate(glob.glob(os.path.join(img_file_base, '*'))):
        # 结果推理
        result = inference_model(model, item)
        print(f'{item}  {result}')

        pred_class = result['pred_class']
        pred_score = result['pred_score']

        img = cv2.imread(item)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        font = cv2.FONT_HERSHEY_COMPLEX
        color = (0, 0, 0)
        predict_text = f'{pred_class}  {pred_score}'
        img = cv2.putText(img, predict_text, (0, 200), font, 1, color, 3)

        # 用tensorboard可视化
        writer.add_images(f'{prediction_tag}{i}', img_tensor=np.array(img), dataformats='HWC')
        # 可视化
        # 原生openmmlab的方法
        # show_result_pyplot(model, item, result)
    writer.close()


if __name__ == '__main__':
    predict_with_tensorboard()
