import glob
import cv2
image_path=glob.glob("Resources/*.jpg")
path='Resources'
for file in image_path: 
    image_name=file.split('\\')[-1].replace('.jpg','')
    img=cv2.imread(file)
    VF=cv2.flip(img,0)
    HF=cv2.flip(img,1)
    cv2.imshow("Image",img)
    cv2.imwrite(f'Flipping Images/{image_name}Original Image.jpg',img)
    cv2.imshow("HF",HF)
    cv2.imwrite(f'Flipping Images/{image_name}Horizontal.jpg',HF)
    cv2.imshow("VF",VF)
    cv2.imwrite(f'Flipping Images/{image_name}Vertical.jpg',HF)
    #cv2.imshow("Image",img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()