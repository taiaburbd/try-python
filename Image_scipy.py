
from skimage import io, img_as_ubyte
import numpy as np
import matplotlib.pyplot as plt

img=img_as_ubyte(io.imread("images/monkey.jpg", as_gray=True))

flippedLR =np.fliplr(img)
flippedUD =np.flipud(img)

plt.subplot(3,1,1)
plt.imshow(img,cmap="Greys")

plt.subplot(2,2,3)
plt.imshow(flippedLR,cmap="Blues")
plt.subplot(2,2,4)
plt.imshow(flippedUD,cmap="Reds")

plt.show()
