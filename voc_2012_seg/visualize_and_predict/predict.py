import os
import glob
import mmcv
from mmseg.apis import init_segmentor,show_result_pyplot,inference_segmentor
import numpy as np

test_base_path = 'test_imgs'
checkpoint_base_path = 'checkpoint'
config_path = os.path.join('config', 'main_config.py')
output_base_path = 'test_out'

model = \
    init_segmentor(config_path,
                   checkpoint=os.path.join(checkpoint_base_path, 'bus.pth'),
                   device='cpu')

def predict_and_show():
    for file_name in glob.glob(os.path.join(test_base_path, '*')):
        result = inference_segmentor(model, file_name)
        print(result)
        result = np.array(result)
        print(np.unique(result))
        print(np.array(result).shape)
        visualization = show_result_pyplot(model, file_name, result, opacity=0.9,
                                           out_file=os.path.join(output_base_path, f'{os.path.basename(file_name)}'))

if __name__ == '__main__':
    predict_and_show()