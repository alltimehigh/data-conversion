# Data Conversion Technical Documentation

[繁中正體 - Traditional Chinese](https://github.com/kancheng/data-conversion/blob/main/README_ZHTW.md).
[简体中文 - Simplified Chinese](https://github.com/kancheng/data-conversion/blob/main/README_ZHCN.md).

## Overview
The **Data Conversion Project** provides a set of tools and scripts to facilitate the transformation of data formats commonly used in deep learning applications, particularly for image segmentation and object detection tasks. This project is designed to handle conversions between formats such as Labelme, YOLO, and mask images.

---

## Project Structure

### Directories
- **datasets/**: Contains sample or user-provided datasets in various formats.
- **docu/**: Documentation and related resources.
- **function/**: Contains utility functions used in the scripts.
- **outputs/**: Stores the output files generated by the scripts.
- **test/**: Test files and sample data for validating script functionality.

### Key Files
- **labelme2mask.py**: Converts Labelme annotations (JSON format) to mask images.
- **labelme2mask2.py**: An extended version of `labelme2mask.py` with additional functionality.
- **labelme2yolov5.py**: Converts Labelme annotations to YOLOv5 format.
- **labelme2yolov8.py**: Converts Labelme annotations to YOLOv8 format.
- **mask2labelme.py**: Converts mask images back to Labelme JSON format.
- **mask2yolo.py**: Converts mask images to YOLO format.
- **yolo2labelme.py**: Converts YOLO annotations to Labelme JSON format.
- **yolo2masks.py**: Converts YOLO annotations to mask images.
- **ydataset2images.py**: Extracts individual images from a YOLO dataset.

### Dependencies
The project uses Python libraries that can be installed using the `requirements.txt` file:
```bash
pip install -r requirements.txt
```

```bash
pip install -r requirements.txt -i https://mirrors.tuna.tsinghua.edu.cn/pypi/web/simple 
```

---

## Functional Descriptions

### 1. Labelme to Mask Conversion
**Script:** `labelme2mask.py`

- **Purpose:** Converts Labelme JSON annotations to binary or colored mask images.
- **Usage:**
  ```bash
  python labelme2mask.py --input_dir <path_to_labelme_jsons> --output_dir <path_to_output_masks>
  ```
- **Parameters:**
  - `--input_dir`: Directory containing Labelme JSON files.
  - `--output_dir`: Directory where mask images will be saved.

### 2. Labelme to YOLO Conversion
**Scripts:** `labelme2yolov5.py`, `labelme2yolov8.py`

- **Purpose:** Converts Labelme annotations to YOLO format for object detection tasks.
- **Usage:**
  ```bash
  python labelme2yolov5.py --input_dir <path_to_labelme_jsons> --output_dir <path_to_yolo_annotations>
  ```
- **Parameters:**
  - `--input_dir`: Directory containing Labelme JSON files.
  - `--output_dir`: Directory where YOLO annotation files will be saved.

### 3. Mask to Labelme Conversion
**Script:** `mask2labelme.py`

- **Purpose:** Converts mask images back to Labelme JSON annotations.
- **Usage:**
  ```bash
  python mask2labelme.py --input_dir <path_to_masks> --output_dir <path_to_labelme_jsons>
  ```

### 4. YOLO to Mask Conversion
**Script:** `yolo2masks.py`

- **Purpose:** Converts YOLO annotations to mask images for segmentation tasks.
- **Usage:**
  ```bash
  python yolo2masks.py --input_dir <path_to_yolo_annotations> --output_dir <path_to_masks>
  ```

### 5. YOLO to Labelme Conversion
**Script:** `yolo2labelme.py`

- **Purpose:** Converts YOLO annotations back to Labelme JSON format.
- **Usage:**
  ```bash
  python yolo2labelme.py --input_dir <path_to_yolo_annotations> --output_dir <path_to_labelme_jsons>
  ```

### 6. YOLO Dataset Extraction
**Script:** `ydataset2images.py`

- **Purpose:** Extracts individual images from a YOLO dataset.
- **Usage:**
  ```bash
  python ydataset2images.py --input_dir <path_to_yolo_dataset> --output_dir <path_to_images>
  ```

---

## Example Workflow
1. **Prepare Data:**
   - Ensure your dataset is in a supported format (e.g., Labelme JSON, YOLO annotations, or mask images).
   
2. **Conversion Process:**
   - Convert Labelme annotations to masks using `labelme2mask.py`.
   - Convert masks to YOLO format using `mask2yolo.py`.
   - Optionally, revert YOLO annotations to Labelme JSON using `yolo2labelme.py`.

3. **Output Verification:**
   - Check the `outputs/` directory for the generated files.

---

## Contribution Guidelines
1. Fork the repository and clone it locally.
2. Create a new branch for your feature or bug fix.
3. Commit your changes with clear messages.
4. Submit a pull request for review.

---

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## Contact
For issues or inquiries, please raise an issue on the [GitHub repository](https://github.com/kancheng/data-conversion/issues).

