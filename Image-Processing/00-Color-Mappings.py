# # Colorspaces
# 
# Let's have a brief introduction into converting to different colorspaces! The video goes into more detail about colorspaces.
# 
# Quick Info Link: 
# https://en.wikipedia.org/wiki/HSL_and_HSV
# 

import cv2
import matplotlib.pyplot as plt
import numpy as np


img = cv2.imread('../DATA/00-puppy.jpg')


# ### Converting to Different Colorspaces

img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.imshow(img)
plt.show()


# **Converting to HSV**
# https://en.wikipedia.org/wiki/HSL_and_HSV


img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
plt.imshow(img)
plt.show()
img = cv2.imread('../DATA/00-puppy.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2HLS)
plt.imshow(img)
plt.show()
