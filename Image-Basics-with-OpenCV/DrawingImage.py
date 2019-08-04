import numpy as np
import cv2
import matplotlib.pyplot as plt

blank_img = np.zeros(shape=(512,512,3),dtype=np.uint8)
print blank_img.shape
plt.imshow(blank_img)
plt.title("Blank Image")
plt.show()

# pt1 = top left
# pt2 = bottom right
# if thickness < 0 - filled rectangle
cv2.rectangle(blank_img,(384,0),(510,128),(0,255,0),2,8,0)
print blank_img
nameWindow = "Rectangle"
cv2.namedWindow(nameWindow,cv2.WINDOW_NORMAL)
cv2.imshow(nameWindow, blank_img)
cv2.waitKey(0)
# pt1 = top left
# pt2 = bottom right
cv2.rectangle(blank_img,pt1=(200,200),pt2=(300,300),color=(0,0,255),thickness=5)
plt.imshow(blank_img)
plt.title("2 Square")
plt.show()

cv2.circle(img=blank_img, center=(100,100), radius=50, color=(255,0,0), thickness=5)
plt.imshow(blank_img)
plt.title("New Geometric")
plt.show()

cv2.circle(img=blank_img, center=(400,400), radius=50, color=(255,0,0), thickness=-1)
# Draw a diagonal blue line with thickness of 5 px
cv2.line(blank_img,pt1=(0,0),pt2=(511,511),color=(102, 255, 255),thickness=5)
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(blank_img,text='Hello',org=(0,500), fontFace=font,fontScale= 4,color=(255,255,255),thickness=2,lineType=cv2.LINE_AA)
plt.imshow(blank_img)
plt.title("New Geometric")
plt.show()

'''To draw a polygon, first you need coordinates of vertices. Make those points into an array of shape ROWSx1x2 where ROWS are number 
of vertices and it should be of type int32.'''

blank_img1 = np.zeros(shape=(512,512,3),dtype=np.uint8)
vertices = np.array([[100,300],[200,200],[400,300],[200,400]],np.int32)
print vertices.shape
pts = vertices.reshape((-1,1,2))
print pts.shape
cv2.polylines(blank_img1,[pts],isClosed=True,color=(255,0,0),thickness=5)
plt.imshow(blank_img1)
plt.show()