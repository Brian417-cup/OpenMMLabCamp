# this config can be refered by
# https://blog.csdn.net/weixin_43624833/article/details/125180817
_base_ = [
    # './mmesgmentation/configs/_base_/models/deeplabv3plus_r50-d8.py',
    'D:/ancando3.4.2/installment2/envs/learn_mmpose/Lib/mmsegmentation/configs/_base_/models/deeplabv3plus_r50-d8.py',
    'D:/ancando3.4.2/installment2/envs/learn_mmpose/Lib/mmsegmentation/configs/_base_/datasets/pascal_voc12_aug.py',
    'D:/ancando3.4.2/installment2/envs/learn_mmpose/Lib/mmsegmentation/configs/_base_/default_runtime.py',
    'D:/ancando3.4.2/installment2/envs/learn_mmpose/Lib/mmsegmentation/configs/_base_/schedules/schedule_20k.py'
]
model = dict(
    type='EncoderDecoder',
    pretrained='resnet50.pth')

dataset_type = 'PascalVOCDataset'
data_root = 'F:/VOC2012'
img_norm_cfg = dict(
    mean=[123.675, 116.28, 103.53], std=[58.395, 57.12, 57.375], to_rgb=True)
crop_size = (512, 512)
train_pipeline = [
    dict(type='LoadImageFromFile'),
    dict(type='LoadAnnotations'),
    dict(type='Resize', img_scale=(2048, 512), ratio_range=(0.5, 2.0)),
    dict(type='RandomCrop', crop_size=crop_size, cat_max_ratio=0.75),
    dict(type='RandomFlip', prob=0.5),
    dict(type='PhotoMetricDistortion'),
    dict(type='Normalize', **img_norm_cfg),
    dict(type='Pad', size=crop_size, pad_val=0, seg_pad_val=255),
    dict(type='DefaultFormatBundle'),
    dict(type='Collect', keys=['img', 'gt_semantic_seg']),
]
test_pipeline = [
    dict(type='LoadImageFromFile'),
    dict(
        type='MultiScaleFlipAug',
        img_scale=(2048, 512),
        # img_ratios=[0.5, 0.75, 1.0, 1.25, 1.5, 1.75],
        flip=False,
        transforms=[
            dict(type='Resize', keep_ratio=True),
            dict(type='RandomFlip'),
            dict(type='Normalize', **img_norm_cfg),
            dict(type='ImageToTensor', keys=['img']),
            dict(type='Collect', keys=['img']),
        ])
]

data = dict(
    samples_per_gpu=2,
    workers_per_gpu=4,
    train=dict(
        type=dataset_type,
        data_root=data_root,
        img_dir='JPEGImages',
        ann_dir='SegmentationClass',
        split='ImageSets/Segmentation/train.txt',
        pipeline=train_pipeline),
    val=dict(
        type=dataset_type,
        data_root=data_root,
        img_dir='JPEGImages',
        ann_dir='SegmentationClass',
        split='ImageSets/Segmentation/val.txt',
        pipeline=test_pipeline),
    test=dict(
        type=dataset_type,
        data_root=data_root,
        img_dir='JPEGImages',
        ann_dir='SegmentationClass',
        split='ImageSets/Segmentation/val.txt',
        pipeline=test_pipeline)
)

runner = dict(type='IterBasedRunner', max_iters=20000)
checkpoint_config = dict(by_epoch=False, interval=5)
evaluation = dict(interval=1, metric='mIoU', pre_eval=True)
load_from = 'deeplbv3plus_pascal_voc.pth'
