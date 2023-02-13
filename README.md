# OpenMMLab寒假训练营之MMSegmentation图像分割
## 环境说明  
<li>Anaconda 2021.05  
<li>Python3.7
<li>gcc 7.3
<li>Pytorch 1.10 
<li>cuda 11.1
<li>mmcv-full 1.4.3 
<li>mmsegmentation  0.30.0  
<li>tensorboard  2.10  
<li>tensorboardX 2.2  
<li>opencv-python  4.5.1.48  
  

## 基础作业：针对VOC2012数据集的图像分割
<li>  说明：由于本次服务器资源的卡时有限，只选择了公交车、猫、人这三个子集作为训练分割的考察对象  

###  预训练模型 
    ResNet50 +  DeepLabV3Plus

### 训练日志、结果模型和整理好的数据集下载地址  
    链接: https://pan.baidu.com/s/1CHDcENFlmNuj3iTovWdWJw  
    提取码: si39 
    
###  结果可视化和部分指标分析  
<li>猫—— IoU ：84.25 ,  Acc ：87.55
<div align=center><img src="https://github.com/Brian417-cup/OpenMMLabCamp/blob/segmentation/voc_2012_seg/visualize_and_predict/combine_out/test1_combine.jpg" alt="voc2012_segmentation"/></div>  

<div align=center><img src="https://github.com/Brian417-cup/OpenMMLabCamp/blob/segmentation/voc_2012_seg/visualize_and_predict/combine_out/test2_combine.jpg" alt="voc2012_segmentation"/></div>  

<li>人—— IoU ：66.29 ,  Acc ：72.83
<div align=center><img src="https://github.com/Brian417-cup/OpenMMLabCamp/blob/segmentation/voc_2012_seg/visualize_and_predict/combine_out/test3_combine.jpg" alt="voc2012_segmentation"/></div>  

<div align=center><img src="https://github.com/Brian417-cup/OpenMMLabCamp/blob/segmentation/voc_2012_seg/visualize_and_predict/combine_out/test4_combine.jpg" alt="voc2012_segmentation"/></div>  

<li>巴士—— IoU ：0.65 ,  Acc ：75.46
<div align=center><img src="https://github.com/Brian417-cup/OpenMMLabCamp/blob/segmentation/voc_2012_seg/visualize_and_predict/combine_out/test5_combine.jpg" alt="voc2012_segmentation"/></div>  

<div align=center><img src="https://github.com/Brian417-cup/OpenMMLabCamp/blob/segmentation/voc_2012_seg/visualize_and_predict/combine_out/test6_combine.jpg"/></div>  

###  推理时间
  在Intel i5 CPU上推理,需4.28s/张
  
##  进阶作业：模特衣物分割(Kaggle的数据集重新整理)

<li>  说明：由于本次服务器资源的卡时有限，最终得到的模型并没有在所有给出的58个类别都有很好的分割效果    

###  预训练模型  ResNet50 + DeepLabV3Plus  

###  训练日志、结果模型和整理好的数据集下载地址  
    链接: https://pan.baidu.com/s/1BH6_1dRMH7oQpD7-iSGwJg 提取码: miqz 
    
###  Acc可视化展示  
<li>bag
<div align=center><img src="https://github.com/Brian417-cup/OpenMMLabCamp/blob/segmentation/clothe_seg/visualize_and_predict/res/______bag______.svg" alt="clothe_segmentation"/></div>  

<li>belt
<div align=center><img src="https://github.com/Brian417-cup/OpenMMLabCamp/blob/segmentation/clothe_seg/visualize_and_predict/res/______belt_____.svg" alt="clothe_segmentation"/></div>  

<li>coat
<div align=center><img src="https://github.com/Brian417-cup/OpenMMLabCamp/blob/segmentation/clothe_seg/visualize_and_predict/res/______coat_____.svg" alt="clothe_segmentation"/></div>  

<li>hair
<div align=center><img src="https://github.com/Brian417-cup/OpenMMLabCamp/blob/segmentation/clothe_seg/visualize_and_predict/res/______hair_____.svg" alt="clothe_segmentation"/></div>  

<li>hat
<div align=center><img src="https://github.com/Brian417-cup/OpenMMLabCamp/blob/segmentation/clothe_seg/visualize_and_predict/res/______hat______.svg" alt="clothe_segmentation"/></div>  

<li>dress
<div align=center><img src="https://github.com/Brian417-cup/OpenMMLabCamp/blob/segmentation/clothe_seg/visualize_and_predict/res/_____dress_____.svg" alt="clothe_segmentation"/></div>  


<li>dressshoes align=center><img src="https://github.com/Brian417-cup/OpenMMLabCamp/blob/segmentation/clothe_seg/visualize_and_predict/res/_____shoes_____.svg" alt="clothe_segmentation"/></div>  


###  推理时间
  在Intel i5 CPU上推理,需3.89s/张

###  部分预测可视化  
<div align=center><img src="https://github.com/Brian417-cup/OpenMMLabCamp/blob/segmentation/clothe_seg/visualize_and_predict/combine_out/test1_combine.jpg" alt="clothe_segmentation"/></div>  

<div align=center><img src="https://github.com/Brian417-cup/OpenMMLabCamp/blob/segmentation/clothe_seg/visualize_and_predict/combine_out/test2_combine.jpg" alt="clothe_segmentation"/></div>  

<div align=center><img src="https://github.com/Brian417-cup/OpenMMLabCamp/blob/segmentation/clothe_seg/visualize_and_predict/combine_out/test3_combine.jpg" alt="clothe_segmentation"/></div>  


<div align=center><img src="https://github.com/Brian417-cup/OpenMMLabCamp/blob/segmentation/clothe_seg/visualize_and_predict/combine_out/test4_combine.jpg" alt="clothe_segmentation"/></div>  


<div align=center><img src="https://github.com/Brian417-cup/OpenMMLabCamp/blob/segmentation/clothe_seg/visualize_and_predict/combine_out/test5_combine.jpg" alt="clothe_segmentation"/></div>  

