# data-conversion-test

Data conversion for deep learning image segmentation models.
深度學習影像分割模型的資料轉換

# Labelme2Masks.

## Command

```bash
python labelme2mask.py --input_dir="./datasets/labelme/dataset_name/" --output_dir="./outputs/dataset_name/"
```

# YOLO2Labelme

Tool to convert yolo format dataset to labelme json format.
將yolo格式資料集轉換為labelme json格式的工具。

## Usage
Arguments:
參數

`data` : path to dataset directory
`data` : 資料集目錄的路徑

Keyword arguments:
關鍵字參數：

`out` : path to output directory. Default dataset is created at same path as data_dir with name labelmeDataset.
`out` ：輸出目錄的路徑。預設資料集在與 data_dir 相同的路徑下創建，名稱為 labelmeDataset。

`skip` : action to take if `.txt` file corresponding to image is not found.
`skip` ：如果未找到與影像對應的 `.txt` 文件，則採取的動作。

- `False` (default) raises `FileNotFoundError`.
- “False”（預設）引發“FileNotFoundError”。

- `print` prints missing file path to stdout.
- `print` 將遺失的檔案路徑印到標準輸出。

- `True` or any other value skips file silently.
- `True` 或任何其他值都會靜默跳過檔案。

### CLI Usage:

Following command creates labelme json dataset directory at `path/to/labelme/dataset` from `path/to/yolo/dataset` dataset directory.
以下命令從「path/to/yolo/dataset」資料集目錄到「path/to/labelme/dataset」建立 labelme json 資料集目錄。
```bash
yolo2labelme path/to/yolo/dataset
```

Specify output directory, skip.
指定輸出目錄，跳過。

```bash
yolo2labelme path/to/yoloDataset --out path/to/labelmeJsonDir --skip print
```

# Labelme2YOLO

Help converting LabelMe Annotation Tool JSON format to YOLO text file format. 
協助將 LabelMe Annotation Tool JSON 格式轉換為 YOLO 文字檔案格式。

If you've already marked your segmentation dataset by LabelMe, it's easy to use this tool to help converting to YOLO format dataset.
如果您已經透過 LabelMe 標記了分割資料集，則可以輕鬆使用此工具來協助轉換為 YOLO 格式資​​料集。

## Parameters Explain  參數解釋
**--json_dir** LabelMe JSON files folder path.
**--json_dir** LabelMe JSON 檔案資料夾路徑。

**--val_size (Optional)** Validation dataset size, for example 0.2 means 20% for validation and 80% for training. Default value is 0.1 .
**--val_size （可選）** 驗證資料集大小，例如 0.2 表示 20% 用於驗證，80% 用於訓練。預設值為 0.1 。

**--json_name (Optional)** Convert single LabelMe JSON file.
**--json_name （可選）** 轉換單一 LabelMe JSON 檔案。

**--seg (Optional)** Convert to [YOLOv5 v7.0](https://github.com/ultralytics/yolov5/tree/v7.0#segmentation--new) instance segmentation dataset.
**--seg （可選）** 轉換為 [YOLOv5 v7.0](https://github.com/ultralytics/yolov5/tree/v7.0#segmentation--new) 實例分割資料集。

## How to Use 如何使用

### 1. Convert JSON files, split training and validation dataset by --val_size  轉換JSON文件，透過--val_size分割訓練和驗證資料集

Put all LabelMe JSON files under **labelme_json_dir**, and run this python command.
將所有 LabelMe JSON 檔案放在 **labelme_json_dir** 下，然後執行此 python 命令。

```bash
python labelme2yolo.py --json_dir /home/username/labelme_json_dir/ --val_size 0.2
```
Script would generate YOLO format dataset labels and images under different folders, for example,
腳本會在不同的資料夾下產生YOLO格式的資料集標籤和圖像，例如，
```bash
# when specifying `--seg', "YOLODataset" will be "YOLODataset_seg"
/home/username/labelme_json_dir/YOLODataset/labels/train/
/home/username/labelme_json_dir/YOLODataset/labels/val/
/home/username/labelme_json_dir/YOLODataset/images/train/
/home/username/labelme_json_dir/YOLODataset/images/val/

/home/username/labelme_json_dir/YOLODataset/dataset.yaml
```

### 2. Convert JSON files, split training and validation dataset by folder 轉換 JSON 文件，按資料夾拆分訓練和驗證資料集

If you already split train dataset and validation dataset for LabelMe by yourself, please put these folder under labelme_json_dir, for example,
如果您已經為LabelMe自行拆分了訓練資料集和驗證資料集，請將這些資料夾放在labelme_json_dir下，例如：

```bash
/home/username/labelme_json_dir/train/
/home/username/labelme_json_dir/val/
```
Put all LabelMe JSON files under **labelme_json_dir**. 
將所有 LabelMe JSON 檔案放在 **labelme_json_dir** 下。

Script would read train and validation dataset by folder.
腳本將按資料夾讀取訓練和驗證資料集。

Run this python command.
運行這個 python 命令。
```bash
python labelme2yolo.py --json_dir /home/username/labelme_json_dir/
```
Script would generate YOLO format dataset labels and images under different folders, for example,
腳本會在不同的資料夾下產生YOLO格式的資料集標籤和圖像，例如，
```bash
# when specifying `--seg', "YOLODataset" will be "YOLODataset_seg"
/home/username/labelme_json_dir/YOLODataset/labels/train/
/home/username/labelme_json_dir/YOLODataset/labels/val/
/home/username/labelme_json_dir/YOLODataset/images/train/
/home/username/labelme_json_dir/YOLODataset/images/val/

/home/username/labelme_json_dir/YOLODataset/dataset.yaml
```

### 3. Convert single JSON file 轉換單一 JSON 文件

Put LabelMe JSON file under **labelme_json_dir**. , and run this python command.
將 LabelMe JSON 檔案放在 **labelme_json_dir** 下。 ，然後執行這個 python 指令。
```bash
python labelme2yolo.py --json_dir /home/username/labelme_json_dir/ --json_name 2.json
```
Script would generate YOLO format text label and image under **labelme_json_dir**, for example,
腳本會在 **labelme_json_dir** 下產生 YOLO 格式的文字標籤和圖像，例如，
```bash
/home/username/labelme_json_dir/2.text
/home/username/labelme_json_dir/2.png
```

##

Only tested on Centos 7/Python 3.6 and Ubuntu 20.04 LTS/Python 3.11.9 environment.
僅在 Centos 7/Python 3.6 和 Ubuntu 20.04 LTS/Python 3.11.9 環境上進行測試。
