from function.fmask2yolo import *
from function.fmask2labelme import *
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

def copy_mask_dataset(src="./datasets/mask/mask_dataset", dest="./outputs/default_data/dataset_masks"):
    if os.path.exists(src):
        shutil.copytree(src, dest, dirs_exist_ok=True)
        print(f"Contents of '{src}' copied to '{dest}'")
    else:
        print(f"Source directory '{src}' does not exist.")

if __name__ == "__main__":
    create_default_data_dirs()
    copy_mask_dataset()
    mask2yolo("./datasets/mask/mask_dataset", "./outputs/default_data/dataset_yolo")
    label_names = { 0: "object1", 1: "object2"}
    mask2labelme("./datasets/mask/mask_dataset", "./outputs/default_data/dataset_labelme", label_names)