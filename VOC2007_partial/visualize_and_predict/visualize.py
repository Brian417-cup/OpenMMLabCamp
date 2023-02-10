import os
import glob
from tensorboardX import SummaryWriter
import re

mAP_epoch_tag = 'Epoch(val) '
mAP_tag = 'mAP: '
log_path_base = os.path.join('logs')
log_file_name = os.path.join(log_path_base, 'train.log')

visualize_path_base = os.path.join('runs')

mAP_epoch_start = 10
mAP_epoch_evaluation_freq = 10


def visualize_mAP_with_tensorboard():
    writer = SummaryWriter(visualize_path_base)

    with open(log_file_name, 'r') as f:
        lines = f.readlines()
        epoch = mAP_epoch_start
        for index, line in enumerate(lines):
            if line.__contains__(mAP_epoch_tag):
                # print(index)
                mAP_digit_start_index = line.find(mAP_tag) + len(mAP_tag)
                mAP_digit_end_index = line.find(',', mAP_digit_start_index)
                mAP_value = float(line[mAP_digit_start_index:mAP_digit_end_index])
                print(mAP_value)
                epoch += mAP_epoch_evaluation_freq
                writer.add_scalar('mAP', mAP_value, epoch)

    writer.close()


bird_tag = '| bird   |'
cat_tag = '| cat    |'
cow_tag = '| cow    |'
dog_tag = '| dog    |'
horse_tag = '| horse  |'
person_tag = '| person |'
sheep_tag = '| sheep  |'


def visualize_AP_with_tensorbard(class_tag: str, offset: int):
    writer = SummaryWriter(visualize_path_base)
    with open(log_file_name, 'r') as f:
        lines = f.readlines()
        for index, line in enumerate(lines):
            if line.__contains__(class_tag):
                AP_value = line.split(' ')[-2]
                epoch_value = lines[index - 5 + offset].split(' ')[-2]

                print(epoch_value, AP_value)
                writer.add_scalar(f'{class_tag}_AP', float(AP_value), int(epoch_value))
    writer.close()


if __name__ == '__main__':
    visualize_mAP_with_tensorboard()
    # visualize_AP_with_tensorbard(bird_tag, 0)
    # visualize_AP_with_tensorbard(cat_tag, -1)
    # visualize_AP_with_tensorbard(cow_tag, -2)
    # visualize_AP_with_tensorbard(dog_tag, -3)
    # visualize_AP_with_tensorbard(horse_tag, -4)
    # visualize_AP_with_tensorbard(person_tag, -5)
    visualize_AP_with_tensorbard(sheep_tag, -6)
