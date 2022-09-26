import os
import cv2
from xml.etree import ElementTree

from cv2 import imread

file_name=("Resources/SampleXML.xml")
#print(file_name)
tree=ElementTree.parse(file_name)
#print(tree)
value=tree.findall('object/bndbox')

for i in value:
    xmin=i.find('xmin').text
    ymin=i.find('ymin').text
    xmax=i.find('xmax').text
    ymax=i.find('ymax').text
#print(xmin,ymin,xmax,ymax)
img=cv2.imread('Resources/Sample.jpg')
BB=cv2.rectangle(img,(int(xmin),int(ymin)),(int(xmax),int(ymax)),(0,0,0),2)
BB1=cv2.putText(img=BB, text='TBI', org=(int(xmin),int(ymin)+29), fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=1, color=(0, 0, 0),thickness=2)
cv2.imshow("output",BB1)
cv2.imwrite('Annotated/image1.jpg',BB1)
cv2.waitKey(0)

