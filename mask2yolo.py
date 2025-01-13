


import copy
import cv2
import os
import shutil
import numpy as np

def eachmask2yolo(path, save_path, procshow=False):
    files = os.listdir(path)
    for file in files:
        name = file.split('.')[0]
        file_path = os.path.join(path,name+'.png')
        img = cv2.imread(file_path)
        H,W=img.shape[0:2]
        print(H,W)

        gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        ret,bin_img = cv2.threshold(gray_img,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
        cnt,hit = cv2.findContours(bin_img,cv2.RETR_TREE,cv2.CHAIN_APPROX_TC89_KCOS)

        cnt = list(cnt)
        f = open(save_path+"/{}.txt".format(file.split(".")[0]), "a+")
        for j in cnt:
            result = []
            pre = j[0]
            for i in j:
                if abs(i[0][0] - pre[0][0]) > 1 or abs(i[0][1] - pre[0][1]) > 1: # 在这里可以调整间隔点，我设置为 1
                    pre = i
                    temp = list(i[0])
                    temp[0] /= W
                    temp[1] /= H
                    result.append(temp)

                    if procshow:
                        cv2.circle(img,i[0],1,(0,0,255),2)

            print(result)
            print(len(result))

            # if len(result) != 0:

            if len(result) != 0:
                f.write("0 ")
                for line in result:
                    line = str(line)[1:-2].replace(",","")
                    # print(line)
                    f.write(line+" ")
                f.write("\n")
        f.close()

        if procshow:
            cv2.imshow("test",img)
            while True:
                key = cv2.waitKey(1)  # 等待 1 毫秒，返回键盘按键的 ASCII 值
                if key == ord('q'):  # 如果按下 'q' 键，退出循环
                    break
            
            cv2.destroyAllWindows()  # 关闭窗口

def convert_unet_to_yolo(input_dir, output_dir):
    os.makedirs(os.path.join(output_dir, "images/train"), exist_ok=True)
    os.makedirs(os.path.join(output_dir, "images/val"), exist_ok=True)
    os.makedirs(os.path.join(output_dir, "labels/train"), exist_ok=True)
    os.makedirs(os.path.join(output_dir, "labels/val"), exist_ok=True)

    for split in ["train", "val"]:
        image_src_dir = os.path.join(input_dir, split, "images")
        mask_src_dir = os.path.join(input_dir, split, "masks")
        image_dst_dir = os.path.join(output_dir, "images", split)
        label_dst_dir = os.path.join(output_dir, "labels", split)
        
        # Copy images to YOLO structure
        for img_file in os.listdir(image_src_dir):
            shutil.copy(os.path.join(image_src_dir, img_file), image_dst_dir)
        
        # Convert masks to YOLO labels
        eachmask2yolo(mask_src_dir, label_dst_dir)
    
    # Create dataset.yaml
    dataset_yaml_content = f"""
    train: {os.path.join(output_dir, 'images/train')}
    val: {os.path.join(output_dir, 'images/val')}

    nc: 1
    names: ['object']
    """
    with open(os.path.join(output_dir, "dataset.yaml"), "w") as yaml_file:
        yaml_file.write(dataset_yaml_content)

# Example usage
input_directory = "./datasets/mask/isic2018"
# /unet_dataset
output_directory = "./outputs/yolo_dataset"
convert_unet_to_yolo(input_directory, output_directory)