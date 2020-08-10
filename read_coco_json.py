import json

fileName = "C:/Users/vinay.DESKTOP-KPCO653.000/Downloads/train_annotations.coco.json"

with open(fileName, 'r') as f:
    coco = json.load(f)

print('JSON Keys:', coco.keys())
