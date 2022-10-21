import cv2
import numpy as np
import matplotlib.pyplot as plt


img = cv2.imread('./data/lena.tif')  # type: np.ndarray

# 1. 读取像素值
# 1.1 按照np.ndarray操作
px = img[100, 100]
blue = img[100, 100, 0]
# 1.2 np的arrat.item()
tmp = img.item(100, 100, 0)

# 2. 修改像素值
# 2.1 按照np.ndarray操作
img[101, 101] = [255, 255, 255]

# 2.2 np的arrat.itemset()
img.itemset((100, 100, 0), 255)

# 3. 图像的属性
# 属性包括: 行，列，通道，图像数据类型，像素数目
print(img.shape)
print(img.size)
print(img.dtype)

# 4. 拆分及合并图像通道
r, g, b = cv2.split(img)  # 拆分
img = cv2.merge([r, g, b])  # 合并

# 或者np合并
imgStack = np.stack((b, g, r), axis=2)
# cv2.imshow("npStack", imgStack)

# 5. 图像合并
imgStackH = np.hstack((img, img))  # 水平拼接
imgStackV = np.vstack((img, img))  # 垂直拼接
# cv2.imshow("hstack", imgStackH)
# cv2.imshow("vstack", imgStackV)

cv2.waitKey(0), cv2.destroyAllWindows()

# 6. 图像的复制
img_new = img.copy()

# 7. 鼠标选中ROI 裁剪
# ROI: region of interest
# roi = cv2.selectROI(img, showCrosshair=True, fromCenter=False)
# xmin, ymin, w, h = roi  # 矩形裁剪区域 (ymin:ymin+h, xmin:xmin+w) 的位置参数
# imgROI = img[ymin:ymin + h, xmin:xmin + w].copy()  # 切片获得裁剪后保留的图像区域
#
# cv2.imshow("DemoRIO", imgROI)
# cv2.waitKey(0)

# 8. 图像扩边操作
blue = [255, 0, 0]
replicate = cv2.copyMakeBorder(img, 10, 10, 10, 10, cv2.BORDER_REPLICATE)
reflect = cv2.copyMakeBorder(img, 10, 10, 10, 10, cv2.BORDER_REFLECT)
reflect101 = cv2.copyMakeBorder(img, 10, 10, 10, 10, cv2.BORDER_REFLECT101)
wrap = cv2.copyMakeBorder(img, 10, 10, 10, 10, cv2.BORDER_WRAP)
constant = cv2.copyMakeBorder(img, 10, 10, 10, 10, cv2.BORDER_CONSTANT, value=blue)

plt.subplot(231), plt.axis("off"), plt.imshow(img, 'gray'), plt.title('original')
plt.subplot(232), plt.axis("off"), plt.imshow(replicate, 'gray'), plt.title('replicate')
plt.subplot(233), plt.axis("off"), plt.imshow(reflect, 'gray'), plt.title('reflect')
plt.subplot(234), plt.axis("off"), plt.imshow(reflect101, 'gray'), plt.title('reflect101')
plt.subplot(235), plt.axis("off"), plt.imshow(wrap, 'gray'), plt.title('wrap')
plt.subplot(236), plt.axis("off"), plt.imshow(constant, 'gray'), plt.title('constant')

plt.show()
