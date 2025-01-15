from function.fyolo2labelme import *
from function.fyolo2masks import *


# Reference : https://github.com/kadapallaNithin/yolo2labelme/blob/main/yolo2labelme.py
# EX : 
# python yolo2labelme.py --input_dir="./datasets/yolo/yolo_dataset/" --out="./outputs/default_data/dataset_labelme"
# python yolo2masks.py --txt="./datasets/yolo/yolo_dataset/labels"  --img="./datasets/yolo/yolo_dataset/images" --out="./outputs/default_data/dataset_masks"
import os

def create_default_data_dirs(base_path="./outputs/default_data"):
    dirs = [
        os.path.join(base_path, "dataset_labelme"),
        os.path.join(base_path, "dataset_masks"),
        os.path.join(base_path, "dataset_yolo")
    ]

    for directory in dirs:
        os.makedirs(directory, exist_ok=True)
        print(f"Directory created: {directory}")

def copy_yolo_dataset(src="./datasets/yolo/yolo_dataset", dest="./outputs/default_data/dataset_yolo"):
    if os.path.exists(src):
        shutil.copytree(src, dest, dirs_exist_ok=True)
        print(f"Contents of '{src}' copied to '{dest}'")
    else:
        print(f"Source directory '{src}' does not exist.")
if __name__ == "__main__":
    create_default_data_dirs()
    copy_yolo_dataset()
    yolo2labelme("./datasets/yolo/yolo_dataset/", "./outputs/default_data/dataset_labelme")
    yolo2masks("./datasets/yolo/yolo_dataset/labels", "./datasets/yolo/yolo_dataset/images", "./outputs/default_data/dataset_masks")