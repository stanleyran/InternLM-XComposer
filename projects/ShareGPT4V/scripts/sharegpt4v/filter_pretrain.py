import sys, os, pdb
import json

sharegpt4v_conv_instruct_coco = '/export/share/datasets/vision/coco/images/train2017'
pretrain_json = '/export/share/shu_zhang/data/ShareGPT4V/share-captioner_coco_lcs_sam_1246k_1107.json'

data = json.load(open(pretrain_json, 'r'))
coco_list = []
for line in data:
    if 'coco/train2017' in line['image']:
        img_fullpath = os.path.join(sharegpt4v_conv_instruct_coco, os.path.basename(line['image']))
        if os.path.exists(img_fullpath):
            line['image'] = img_fullpath
            coco_list.append(line)

with open('/export/share/shu_zhang/data/ShareGPT4V/coco_only_pretrain.json', 'w') as fout:
    json.dump(coco_list , fout)  
