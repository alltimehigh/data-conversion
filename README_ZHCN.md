# 数据转换技术文件

## 概述
**数据转换项目**提供了一组工具和脚本，用于促进深度学习应用中尤其是图像分割和目标检测任务的数据格式转换。此项目设计用于处理 Labelme、YOLO 和掩码图像之间的格式转换。

---

## 项目结构

### 目录
- **datasets/**: 包含示例或用户提供的各种格式的数据集。
- **docu/**: 文档及相关资源。
- **function/**: 包含脚本使用的工具函数。
- **outputs/**: 存储由脚本生成的输出文件。
- **test/**: 用于验证脚本功能的测试文件和示例数据。

### 关键文件
- **labelme2mask.py**: 将 Labelme 标注（JSON 格式）转换为掩码图像。
- **labelme2mask2.py**: `labelme2mask.py` 的扩展版本，具有更多功能。
- **labelme2yolov5.py**: 将 Labelme 标注转换为 YOLOv5 格式。
- **labelme2yolov8.py**: 将 Labelme 标注转换为 YOLOv8 格式。
- **mask2labelme.py**: 将掩码图像转换回 Labelme JSON 格式。
- **mask2yolo.py**: 将掩码图像转换为 YOLO 格式。
- **yolo2labelme.py**: 将 YOLO 标注转换为 Labelme JSON 格式。
- **yolo2masks.py**: 将 YOLO 标注转换为掩码图像。
- **ydataset2images.py**: 从 YOLO 数据集中提取单个图像。

### 依赖项
本项目使用的 Python 库可以通过 `requirements.txt` 文件进行安装：
```bash
pip install -r requirements.txt
```

---

## 功能描述

### 1. Labelme 到掩码转换
**脚本:** `labelme2mask.py`

- **目的:** 将 Labelme JSON 标注转换为二进制或彩色掩码图像。
- **用法:**
  ```bash
  python labelme2mask.py --input_dir <path_to_labelme_jsons> --output_dir <path_to_output_masks>
  ```
- **参数:**
  - `--input_dir`: 包含 Labelme JSON 文件的目录。
  - `--output_dir`: 保存掩码图像的目录。

### 2. Labelme 到 YOLO 格式转换
**脚本:** `labelme2yolov5.py`, `labelme2yolov8.py`

- **目的:** 将 Labelme 标注转换为 YOLO 格式，用于目标检测任务。
- **用法:**
  ```bash
  python labelme2yolov5.py --input_dir <path_to_labelme_jsons> --output_dir <path_to_yolo_annotations>
  ```
- **参数:**
  - `--input_dir`: 包含 Labelme JSON 文件的目录。
  - `--output_dir`: 保存 YOLO 标注文件的目录。

### 3. 掩码到 Labelme 格式转换
**脚本:** `mask2labelme.py`

- **目的:** 将掩码图像转换回 Labelme JSON 标注。
- **用法:**
  ```bash
  python mask2labelme.py --input_dir <path_to_masks> --output_dir <path_to_labelme_jsons>
  ```

### 4. YOLO 到掩码转换
**脚本:** `yolo2masks.py`

- **目的:** 将 YOLO 标注转换为掩码图像，用于分割任务。
- **用法:**
  ```bash
  python yolo2masks.py --input_dir <path_to_yolo_annotations> --output_dir <path_to_masks>
  ```

### 5. YOLO 到 Labelme 格式转换
**脚本:** `yolo2labelme.py`

- **目的:** 将 YOLO 标注转换回 Labelme JSON 格式。
- **用法:**
  ```bash
  python yolo2labelme.py --input_dir <path_to_yolo_annotations> --output_dir <path_to_labelme_jsons>
  ```

### 6. YOLO 数据集提取
**脚本:** `ydataset2images.py`

- **目的:** 从 YOLO 数据集中提取单个图像。
- **用法:**
  ```bash
  python ydataset2images.py --input_dir <path_to_yolo_dataset> --output_dir <path_to_images>
  ```

---

## 示例工作流程
1. **准备数据:**
   - 确保数据集为支持的格式（如 Labelme JSON、YOLO 标注或掩码图像）。
   
2. **转换流程:**
   - 使用 `labelme2mask.py` 将 Labelme 标注转换为掩码。
   - 使用 `mask2yolo.py` 将掩码转换为 YOLO 格式。
   - 可选地，使用 `yolo2labelme.py` 将 YOLO 标注转回 Labelme JSON。

3. **输出验证:**
   - 检查 `outputs/` 目录中的生成文件。

---

## 贡献指南
1. Fork 此仓库并在本地克隆。
2. 为您的功能或错误修复创建新分支。
3. 提交带有清晰信息的更改。
4. 提交拉取请求以供审查。

---

## 授权
此项目基于 MIT 许可证授权。详情请参见 `LICENSE` 文件。

---

## 联系方式
如有问题或查询，请在 [GitHub 仓库](https://github.com/kancheng/data-conversion/issues) 中提交 issue。

