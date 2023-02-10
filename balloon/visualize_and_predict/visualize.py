import os
import glob
from tensorboardX import SummaryWriter

# 针对训练的文件做可视化
# 日志路径
log_path = os.path.join('logs', 'train.log')
# 可视化路径
output_base_path = os.path.join('runs')

# 指标标识符
# 指标说明见: https://blog.csdn.net/qq_17457331/article/details/84590662
bbox_mAP_tag = 'bbox_mAP: '
bbox_mAP_50_tag = 'bbox_mAP_50: '
bbox_mAP_75_tag = 'bbox_mAP_75: '
bbox_mAP_s_tag = 'bbox_mAP_s: '
bbox_mAP_m_tag = 'bbox_mAP_m: '
bbox_mAP_l_tag = 'bbox_mAP_l: '
segm_mAP_tag = 'segm_mAP: '
segm_mAP_50_tag = 'segm_mAP_50: '
segm_mAP_75_tag = 'segm_mAP_75: '
segm_mAP_s_tag = 'segm_mAP_s: '
segm_mAP_m_tag = 'segm_mAP_m: '
segm_mAP_l_tag = 'segm_mAP_l: '

epoch_tag = 'Saving checkpoint at '


def visualize_by_log_with_tensorboard(value_tag: str):
    writer = SummaryWriter(output_base_path)

    with open(log_path, 'r') as f:
        log_lines = f.readlines()
        for i, line in enumerate(log_lines):
            if line.__contains__(epoch_tag):
                epoch = int(line.replace('\n', '').split(' ')[-2])
                print(epoch)

                if epoch == 1:
                    continue

                last_line = log_lines[i - 1]
                start_index = last_line.find(value_tag) + len(value_tag)
                end_index = last_line.find(',', start_index)
                # print(start_index,end_index)
                value = last_line[start_index:end_index]
                print(value)

                writer.add_scalar(value_tag[:-2], float(value), epoch)

    writer.close()


if __name__ == '__main__':
    visualize_by_log_with_tensorboard(value_tag=bbox_mAP_tag)
    # visualize_by_log_with_tensorboard(value_tag=bbox_mAP_50_tag)
    # visualize_by_log_with_tensorboard(value_tag=bbox_mAP_75_tag)
    # visualize_by_log_with_tensorboard(value_tag=bbox_mAP_s_tag)
    # visualize_by_log_with_tensorboard(value_tag=bbox_mAP_m_tag)
    # visualize_by_log_with_tensorboard(value_tag=bbox_mAP_l_tag)
    # visualize_by_log_with_tensorboard(value_tag=segm_mAP_50_tag)
    # visualize_by_log_with_tensorboard(value_tag=segm_mAP_75_tag)
    # visualize_by_log_with_tensorboard(value_tag=segm_mAP_s_tag)
    # visualize_by_log_with_tensorboard(value_tag=segm_mAP_m_tag)
    # visualize_by_log_with_tensorboard(value_tag=segm_mAP_l_tag)
    # visualize_by_log_with_tensorboard(value_tag=segm_mAP_tag)
