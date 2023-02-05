_base_ = ['./model/mobilenet_v2_1x.py',
          './model/imagenet_bs32_pil_resize.py',
          './model/imagenet_bs256_epochstep.py',
          './model/default_runtime.py'
          ]

model = dict(
    head=(dict(
        num_classes=2,
        topk=(1,)
    ))
)

data = dict(
    # 设置batch_size和workes数量
    samples_per_gpu=64,
    workers_per_gpu=16,
    # 训练集路径
    train=dict(
        ann_file='./cat_and_dog_dataset/train.txt',
        data_prefix='./cat_and_dog_dataset/train',
        classes='./cat_and_dog_dataset/classes.txt'
    ),
    # 验证集路径
    val=dict(
        ann_file='./cat_and_dog_dataset/val.txt',
        data_prefix='./cat_and_dog_dataset/val',
        classes='./cat_and_dog_dataset/classes.txt'
    ),
    # train_dataloader=dict(samples_per_gpu=4, workers_per_gpu=1,mode=None),
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

load_from = 'MobileNetV2.pth'
