
import numpy as np
from imageio import imread,imsave

img=imread('images/rgb.jpeg')

red_img= img * [1.,0.,0.]
green_img=img * [0.,1.,0.]
blue_img=img * [0.,0.,1.]

imsave('images/red_img.jpeg',red_img)
imsave('images/green_img.jpeg',green_img)
imsave('images/blue_img.jpeg',blue_img)