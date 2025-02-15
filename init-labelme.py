from function.flabelme2yolov8 import *
from function.flabelme2mask2 import *

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

def copy_labelme_dataset(src="./datasets/labelme/labelme_dataset", dest="./outputs/default_data/dataset_labelme"):
    if os.path.exists(src):
        shutil.copytree(src, dest, dirs_exist_ok=True)
        print(f"Contents of '{src}' copied to '{dest}'")
    else:
        print(f"Source directory '{src}' does not exist.")

if __name__ == "__main__":
    create_default_data_dirs()
    copy_labelme_dataset()
    lme2yolov8("./datasets/labelme/labelme_dataset/", seg=True, val_size=0.2, json_name=None, other_path="../../../outputs/default_data/dataset_yolo/")
    lme2mask2("./datasets/labelme/labelme_dataset", "./outputs/default_data/dataset_masks/")
