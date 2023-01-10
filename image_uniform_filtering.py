from scipy import ndimage
from skimage import io, img_as_ubyte
import numpy as np
import matplotlib.pyplot as plt

img=img_as_ubyte(io.imread("images/monkey.jpg", as_gray=True))

uniform_filtered=ndimage.uniform_filter(img,size=50)

plt.imshow(uniform_filtered)
plt.show()