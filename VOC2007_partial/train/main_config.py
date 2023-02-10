# The relative operation can be refered by
# https://www.shouxicto.com/article/661.html

_base_ = ['./mmdet/.mim/configs/yolox/yolox_s_8x8_300e_coco.py']

model = dict(
    type='YOLOX',
    bbox_head=dict(
        type='YOLOXHead', num_classes=7))

# Please write the complete path for the dataset
dataset_type = 'VOCDataset'
data_root = 'F:/dataset/VOC2007/'

train_dataset = dict(
    type='MultiImageMixDataset',
    dataset=dict(
        type=dataset_type,
        ann_file=data_root + 'ImageSets/Main/train.txt',
        img_prefix=data_root,
    ))

data = dict(
    # samples_per_gpu=1,
    samples_per_gpu=16,
    workers_per_gpu=4,
    persistent_workers=True,
    train=train_dataset,
    val=dict(
        type=dataset_type,
        ann_file=data_root + 'ImageSets/Main/val.txt',
        img_prefix=data_root, ),
    test=dict(
        type=dataset_type,
        ann_file=data_root + 'ImageSets/Main/train.txt',
        img_prefix=data_root, ))

evaluation = dict(
    save_best='auto',
    metric='mAP')

# update the log record
log_config = dict(interval=1)
# use the learning_rate for the single gpu
optimizer = dict(type='SGD', lr=0.001, momentum=0.9, weight_decay=5e-4)
optimizer_config = dict(grad_clip=None)

runner = dict(type='EpochBasedRunner', max_epochs=3000)

load_from = 'yolox_s.pth'
checkpoint_config = dict(interval=1)
# cfg.checkpoint_config.interval = 3
