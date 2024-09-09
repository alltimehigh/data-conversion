# data-conversion 数据转换文件

Data conversion for deep learning image segmentation models.
深度学习图像分割模型的数据转换

# Labelme2Masks.

## Command

```bash
python labelme2mask.py --input_dir="./datasets/labelme/dataset_name/" --output_dir="./outputs/dataset_name/"
```

# YOLO2Labelme

Tool to convert yolo format dataset to labelme json format.
将yolo格式数据集转换为labelme json格式的工具。

## Usage
Arguments:
参数

`data` : path to dataset directory
`data`：数据集目录路径

Keyword arguments:
关键参数

`out` : path to output directory. Default dataset is created at same path as data_dir with name labelmeDataset.
out`：输出目录路径。默认数据集与 data_dir 的路径相同，名称为 labelmeDataset。


`skip` : action to take if `.txt` file corresponding to image is not found.
`跳过`：如果未找到与图像对应的txt文件，则要采取的操作。
- `False` (default) raises `FileNotFoundError`.
- `错误`（默认）引发 `文件寻找错误`。
- `print` prints missing file path to stdout.
- `打印（显示要的数据）` 将缺失文件路径打印到 stdout。
- `True` or any other value skips file silently.
- 寻找文件正确或任何其他值都会静默跳过文件。

### CLI Usage:

Following command creates labelme json dataset directory at `path/to/labelme/dataset` from `path/to/yolo/dataset` dataset directory.
以下命令从“path/to/yolo/dataset”数据集目录转到“path/to/labelme/dataset”处创建 labelme json 数据集目录。
```bash
yolo2labelme path/to/yolo/dataset
```

Specify output directory, skip.
指定输出目录，跳过。

```bash
yolo2labelme path/to/yoloDataset --out path/to/labelmeJsonDir --skip print
```

# Labelme2YOLO

Help converting LabelMe Annotation Tool JSON format to YOLO text file format. 
帮助将 LabelMe 标注工具从JSON 格式转换为 YOLO 文本文件格式。
If you've already marked your segmentation dataset by LabelMe, it's easy to use this tool to help converting to YOLO format dataset.
如果您已经通过 LabelMe 标注了您的分割数据集，则可以轻松使用此工具帮助转换为 YOLO 格式的数据集。

## Parameters Explain ## 参数解释
**--json_dir** LabelMe JSON files folder path.
**--json_dir** LabelMe JSON 文件的文件夹路径。

**--val_size (Optional)** Validation dataset size, for example 0.2 means 20% for validation and 80% for training. Default value is 0.1 .
**--val_size（可选）** 验证数据集大小，例如 0.2 表示 20% 用于验证，80% 用于训练。默认值为 0.1。

**--json_name (Optional)** Convert single LabelMe JSON file.
**--json_name（可选）** 转换单个 LabelMe JSON 文件。

**--seg (Optional)** Convert to [YOLOv5 v7.0](https://github.com/ultralytics/yolov5/tree/v7.0#segmentation--new) instance segmentation dataset.
**--seg (可选)** 转换为 [YOLOv5 v7.0](https://github.com/ultralytics/yolov5/tree/v7.0#segmentation--new) 实例分割数据集。

## How to Use 如何使用

### 1. Convert JSON files, split training and validation dataset by --val_size
### 1. 转换 JSON 文件，通过 --val_size 分割训练和验证数据集

Put all LabelMe JSON files under **labelme_json_dir**, and run this python command.
将所有 LabelMe JSON 文件放在 **labelme_json_dir** 下，然后运行此 python 命令。

```bash
python labelme2yolo.py --json_dir /home/username/labelme_json_dir/ --val_size 0.2
```
Script would generate YOLO format dataset labels and images under different folders, for example,
脚本将在不同的文件夹下生成 YOLO 格式的数据集标签和图像，例如
```bash
# when specifying `--seg', "YOLODataset" will be "YOLODataset_seg"
/home/username/labelme_json_dir/YOLODataset/labels/train/
/home/username/labelme_json_dir/YOLODataset/labels/val/
/home/username/labelme_json_dir/YOLODataset/images/train/
/home/username/labelme_json_dir/YOLODataset/images/val/

/home/username/labelme_json_dir/YOLODataset/dataset.yaml
```

### 2. Convert JSON files, split training and validation dataset by folder  转换 JSON 文件，按文件夹拆分训练和验证数据集
转换 JSON 文件，按文件夹拆分训练和验证数据集

If you already split train dataset and validation dataset for LabelMe by yourself, please put these folder under labelme_json_dir, for example,
如果你已经自行拆分了 LabelMe 的训练数据集和验证数据集，请将这些文件夹放在 labelme_json_dir 下，例如，
```bash
/home/username/labelme_json_dir/train/
/home/username/labelme_json_dir/val/
```
Put all LabelMe JSON files under **labelme_json_dir**. 
将所有 LabelMe JSON 文件放在 **labelme_json_dir** 下。

Script would read train and validation dataset by folder.
脚本将按文件夹读取训练和验证数据集。

Run this python command.
运行此 python 命令。

```bash
python labelme2yolo.py --json_dir /home/username/labelme_json_dir/
```
Script would generate YOLO format dataset labels and images under different folders, for example,
脚本将在不同的文件夹下生成 YOLO 格式的数据集标签和图像，例如
```bash
# when specifying `--seg', "YOLODataset" will be "YOLODataset_seg"
/home/username/labelme_json_dir/YOLODataset/labels/train/
/home/username/labelme_json_dir/YOLODataset/labels/val/
/home/username/labelme_json_dir/YOLODataset/images/train/
/home/username/labelme_json_dir/YOLODataset/images/val/

/home/username/labelme_json_dir/YOLODataset/dataset.yaml
```

### 3. Convert single JSON file 转换单独JSON文件
Put LabelMe JSON file under **labelme_json_dir**. , and run this python command.
将 LabelMe JSON 文件放在 **labelme_json_dir** 下，然后运行此 python 命令。

```bash
python labelme2yolo.py --json_dir /home/username/labelme_json_dir/ --json_name 2.json
```
Script would generate YOLO format text label and image under **labelme_json_dir**, for example,
脚本会在labelme_json_dir下生成YOLO格式的文本标签和图片，例如：

```bash
/home/username/labelme_json_dir/2.text
/home/username/labelme_json_dir/2.png
```

##

Only tested on Centos 7/Python 3.6 and Ubuntu 20.04 LTS/Python 3.11.9 environment.
仅在 Centos 7/Python 3.6 和 Ubuntu 20.04 LTS/Python 3.11.9 环境上测试。
