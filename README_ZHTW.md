# 資料轉換技術文件

## 概述
**資料轉換專案**提供了一組工具和腳本，用於促進深度學習應用中特別是圖像分割和目標檢測任務的數據格式轉換。此專案設計用於處理 Labelme、YOLO 和 Mask 圖像之間的格式轉換。

---

## 專案結構

### 目錄
- **datasets/**: 包含示例或使用者提供的各種格式的數據集。
- **docu/**: 文檔及相關資源。
- **function/**: 包含腳本使用的工具函數。
- **outputs/**: 存儲由腳本生成的輸出文件。
- **test/**: 用於驗證腳本功能的測試文件和示例數據。

### 關鍵文件
- **labelme2mask.py**: 將 Labelme 標註（JSON 格式）轉換為Mask圖像。
- **labelme2mask2.py**: `labelme2mask.py` 的擴展版本，具有更多功能。
- **labelme2yolov5.py**: 將 Labelme 標註轉換為 YOLOv5 格式。
- **labelme2yolov8.py**: 將 Labelme 標註轉換為 YOLOv8 格式。
- **mask2labelme.py**: 將Mask圖像轉換回 Labelme JSON 格式。
- **mask2yolo.py**: 將Mask圖像轉換為 YOLO 格式。
- **yolo2labelme.py**: 將 YOLO 標註轉換為 Labelme JSON 格式。
- **yolo2masks.py**: 將 YOLO 標註轉換為Mask圖像。
- **ydataset2images.py**: 從 YOLO 數據集中提取單個圖像。

### 依賴項
本專案使用的 Python 套件可以通過 `requirements.txt` 文件進行安裝：
```bash
pip install -r requirements.txt
```

---

## 功能描述

### 1. Labelme 到 Mask 轉換
**腳本:** `labelme2mask.py`

- **目的:** 將 Labelme JSON 標註轉換為二進制或彩色 Mask 圖像。
- **用法:**
  ```bash
  python labelme2mask.py --input_dir <path_to_labelme_jsons> --output_dir <path_to_output_masks>
  ```
- **參數:**
  - `--input_dir`: 包含 Labelme JSON 文件的目錄。
  - `--output_dir`: 保存Mask圖像的目錄。

### 2. Labelme 到 YOLO 格式轉換
**腳本:** `labelme2yolov5.py`, `labelme2yolov8.py`

- **目的:** 將 Labelme 標註轉換為 YOLO 格式，用於目標檢測任務。
- **用法:**
  ```bash
  python labelme2yolov5.py --input_dir <path_to_labelme_jsons> --output_dir <path_to_yolo_annotations>
  ```
- **參數:**
  - `--input_dir`: 包含 Labelme JSON 文件的目錄。
  - `--output_dir`: 保存 YOLO 標註文件的目錄。

### 3. Mask 到 Labelme 格式轉換
**腳本:** `mask2labelme.py`

- **目的:** 將Mask圖像轉換回 Labelme JSON 標註。
- **用法:**
  ```bash
  python mask2labelme.py --input_dir <path_to_masks> --output_dir <path_to_labelme_jsons>
  ```

### 4. YOLO 到Mask轉換
**腳本:** `yolo2masks.py`

- **目的:** 將 YOLO 標註轉換為Mask圖像，用於分割任務。
- **用法:**
  ```bash
  python yolo2masks.py --input_dir <path_to_yolo_annotations> --output_dir <path_to_masks>
  ```

### 5. YOLO 到 Labelme 格式轉換
**腳本:** `yolo2labelme.py`

- **目的:** 將 YOLO 標註轉換回 Labelme JSON 格式。
- **用法:**
  ```bash
  python yolo2labelme.py --input_dir <path_to_yolo_annotations> --output_dir <path_to_labelme_jsons>
  ```

### 6. YOLO 數據集提取
**腳本:** `ydataset2images.py`

- **目的:** 從 YOLO 數據集中提取單個圖像。
- **用法:**
  ```bash
  python ydataset2images.py --input_dir <path_to_yolo_dataset> --output_dir <path_to_images>
  ```

---

## 示例工作流程
1. **準備數據:**
   - 確保數據集為支持的格式（如 Labelme JSON、YOLO 標註或Mask圖像）。
   
2. **轉換流程:**
   - 使用 `labelme2mask.py` 將 Labelme 標註轉換為Mask。
   - 使用 `mask2yolo.py` 將Mask轉換為 YOLO 格式。
   - 可選地，使用 `yolo2labelme.py` 將 YOLO 標註轉回 Labelme JSON。

3. **輸出驗證:**
   - 檢查 `outputs/` 目錄中的生成文件。

---

## 貢獻指南
1. Fork 此倉庫並在本地克隆。
2. 為您的功能或錯誤修復創建新分支。
3. 提交帶有清晰信息的更改。
4. 提交拉取請求以供審查。

---

## 授權
此專案基於 MIT 許可證授權。詳情請參見 `LICENSE` 文件。

---

## 聯繫方式
如有問題或查詢，請在 [GitHub 倉庫](https://github.com/kancheng/data-conversion/issues) 中提交 issue。

