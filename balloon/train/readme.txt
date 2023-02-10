1.Download the dataset named "balloon_dataset".Make it the same level as the current folder, "train".Just like this:
    -balloon
        -balloon_dataset(This is the target posisiton you have to put)
        -data_dealing
        -train
            ......
2.Download the pretrained model "mask_rcnn.pth" that pretrained.Then, put it at the current directory.
3.Download the pretrained model "resnet50_caffe.pth" that pretrained.Then, put it intuo the subdirectory named "model".
4.run the python in the command at the current directory:
    python train.py main_config.py --work-dir out_dir