import numpy as np
import cv2


# # 查看支持的鼠标事件
# events = [i for i in dir(cv2) if 'EVENT' in i]
# print(events)


# 1. 点击鼠标则执行预定函数

# mouse callback function
def draw_circle(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle(img, (x, y), 100, (255, 0, 0), -1)


# 创建图像与窗口并将窗口与回调函数绑定
img = np.zeros((500, 500, 3), np.uint8)
cv2.namedWindow('image')
cv2.setMouseCallback('image', draw_circle)

while True:
    cv2.imshow('image', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):  # 按q键退出
        break
cv2.destroyAllWindows()

