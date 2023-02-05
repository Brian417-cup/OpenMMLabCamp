import os
# 使用tensorboardX要把tensorboard也装上
from tensorboardX import SummaryWriter

log_path = os.path.join('train.log')

epoch_flag = 'Saving checkpoint'
accuracy_flag = 'accuracy_top-1'
accuracy_str = 'Accuracy'
visual_output_path = os.path.join('logs')


def accuracy_visualize():
    epoc_list = []
    writer = SummaryWriter(logdir=visual_output_path)
    with open(log_path, 'r') as f:
        all_lines = f.readlines()
        for i, line in enumerate(all_lines):
            if line.__contains__(epoch_flag):
                epoch_int = int(line.split(' ')[-2])
                epoc_list.append({'epoch': epoch_int, 'line_index': i})

        for item in epoc_list:
            line_index = item['line_index']
            epoch_int = item['epoch']
            accuracy_value = all_lines[line_index + 1].replace('\n', '').split(' ')[-1]
            accuracy_value = float(accuracy_value)
            print(accuracy_value)

            writer.add_scalar(accuracy_str, accuracy_value, epoch_int)

        writer.close()


if __name__ == '__main__':
    accuracy_visualize()
