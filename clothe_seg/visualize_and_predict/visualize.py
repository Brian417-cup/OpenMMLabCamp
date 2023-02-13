import os
import glob
from tensorboardX import SummaryWriter

log_base_path = 'logs'
log_save_freq = 50
null_class_tag = '|     null    |'
bag_class_tag = '|     bag     |'
belt_class_tag = '|     belt    |'
dress_class_tag = '|    dress    |'
hair_class_tag = '|     hair    |'
hat_class_tag = '|     hat     |'
jeans_class_tag = '|    jeans    |'
coat_class_tag = '|     coat    |'
shoes_class_tag = '|    shoes    |'
skin_class_tag = '|     skin    |'
stocking_class_tag = '|  stockings  |'
output_save_base_path = 'runs'

all_classes_tag = [null_class_tag, bag_class_tag, belt_class_tag, dress_class_tag,
                   hair_class_tag, hat_class_tag, jeans_class_tag, coat_class_tag,
                   shoes_class_tag, skin_class_tag, stocking_class_tag]


def visualize_acc(class_tag: str):
    i = 1
    for log_file_name in glob.glob(os.path.join(log_base_path, '*.log')):
        with open(log_file_name, 'r') as f:
            print(log_file_name)
            lines = f.readlines()
            for line in lines:
                if line.__contains__(class_tag):
                    acc_value = line.split(' ')[-2]
                    epoch = i * log_save_freq
                    print(acc_value, epoch)

                    i = i + 1


def visualize_acc_from_all_classes(class_tag: str, writer):
    print(class_tag)
    i = 1
    for log_file_name in glob.glob(os.path.join(log_base_path, '*.log')):
        with open(log_file_name, 'r') as f:
            print(log_file_name)
            lines = f.readlines()
            for line in lines:
                if line.__contains__(class_tag):
                    acc_value = line.replace('\n', '').replace(' ', '').split('|')[-2]
                    acc_value = float(acc_value) if acc_value != 'nan' else 0.0

                    epoch = i * log_save_freq
                    # print(acc_value, epoch)
                    # print(class_tag.split(' ')[2])
                    writer.add_scalar(class_tag, acc_value, epoch)
                    i = i + 1


if __name__ == '__main__':
    writer=SummaryWriter(output_save_base_path)
    for class_flag in all_classes_tag:
        visualize_acc_from_all_classes(class_flag,writer)