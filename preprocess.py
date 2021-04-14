import cv2
import numpy as np
import glob
image=glob.glob('data/validation/*')
val_no=len(image)
image.extend(glob.glob('data/training/*'))
train_no=len(image)-val_no
for i in image:
  im1=cv2.imread(i)
  if im1.shape!=(512,512,3):
    resize=cv2.resize(im1,(512,512))
    cv2.imwrite(i,resize)

print(f"Resizing Sccessful! You have {train_no} training images and {val_no} validation images.")

