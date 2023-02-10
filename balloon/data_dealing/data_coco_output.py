import os
import glob
import cv2
import json

# COCO数据集目标检测和实例分割数据集检测可以参考
# https://blog.csdn.net/sun1221__/article/details/127546605

img_list = []

img = {
    'id': 0,
    'width': 0,
    'height': 0,
    'file_name': 'test.jpg',
    'license': 'null',
    'flickr_url': 'null',
    'data_captured': 'null'
}

annotation_list = []

annotation = {
    # int 图片中每个被标记物体的id编号
    'id': 0,
    # int 该物体所在图片的编号
    'image_id': 0,
    # int 被标记物体的类别id编号
    'category_id': 0,
    # width*height
    'area': 0.0,
    # 目标检测的属性
    # [x, y, width, height]  x, y代表的是物体的左上角的x, y的坐标值
    'bbox': [0, 0, 15, 15],
    # 实例分割检测属性
    # 例: "segmentation": [[200.0, 416.0, 264.0, 416.0, 264.0, 480.0, 200.0, 480.0]]
    # 这里表示(x,y)一对一对的
    # 'segmentation': 'RLE',
    'segmentation': [[]],
    'iscrowd': 0
}

category_list = []

balloon_category_id = 0

category = {
    'id': balloon_category_id,
    'name': 'balloon',
    'supercategory': 'null'
}

category_list.append(category)

# COCO总的数据结构
coco_data_struct = {
    'info': 'COCO Data Output',
    'images': img_list,
    'annotations': annotation_list,
    'categories': category_list
}

balloon_dataset_base = os.path.join('..', 'balloon_dataset')
balloon_train_dataset_base = os.path.join(balloon_dataset_base, 'train')
balloon_val_dataset_base = os.path.join(balloon_dataset_base, 'val')
target_json_name = 'via_region_data.json'


# 原始的待转换数据集中包含如下几项
# fileref 图片参考
# size 图片大小
# filename 文件名
# base64_img_data  base64的编码
# file_attributes 文件属性
# regions:{
# 这个下面可以有多个对象组成
#     {
#         shape_attributes 形状属性 :{
#             name : 形状名称,
#             all_points_x 所有的x坐标: [],
#             all_points_y  所有的y坐标: [],
#             region_attributes 区域属性(这次用不到): {}
#         },
#
#     }
# }
def convert_json_to_coco_json(base_path: str, json_path: str):
    with open(json_path, 'r') as f:
        target_dict = json.load(f)

        for target_id, key in enumerate(target_dict):
            # print(item)
            item = target_dict[key]

            # -------------------------------------------------------
            # 图片属性设置
            img_copy = img.copy()
            img_copy['id'] = int(target_id)
            print(item['filename'])
            img_copy['file_name'] = item['filename']
            img_data = cv2.imread(os.path.join(base_path, item['filename']))
            img_copy['width'] = img_data.shape[1]
            img_copy['height'] = img_data.shape[0]

            # ---------------------------------------------------------
            # 标注属性设置
            annotation_copy = annotation.copy()
            # 因为这里是实例分割，所以一个气球会有很多的区域，那么id号都编号为一个即可
            # annotation_copy['id'] = balloon_category_id
            annotation_copy['id'] = int(target_id)
            annotation_copy['image_id']=img_copy['id']
            annotation_copy['category_id']=balloon_category_id
            annotation_copy['area'] = img_data.shape[0] * img_data.shape[1]
            annotation_copy['bbox'] = [0, 0, img_data.shape[1], img_data.shape[0]]

            regions = item['regions']

            # 所有分割区域的分割边遍历
            for region_key in regions:
                x_list = regions[region_key]['shape_attributes']['all_points_x']
                y_list = regions[region_key]['shape_attributes']['all_points_y']
                # 重组成COCO支持的(x,y)一对的格式
                merge_list = []
                merge_list.clear()
                for i in range(len(x_list)):
                    x = x_list[i]
                    y = y_list[i]

                    merge_list.append(x)
                    merge_list.append(y)

                annotation_copy['segmentation'].clear()
                annotation_copy['segmentation'].append(merge_list)

            img_list.append(img_copy)
            annotation_list.append(annotation_copy)

        print(coco_data_struct['categories'])

    with open(f"{os.path.join(base_path,'out.json')}",'w') as f:
        json.dump(coco_data_struct,f)



if __name__ == '__main__':
    convert_json_to_coco_json(balloon_train_dataset_base,
                              os.path.join(balloon_train_dataset_base, target_json_name))

    # convert_json_to_coco_json(balloon_val_dataset_base,
    #                           os.path.join(balloon_val_dataset_base, target_json_name))
