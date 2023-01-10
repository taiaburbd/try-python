from skimage import io, img_as_ubyte


img=img_as_ubyte(io.imread("images/monkey.jpg", as_gray=True))

print(img.shape, img.dtype)
print(img[10:20])

mean_grey=img.mean()
max_value=img.max()
min_value=img.min()

print("Min,Max and Mean are: ", min_value, max_value,mean_grey)