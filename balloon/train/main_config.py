# reference https://github.com/open-mmlab/mmdetection/tree/master/configs/mask_rcnn
# choose model X-101-64x4d-FPN

_base_ = './model/mask_rcnn_r50_caffe_fpn_mstrain-poly_2x_coco.py'

model = dict(
    roi_head=dict(
        # bbox and mask change
        bbox_head=dict(num_classes=1),
        mask_head=dict(num_classes=1)
    )
)

dataset_type = 'COCODataset'
classes = ('balloon',)
data = dict(
    # set batch_size and gpu nums
    samples_per_gpu=1,
    workers_per_gpu=2,
    train=dict(
        img_prefix='../balloon_dataset/train/',
        classes=classes,
        ann_file='../balloon_dataset/train/out.json'),
    val=dict(
        img_prefix='../balloon_dataset/val/',
        classes=classes,
        ann_file='../balloon_dataset/val/out.json'),
)

# optimizer setting
optimizer = dict(type='SGD', lr=0.001, momentum=0.9, weight_decay=0.0001)
optimizer_config = dict(grad_clip=None)

runner = dict(type='EpochBasedRunner', max_epochs=1000)

load_from = 'mask_rcnn.pth'
