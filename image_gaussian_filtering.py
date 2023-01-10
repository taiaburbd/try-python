from scipy import ndimage
from skimage import io, img_as_ubyte
import numpy as np
import matplotlib.pyplot as plt

img=img_as_ubyte(io.imread("images/monkey.jpg", as_gray=True))

gaussian_filter=ndimage.gaussian_filter(img,sigma=8)

plt.imshow(gaussian_filter)
plt.show()