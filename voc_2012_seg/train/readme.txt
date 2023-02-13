1.Download the dataset named "VOC2012".Put it to a target directory.In the cureent directory, there is a file named "main_config.py", please write the complete path in the line 13 that aims to set the value for variable "data_root".
2.Download the pretrained model "resnet50.pth" and deeplbv3plus_pascal_voc.pth that pretrained.Then, put it as the direct subfolder of the "train" folder.
3.run the python in the command at the current directory:
    python train.py main_config.py --work-dir out_dir