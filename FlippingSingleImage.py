import cv2
image=cv2.imread("Resources\sample.jpg")

Vflip=cv2.flip(image,0)#Vertically Flipped
Hflip=cv2.flip(image,1)#Horizontally Flipped
cv2.imshow("Original Image",image)
cv2.imshow("Vertically Flipped Image",Vflip)
cv2.imshow("Horizontally Flipped Image",Hflip)
cv2.waitKey(0)