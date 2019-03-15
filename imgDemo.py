# coding=gbk
# from skimage import io,transform
# import matplotlib.pyplot as plt
#
#
# img = io.imread("d:/a.jpg")
# plt.imshow(img)
# plt.show()
# img = transform.resize(img, (800, 600))
# plt.imshow(img)
# plt.show()
# io.imsave("d:/ab.jpg", img)
# coding=gbk
from PIL import Image

# img = Image.open("d:/a.jpg")
# print(img.size)
# cropped = img.crop((0, 0, 800, 600))  # (left, upper, right, lower) #适合裁剪
# cropped.save("d:/aa.jpg")

im = Image.open("d:/a.jpg")
im.show()
#
# # 原图像缩放为128x128
im = im.resize((600, 800))
im.show()
im.save("d:/qq.jpg")
print("成功")

