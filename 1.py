import cv2
import gray
import numpy as np
from matplotlib import pyplot as plt

# Read the image
img = cv2.imread('receipt.jpg',0)
# Simple thresholding
ret,thresh1 = cv2.threshold(img,210,255,cv2.THRESH_BINARY)
cv2.imshow(thresh1,gray)