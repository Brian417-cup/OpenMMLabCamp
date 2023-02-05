
_base_ = ['resnet50.py', 'imagenet_bs32.py',
          'default_runtime.py']

model = dict(
    head=(dict(
        num_classes=5,
        topk=(1,)
    ))
)

data = dict(
    # 设置batch_size和workes数量
    samples_per_gpu=32,
    workers_per_gpu=2,
    # # 训练集路径
    # train=dict(
    #     ann_file=os.path.join(os.path.join('..', 'flower_dataset_imagenet'), 'train.txt'),
    #     data_prefix=os.path.join(os.path.join('..', 'flower_dataset_imagenet'), 'train'),
    #     classes=os.path.join(os.path.join('..', 'flower_dataset_imagenet'), 'classes.txt')
    # ),
    # # 验证集路径
    # val=dict(
    #     ann_file=os.path.join(os.path.join('..', 'flower_dataset_imagenet'), 'val.txt'),
    #     data_prefix=os.path.join(os.path.join('..', 'flower_dataset_imagenet'), 'val'),
    #     classes=os.path.join(os.path.join('..', 'flower_dataset_imagenet'), 'classes.txt')
    # ),
    
# 训练集路径
    train=dict(
        ann_file='./flower_dataset_imagenet/train.txt',
        data_prefix='./flower_dataset_imagenet/train',
        classes='./flower_dataset_imagenet/classes.txt'
    ),
    # 验证集路径
    val=dict(
        ann_file='./flower_dataset_imagenet/val.txt',
        data_prefix='./flower_dataset_imagenet/val',
        classes='./flower_dataset_imagenet/classes.txt'
    ),
)

# 定义评估方式
evaluation = dict(metric_options={'topk': (1,)})

# 优化器
optimizer = dict(type='SGD', lr=0.001, momentum=0.9, weight_decay=0.0001)
optimizer_config = dict(grad_clip=None)

# 学习率策略
lr_config = dict(
    policy='step',
    step=[1]
)

runner = dict(type='EpochBasedRunner', max_epochs=1000)

load_from = 'resnet50.pth'
