# OpenMMLab寒假训练营之MMDetection目标检测
## 环境说明  
<li>Anaconda 2021.05  
<li>Python3.8
<li>gcc 7.3
<li>Pytorch 1.10 
<li>cuda 11.1
<li>mmcv-full 1.7.0 
<li>mmdet  2.28.1  
<li>tensorboard  2.10  
<li>tensorboardX 2.2  
<li>opencv-python  4.5.1.48  
  

## 基础作业：气球检测
<li> 预训练模型 MaskRCNN 

<li> 训练日志、结果模型和整理好的数据集下载地址  
    链接: https://pan.baidu.com/s/1OTfnBPHLnLbWooxJJe3xLA 提取码: 4eik 
    
<li>可视化评估</li>  
 
<div align=center><img src="https://github.com/Brian417-cup/OpenMMLabCamp/blob/detection/balloon/visualize_and_predict/res/bbox_mAP.svg" alt="balloon_detection"/></div>   
<div align=center><h3> bbox_mAP可视化</h3></div><br> 

<div align=center><img src="https://github.com/Brian417-cup/OpenMMLabCamp/blob/detection/balloon/visualize_and_predict/res/segm_mAP.svg" alt="balloon_detection"/></div>  
<div align=center><h3> segm_mAP可视化</h3></div><br>  

<li>部分预测可视化  
<div align=center><img src="https://github.com/Brian417-cup/OpenMMLabCamp/blob/detection/balloon/visualize_and_predict/output_gray/combine_result.jpg" alt="balloon_detection"/></div>  
<div align=center><img src="https://github.com/Brian417-cup/OpenMMLabCamp/blob/detection/balloon/visualize_and_predict/res/balloon_gray.gif" alt="balloon_detection"/></div>  


##  进阶作业：VOC2007数据集目标检测
<li>说明  本次使用的数据集为VOC2007数据集的子类，仅包含如下类别的目标检测：鸟、猫、奶牛、狗、马、人、山羊  

<li>预训练模型  YOLOVX  

<li>训练日志、结果模型下载地址  
    链接: https://pan.baidu.com/s/1YziQ3lc0GqarRwHxMUWnQQ 提取码: tdni 

<li>VOC2007数据集下载地址  http://host.robots.ox.ac.uk/pascal/VOC/voc2007/index.html

<li>准确率可视化评估  
<div align=center><img src="https://github.com/Brian417-cup/OpenMMLabCamp/blob/detection/VOC2007_partial/visualize_and_predict/res/mAP.svg" alt="VOC2007_detection"/></div>   
<div align=center><h3> mAP可视化</h3></div><br> 

<div align=center><img src="https://github.com/Brian417-cup/OpenMMLabCamp/blob/detection/VOC2007_partial/visualize_and_predict/res/birdAP.svg" alt="VOC2007_detection"/></div>   
<div align=center><h3> bird_mAP可视化</h3></div><br> 

<div align=center><img src="https://github.com/Brian417-cup/OpenMMLabCamp/blob/detection/VOC2007_partial/visualize_and_predict/res/catAP.svg" alt="VOC2007_detection"/></div>   
<div align=center><h3> cat_mAP可视化</h3></div><br> 


<div align=center><img src="https://github.com/Brian417-cup/OpenMMLabCamp/blob/detection/VOC2007_partial/visualize_and_predict/res/cowAP.svg" alt="VOC2007_detection"/></div>   
<div align=center><h3> cow_mAP可视化</h3></div><br> 

<div align=center><img src="https://github.com/Brian417-cup/OpenMMLabCamp/blob/detection/VOC2007_partial/visualize_and_predict/res/dogAP.svg" alt="VOC2007_detection"/></div>   
<div align=center><h3> dog_mAP可视化</h3></div><br> 


<div align=center><img src="https://github.com/Brian417-cup/OpenMMLabCamp/blob/detection/VOC2007_partial/visualize_and_predict/res/horseAP.svg" alt="VOC2007_detection"/></div>   
<div align=center><h3> horse_mAP可视化</h3></div><br> 

<div align=center><img src="https://github.com/Brian417-cup/OpenMMLabCamp/blob/detection/VOC2007_partial/visualize_and_predict/res/personAP.svg" alt="VOC2007_detection"/></div>   
<div align=center><h3> person_mAP可视化</h3></div><br> 

<div align=center><img src="https://github.com/Brian417-cup/OpenMMLabCamp/blob/detection/VOC2007_partial/visualize_and_predict/res/sheepAP.svg" alt="VOC2007_detection"/></div>   
<div align=center><h3> sheep_mAP可视化</h3></div><br> 

<li>预测可视化  
<div align=center><img src="https://github.com/Brian417-cup/OpenMMLabCamp/blob/detection/VOC2007_partial/visualize_and_predict/combine_output/bird.jpg" alt="VOC2007_detection"/></div>  
<div align=center><img src="https://github.com/Brian417-cup/OpenMMLabCamp/blob/detection/VOC2007_partial/visualize_and_predict/combine_output/cat.jpg" alt="VOC2007_detection"/></div>  
<div align=center><img src="https://github.com/Brian417-cup/OpenMMLabCamp/blob/detection/VOC2007_partial/visualize_and_predict/combine_output/cow.jpg" alt="VOC2007_detection"/></div>  
<div align=center><img src="https://github.com/Brian417-cup/OpenMMLabCamp/blob/detection/VOC2007_partial/visualize_and_predict/combine_output/dog.jpg" alt="VOC2007_detection"/></div> 
<div align=center><img src="https://github.com/Brian417-cup/OpenMMLabCamp/blob/detection/VOC2007_partial/visualize_and_predict/combine_output/horse.jpg" alt="VOC2007_detection"/></div> 
<div align=center><img src="https://github.com/Brian417-cup/OpenMMLabCamp/blob/detection/VOC2007_partial/visualize_and_predict/combine_output/person.jpg" alt="VOC2007_detection"/></div> 
<div align=center><img src="https://github.com/Brian417-cup/OpenMMLabCamp/blob/detection/VOC2007_partial/visualize_and_predict/combine_output/sheep.jpg" alt="VOC2007_detection"/></div> 
