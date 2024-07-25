import cv2
import os, sys
import shutil
import random

# EX:
# input_folder =  "./datasets/ad/metalworking/"
# output_folder = "./outputs/ad/metalworking/"
# input_folder =  "./datasets/ad/mcl/"
# output_folder = "./outputs/ad/mcl/"
# python aidilabview2yoloseg.py --input_dir="./datasets/ad/metalworking/" --output_dir="./outputs/ad/metalworking/"
# python aidilabview2yoloseg.py --input_dir="./datasets/ad/mcl/" --output_dir="./outputs/ad/mcl/"

import argparse

parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument('--input_dir', help='input annotated directory')
parser.add_argument('--output_dir', help='output dataset directory')
args = parser.parse_args()

# args.input_dir
# input_folder =  "./datasets/ad/dataset_name/"
input_folder =  args.input_dir
# args.output_dir
# output_folder = "./outputs/ad/dataset_name/"
output_folder = args.output_dir

if not os.path.exists(input_folder):
    print("No data source.")
    print("沒有數據來源。")
    print("没有数据来源。")
    sys.exit(0)

if not os.path.exists(output_folder + "images/"):
    os.makedirs(output_folder + "images/train")
    os.makedirs(output_folder + "images/val")

if not os.path.exists(output_folder + "labels/"):
    os.makedirs(output_folder + "labels/train")
    os.makedirs(output_folder + "labels/val")
yaml_path = input_folder + "/dataset.yaml"
with open(yaml_path, "r") as f:
    yaml_data = f.read()

new_yaml_data = "path : " + input_folder + "\ntrain: images/train \nval: images/val \n" + yaml_data

def yaml(path, name, text): # Define function name
    xxoo = path + name + '.yaml' # Create a yaml file in the new file under the path of the current py file
    file = open(xxoo,'w')
    file.write(text) # Write content information
    file.close()
    print ('YAML OK!')
yaml(output_folder, 'dataset', new_yaml_data) # Create a yaml file named test with the content str !!

files = []
txtfs = []
files_check = []
txtfs_check = []
for filename in os.listdir(input_folder + "images/"):
    if filename.endswith((".png", ".jpg", ".jpeg", ".bmp")):
        files.append(filename) 
        for con in files:
            files_check.append(con.split(".")[0])

for filename in os.listdir(input_folder + "labels/"):
    if filename.endswith((".txt")):
        txtfs.append(filename)
        for con in txtfs:
            txtfs_check.append(con.split(".")[0])
intersection_files = []


# EX : H -> 315; W -> 700; Picture -> 315*700
# The point -> h = x1 = 35.576923076923094; w = y1 = 11.538461538461538
# YOLO point -> h = x1 = 35.576923076923094 / 315 = 0.112943;
#               w = y1 = 11.538461538461538 / 700 = 0.016484

if files_check == txtfs_check :
    print("The number of files is consistent with the number of txt.")
    print("Intersection File Number :", len(set(txtfs_check).intersection(set(files_check))))
    print("Intersection Files :", set(txtfs_check).intersection(set(files_check)))
    intersection_files = list(set(txtfs_check).intersection(set(files_check)))
    for con in intersection_files:
        tn = con + ".png"
        print("INFO. Checked ... ", input_folder + "images/" + tn , input_folder + "images/" + tn )
    print("Done!")
    print("Val Number : ",int(len(intersection_files) * 0.2))
    print("TRAIN Number : ",int(len(intersection_files) * 0.8))

    val_name = random.sample(intersection_files, int(len(intersection_files) * 0.2))
    print("Val Number Flies: ", val_name)
    train_name = list(set(intersection_files).difference(set(val_name)))
    print("Train Number Flies: ", train_name)
    for tn in val_name:
        tnfiles = tn + ".png"
        tntxts = tn + ".txt"
        shutil.copyfile(input_folder + "images/" + tnfiles, output_folder + "images/val/" + tnfiles)
        print("INFO. Copy ... ", input_folder + "images/" + tnfiles, "; ", output_folder + "images/val/" + tnfiles)

        # Read original image
        image = cv2.imread(input_folder + "images/" + tnfiles)
        h, w = image.shape[:2]
        # Read YOLO annotation file
        with open(input_folder + "labels/" + tntxts, 'r') as file:
            lines = file.readlines()
        temclear = ''
        temclearlist = []
        for line in lines:
            temclear = temclear + line
        temclearlist = temclear.split("\n")
        hdndata = []
        for line in range(len(temclearlist)):
            if len(temclearlist[line]) != 0:
                hdndata.append(temclearlist[line])
        hdspacetab = []
        alltemspacetabs = []
        for spacetabs in hdndata :
            temspacetabs = spacetabs.split("\t")
            for line in range(len(temspacetabs)):
                if len(temspacetabs[line]) != 0:
                    alltemspacetabs.append(temspacetabs[line])
            hdspacetab.append(alltemspacetabs)
        mathtoyolo = []
        dataobj = []
        datatag = []
        finaldatalist = []
        for mm in hdspacetab:
            datatag = mm[0]
            dataobj = mm[1:]
            for i in range(len(dataobj)):
                if  i % 2 != 0:
                    dataobj[i] = format(float(dataobj[i])/w, '.6f')
                if i % 2 == 0:
                    dataobj[i] = format(float(dataobj[i])/h, '.6f')
            dataobj.insert(0,datatag)
            str = " ".join(dataobj)
            finaldatalist.append(str)
        contextstr = "\n".join(finaldatalist)
        with open( output_folder + "labels/val/" + tntxts ,'w') as f:
            f.write(contextstr)
        print("INFO. Convert ... ", input_folder + "labels/" + tntxts, "; ", output_folder + "labels/val/" + tntxts)
    for tn in train_name:
        tnfiles = tn + ".png"
        tntxts = tn + ".txt"
        shutil.copyfile(input_folder + "images/" + tnfiles, output_folder + "images/train/" + tnfiles)
        print("INFO. Copy ... ", input_folder + "images/" + tnfiles, "; ", output_folder + "images/train/" + tnfiles)

        # Read original image
        image = cv2.imread(input_folder + "images/" + tnfiles)
        h, w = image.shape[:2]
        # Read YOLO annotation file
        with open(input_folder + "labels/" + tntxts, 'r') as file:
            lines = file.readlines()
        temclear = ''
        temclearlist = []
        for line in lines:
            temclear = temclear + line
        temclearlist = temclear.split("\n")
        hdndata = []
        for line in range(len(temclearlist)):
            if len(temclearlist[line]) != 0:
                hdndata.append(temclearlist[line])
        hdspacetab = []
        alltemspacetabs = []
        for spacetabs in hdndata :
            temspacetabs = spacetabs.split("\t")
            for line in range(len(temspacetabs)):
                if len(temspacetabs[line]) != 0:
                    alltemspacetabs.append(temspacetabs[line])
            hdspacetab.append(alltemspacetabs)
        mathtoyolo = []
        dataobj = []
        datatag = []
        finaldatalist = []
        for mm in hdspacetab:
            datatag = mm[0]
            dataobj = mm[1:]
            for i in range(len(dataobj)):
                if  i % 2 != 0:
                    dataobj[i] = format(float(dataobj[i])/w, '.6f')
                if i % 2 == 0:
                    dataobj[i] = format(float(dataobj[i])/h, '.6f')
            dataobj.insert(0,datatag)
            str = " ".join(dataobj)
            finaldatalist.append(str)
        contextstr = "\n".join(finaldatalist)
        with open( output_folder + "labels/train/" + tntxts ,'w') as f:
            f.write(contextstr)
        print("INFO. Convert ... ", input_folder + "labels/" + tntxts, "; ", output_folder + "labels/train/" + tntxts)


else :
    print("The number of files and the number of txt are inconsistent. \n ...")
    if not os.path.exists(input_folder + "images/clear"):
        os.makedirs(input_folder + "images/clear")
    print("Intersection File Number :", len(set(txtfs_check).intersection(set(files_check))))
    print("Intersection Files :", set(txtfs_check).intersection(set(files_check)))
    intersection_files = list(set(txtfs_check).intersection(set(files_check)))
    for con in intersection_files:
        tn = con + ".png"
        print("INFO. Copy ... ", input_folder + "images/" + tn , input_folder + "images/clear/" + tn )
        shutil.copyfile(input_folder + "images/" + tn , input_folder + "images/clear/" + tn)
    print("Done!")
    print("Val Number : ",int(len(intersection_files) * 0.2))
    print("TRAIN Number : ",int(len(intersection_files) * 0.8))

    val_name = random.sample(intersection_files, int(len(intersection_files) * 0.2))
    print("Val Number Flies: ", val_name)
    train_name = list(set(intersection_files).difference(set(val_name)))
    print("Train Number Flies: ", train_name)
    for tn in val_name:
        tnfiles = tn + ".png"
        tntxts = tn + ".txt"
        shutil.copyfile(input_folder + "images/clear/" + tnfiles, output_folder + "images/val/" + tnfiles)
        print("INFO. Copy ... ", input_folder + "images/clear/" + tnfiles, "; ", output_folder + "images/val/" + tnfiles)

        # Read original image
        image = cv2.imread(input_folder + "images/clear/" + tnfiles)
        h, w = image.shape[:2]
        # Read YOLO annotation file
        with open(input_folder + "labels/" + tntxts, 'r') as file:
            lines = file.readlines()
        temclear = ''
        temclearlist = []
        for line in lines:
            temclear = temclear + line
        temclearlist = temclear.split("\n")
        hdndata = []
        for line in range(len(temclearlist)):
            if len(temclearlist[line]) != 0:
                hdndata.append(temclearlist[line])
        hdspacetab = []
        alltemspacetabs = []
        for spacetabs in hdndata :
            temspacetabs = spacetabs.split("\t")
            for line in range(len(temspacetabs)):
                if len(temspacetabs[line]) != 0:
                    alltemspacetabs.append(temspacetabs[line])
            hdspacetab.append(alltemspacetabs)
        mathtoyolo = []
        dataobj = []
        datatag = []
        finaldatalist = []
        for mm in hdspacetab:
            datatag = mm[0]
            dataobj = mm[1:]
            for i in range(len(dataobj)):
                if  i % 2 != 0:
                    dataobj[i] = format(float(dataobj[i])/w, '.6f')
                if i % 2 == 0:
                    dataobj[i] = format(float(dataobj[i])/h, '.6f')
            dataobj.insert(0,datatag)
            str = " ".join(dataobj)
            finaldatalist.append(str)
        contextstr = "\n".join(finaldatalist)
        with open( output_folder + "labels/val/" + tntxts ,'w') as f:
            f.write(contextstr)
        print("INFO. Convert ... ", input_folder + "labels/" + tntxts, "; ", output_folder + "labels/val/" + tntxts)
    for tn in train_name:
        tnfiles = tn + ".png"
        tntxts = tn + ".txt"
        shutil.copyfile(input_folder + "images/clear/" + tnfiles, output_folder + "images/train/" + tnfiles)
        print("INFO. Copy ... ", input_folder + "images/clear/" + tnfiles, "; ", output_folder + "images/train/" + tnfiles)

        # Read original image
        image = cv2.imread(input_folder + "images/clear/" + tnfiles)
        h, w = image.shape[:2]
        # Read YOLO annotation file
        with open(input_folder + "labels/" + tntxts, 'r') as file:
            lines = file.readlines()
        temclear = ''
        temclearlist = []
        for line in lines:
            temclear = temclear + line
        temclearlist = temclear.split("\n")
        hdndata = []
        for line in range(len(temclearlist)):
            if len(temclearlist[line]) != 0:
                hdndata.append(temclearlist[line])
        hdspacetab = []
        alltemspacetabs = []
        for spacetabs in hdndata :
            temspacetabs = spacetabs.split("\t")
            for line in range(len(temspacetabs)):
                if len(temspacetabs[line]) != 0:
                    alltemspacetabs.append(temspacetabs[line])
            hdspacetab.append(alltemspacetabs)
        mathtoyolo = []
        dataobj = []
        datatag = []
        finaldatalist = []
        for mm in hdspacetab:
            datatag = mm[0]
            dataobj = mm[1:]
            for i in range(len(dataobj)):
                if  i % 2 != 0:
                    dataobj[i] = format(float(dataobj[i])/w, '.6f')
                if i % 2 == 0:
                    dataobj[i] = format(float(dataobj[i])/h, '.6f')
            dataobj.insert(0,datatag)
            str = " ".join(dataobj)
            finaldatalist.append(str)
        contextstr = "\n".join(finaldatalist)
        with open( output_folder + "labels/train/" + tntxts ,'w') as f:
            f.write(contextstr)
        print("INFO. Convert ... ", input_folder + "labels/" + tntxts, "; ", output_folder + "labels/train/" + tntxts)

