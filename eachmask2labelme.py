import cv2
import numpy as np
import json
import os
import base64
import matplotlib.pyplot as plt

def mask_to_labelme_with_base64_and_print(image_path, mask_path, label_names):
    """
    將 mask 影像轉換為 Labelme 格式的 JSON 檔案，並列印輪廓點資訊。
    
    Args:
        image_path (str): 原始影像路徑。
        mask_path (str): 輸入的 mask 影像路徑（單通道 PNG 或多通道影像）。
        label_names (dict): 標籤名稱與對應灰度值的字典，例如 {0: "background", 1: "object"}。
    """
    # 讀取 mask 影像（假設為單通道）
    mask = cv2.imread(mask_path, cv2.IMREAD_GRAYSCALE)
    # 讀取原始影像並轉換為 Base64 編碼
    with open(image_path, "rb") as img_file:
        image_base64 = base64.b64encode(img_file.read()).decode('utf-8')
    shapes = []
    # 對每個類別的灰度值進行輪廓提取
    for value, label in label_names.items():
        # 創建二值影像，僅保留當前類別的區域
        binary_mask = np.uint8(mask == value)
        
        contours, _ = cv2.findContours(binary_mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_TC89_KCOS)
        new_contours = contours[1:]  # 從索引 1 開始切片
        for contour in new_contours:
            # 將輪廓轉換為序列化的多邊形點列表
            points = contour.squeeze().tolist()
            if len(points) < 3:  # 跳過小於 3 個點的無效輪廓
                continue
            
            shapes.append({
                "label": label,
                "points": points,
                "group_id": None,
                "description": "",
                "shape_type": "polygon",
                "flags": {}
            })
            print("shapes" , shapes)
            # 列印輪廓點資訊
            print(f"Label: {label}")
            print("Points:")
            print(points)
            print("-" * 50)
    # 建立 Labelme JSON 格式的結構
    labelme_json = {
        "version": "5.2.1",
        "flags": {},
        "shapes": shapes,
        "imagePath": os.path.basename(image_path),
        "imageData": image_base64,
        "imageHeight": mask.shape[0],
        "imageWidth": mask.shape[1]
    }
    print(labelme_json)
    # 儲存為 JSON 檔案
    with open(output_json_path, 'w') as f:
        json.dump(labelme_json, f, indent=4)

    # 顯示測試用 mask 影像
    plt.imshow(mask, cmap='gray')
    plt.title("Test Mask")
    plt.colorbar(label="Class Label")
    plt.show()
# 範例使用
image_path = "./test/image_0.png"  # 原始影像路徑
mask_path = "./test/mask_0.png" # 輸入的 mask 影像路徑
output_json_path = "./outputs/image_0.json" # 輸出的 Labelme JSON 檔案路徑
# label_names = {0: "background", 1: "cat", 2: "dog"}  # 對應灰度值與標籤名稱
# label_names = {0: "background", 1: "lesion"}  # 對應灰度值與標籤名稱 定義類別與灰度值對應關係
label_names = {0: "object"}  # 對應灰度值與標籤名稱 定義類別與灰度值對應關係
mask_to_labelme_with_base64_and_print(image_path, mask_path, label_names)

