import numpy as np
import cv2
import matplotlib.pyplot as plt

# 1. 读取图像
img = cv2.imread('./data/car.jpg', 0)

# 2. 创建可调的窗口
cv2.namedWindow('image', cv2.WINDOW_NORMAL)
# 3. 显示图像
cv2.imshow('image', img)

# 利用matplotlib显示窗口
plt.imshow(img, cmap='gray', interpolation='bicubic'), plt.axis("off")

# 4. 图像的保存
cv2.imwrite("./data/car2.jpg", img)
# 利用matplotlib保存图片
plt.savefig("./data/car3.png")
plt.show()

# 5. 退出窗口
k = cv2.waitKey(0)  # 等待键盘输入，为毫秒级
if k == 27:  # 若输入ESC按键，则退出
    # if k == ord("k"):  # 若输入按键k或K，则退出
    cv2.destroyAllWindows()  # 退出程序自动删除窗口
