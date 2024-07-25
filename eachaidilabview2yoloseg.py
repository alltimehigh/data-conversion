import cv2
import os

image_path = './test/ai.png'
ad_labview_txt_path = './test/ai.txt'

# Read original image
image = cv2.imread(image_path)
h, w = image.shape[:2]

# Read YOLO annotation file
with open(ad_labview_txt_path, 'r') as file:
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

# EX : H -> 315; W -> 700; Picture -> 315*700
# The point -> h = x1 = 35.576923076923094; w = y1 = 11.538461538461538
# YOLO point -> h = x1 = 35.576923076923094 / 315 = 0.112943;
#               w = y1 = 11.538461538461538 / 700 = 0.016484

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

def txt(name,text): # Define function name
    b = os.getcwd()[:0] + 'new\\'
    if not os.path.exists(b): # Determine whether the current path exists, if not, create a new folder
        os.makedirs(b)
    xxoo = b + name + '.txt' # Create a txt file in the new file under the path of the current py file
    file = open(xxoo,'w')
    file.write(text) # Write content information
    file.close()
    print ('OK!')
txt('data', contextstr) # Create a txt file named test with the content str !!


