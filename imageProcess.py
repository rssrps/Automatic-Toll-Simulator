import cv2
import numpy as np
from PIL import Image
import pytesseract
import Tkinter

def check(a):
  if(a<=15 and a>=0):
    return 1
  else:
    return 0 

def processImage(imgCount):
  path = "image/" + str(imgCount) + ".png"
  img = cv2.imread(path,cv2.CV_LOAD_IMAGE_COLOR)   # Load an color image
 
  #crop_img = img[660:720, 350:640]
  # cv2.imshow("cropped", crop_img)
  # cv2.waitKey(0)
  
  for x in range(980):
   for y in range(975):
    color = img[x,y]
    if(check(color[0])==0 or check(color[1])==0 or check(color[2])==0):
     img[x,y] = (255,255,255)

  carNo = pytesseract.image_to_string( img , lang = "eng")		# Extract Car number from image using pytesseract
  print carNo
  return carNo


