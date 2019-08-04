import numpy as np
import matplotlib.pyplot as plt
import cv2

#Tentando abrir uma imagem que nao existe
# WONT GIVE ERROR! GIVES NONE INSTEAD!!!
img = cv2.imread("some/wrong/path.jpg")
print img

img = cv2.imread('../DATA/00-puppy.jpg')
print img.shape
print img

img_bgr = cv2.imread('../DATA/00-puppy.jpg')
plt.imshow(img_bgr)
'''The image has been correctly loaded by openCV as a numpy array, but the color of each pixel has been sorted as BGR.
Matplotlib's plot expects an RGB image so, for a correct display of the image, it is necessary to swap those channels. 
This operation can be done either by using openCV conversion functions cv2.cvtColor() or by working directly with the numpy array.'''
plt.title('BGR Image')
plt.show()

img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.imshow(img_rgb)
plt.title('RGB Image')
plt.show()

img_gray = cv2.imread('../DATA/00-puppy.jpg',cv2.IMREAD_GRAYSCALE)
plt.imshow(img_gray)
plt.title('Grayscale Image')
plt.show()

img_gray = cv2.imread('../DATA/00-puppy.jpg',cv2.IMREAD_GRAYSCALE)
plt.imshow(img_gray,cmap='gray')
plt.title('Grayscale Image Corrected')
plt.show()

#Resize Images

print "\nOriginal Image: ",img_rgb.shape
new_img =cv2.resize(img_rgb,(1300,275))
plt.imshow(new_img)
plt.title('Resized Image')
plt.show()
print "Resized Image: ",new_img.shape

#by ratio
w_ratio = 0.5
h_ratio = 0.5
new_img =cv2.resize(img_rgb,(0,0),img,w_ratio,h_ratio)
plt.imshow(new_img)
plt.title('Scaled Image')
plt.show()
print "Scaled Image: ",new_img.shape

#Flipping Images

# Along central x axis
new_img = cv2.flip(new_img,0)
plt.imshow(new_img)
plt.title('Fliped Image X')
plt.show()
print "Fliped Image X: ",new_img.shape

# Along central y axis
new_img = cv2.flip(new_img,1)
plt.imshow(new_img)
plt.title('Fliped Image Y')
plt.show()
print "Fliped Image Y: ",new_img.shape

# Along both axis
new_img = cv2.flip(new_img,-1)
plt.imshow(new_img)
plt.title('Fliped Image XY')
plt.show()
print "Fliped Image XY: ",new_img.shape

print cv2.imwrite('my_new_picture.jpg',new_img)

img_opencv = cv2.imread('../DATA/00-puppy.jpg',cv2.IMREAD_GRAYSCALE)
cv2.namedWindow('Imagem',cv2.WINDOW_NORMAL)
cv2.imshow('Imagem',img_opencv)
cv2.waitKey(0)

