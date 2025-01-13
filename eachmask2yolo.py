import copy
import cv2
import os
import shutil
import numpy as np


path = "./test/masks"
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
    f = open("{}.txt".format(file.split(".")[0]), "a+")
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

                # cv2.circle(img,i[0],1,(0,0,255),2)

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

    # cv2.imshow("test",img)
    # while True:
    #     key = cv2.waitKey(1)  # 等待 1 毫秒，返回键盘按键的 ASCII 值
    #     if key == ord('q'):  # 如果按下 'q' 键，退出循环
    #         break
    
    # cv2.destroyAllWindows()  # 关闭窗口

