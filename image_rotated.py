from scipy import ndimage
from skimage import io, img_as_ubyte
import numpy as np
import matplotlib.pyplot as plt

img=img_as_ubyte(io.imread("images/monkey.jpg", as_gray=True))

# Image will made reshape by True or False
rotated=ndimage.rotate(img,45,reshape=True)


plt.imshow(rotated)
plt.show()