import numpy as np

import matplotlib.pyplot as plt

from PIL import Image

pic = Image.open('../DATA/00-puppy.jpg')
#pic.show()
print(type(pic))
pic_arr = np.asarray(pic)
plt.imshow(pic_arr)
plt.show()
print(pic_arr.shape)
pic_red = pic_arr.copy()
pic_red[:, :, 1] = 0
pic_red[:, :, 2] = 0
plt.imshow(pic_red)
plt.title('Image Red Channel')
plt.show()