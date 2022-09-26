import cv2
#import matplotlib.pyplot as plt
img=cv2.imread("Resources\Sample.jpg")
(h,w)=img.shape[:2]

center=(w/2,h/2)

angle90=-90
angle180=180

#scale=0

M = cv2.getRotationMatrix2D(center, angle90)
rotated90 = cv2.warpAffine(img, M, (h, w))

M = cv2.getRotationMatrix2D(center, angle180)
rotated180 = cv2.warpAffine(img, M, (h, w))

cv2.imshow("Original Image",img)
#cv2.waitKey(0)
#cv2.destroyAllWindows()
cv2.imshow("Rotated 90 degree",rotated90)
#cv2.waitKey(0)
#cv2.destroyAllWindows()
cv2.imshow("Rotated 180 degree",rotated180)
cv2.waitKey(0)
#cv2.destroyAllWindows()