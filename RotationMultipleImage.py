import glob
from PIL import Image
path=glob.glob('Resources/*.jpg')
for file in path:
  #img=Image.open(file)
  print(file)
dest_path = 'RotatedImages'
for imagefile in path:
  img = Image.open(imagefile)
  image_name = imagefile.split('\\')[-1]
  image_file_name = image_name.rstrip('.jpg')

## 90 Degree
  imge = img.transpose(Image.ROTATE_90)
  imge.save(dest_path+'\\'+ image_file_name +'_Ninety' +'.jpg')
  

## 45 Degree
  imge = img.transpose(Image.ROTATE_180)
  imge.save(dest_path+'\\'+ image_file_name +'_180' +'.jpg')  