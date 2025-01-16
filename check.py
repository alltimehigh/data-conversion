import os

def is_labelme_format(root_dir):
    """判斷是否是 LabelMe 格式"""
    for subdir in os.listdir(root_dir):
        sub_path = os.path.join(root_dir, subdir)
        if os.path.isdir(sub_path) and 'labelme' in subdir.lower():
            return True
    return False

def is_mask_format(root_dir):
    """判斷是否是 Mask 格式"""
    mask_path = os.path.join(root_dir, 'mask')
    if not os.path.exists(mask_path) or not os.path.isdir(mask_path):
        return False

    for subdir in os.listdir(mask_path):
        sub_path = os.path.join(mask_path, subdir)
        if os.path.isdir(sub_path):
            images_found, masks_found = False, False
            for inner_dir in os.listdir(sub_path):
                if 'images' in inner_dir.lower():
                    images_found = True
                if 'masks' in inner_dir.lower():
                    masks_found = True
            if images_found and masks_found:
                return True

    return False

def is_yolo_format(root_dir):
    """判斷是否是 YOLO 格式"""
    yolo_path = os.path.join(root_dir, 'yolo')
    if not os.path.exists(yolo_path) or not os.path.isdir(yolo_path):
        return False

    for subdir in os.listdir(yolo_path):
        sub_path = os.path.join(yolo_path, subdir)
        if os.path.isdir(sub_path):
            images_path = os.path.join(sub_path, 'images')
            labels_path = os.path.join(sub_path, 'labels')
            if os.path.exists(images_path) and os.path.exists(labels_path):
                images_train = os.path.join(images_path, 'train')
                images_val = os.path.join(images_path, 'val')
                labels_train = os.path.join(labels_path, 'train')
                labels_val = os.path.join(labels_path, 'val')
                return all(os.path.exists(path) for path in [images_train, images_val, labels_train, labels_val])

    return False

def detect_dataset_format(root_dir):
    """檢測數據集格式"""
    formats = []

    if is_labelme_format(root_dir):
        formats.append("LabelMe")
    if is_mask_format(root_dir):
        formats.append("Mask")
    if is_yolo_format(root_dir):
        formats.append("YOLO")

    return formats

# 示例用法
root_dir = "./datasets"  # 替換為您的根目錄
formats_detected = detect_dataset_format(root_dir)

if formats_detected:
    print(f"檢測到的數據格式: {', '.join(formats_detected)}")
else:
    print("未檢測到已知的數據格式")
