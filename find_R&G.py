import cv2
import numpy as np

class Coordinate:
    def __int__(self,x,y):
        self.x=x
        self.y=y
target = Coordinate()
current= Coordinate()
# 初始化最大面积和对应的轮廓索引
max_area_green = 0
max_contour_index_green = -1

max_area_red = 0
max_contour_index_red = -1

# 定义面积阈值
area_threshold = 100

# 打开摄像头
cap = cv2.VideoCapture(0)

#设置参数
lower_green = np.array([0, 0, 0])
upper_green = np.array([176, 255, 255])

lower_red = np.array([0, 0, 0])
upper_red = np.array([176, 255, 255])
while True:
    # 读取摄像头帧
    ret, frame = cap.read()

    # 将图像转换为HSV颜色空间
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # 根据颜色范围创建掩膜
    mask_green = cv2.inRange(hsv, lower_green, upper_green)
    mask_red = cv2.inRange(hsv, lower_red, upper_red)

    # 寻找绿色LED的轮廓
    contours_green, _ = cv2.findContours(mask_green, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    # 寻找红色LED的轮廓
    contours_red, _ = cv2.findContours(mask_red, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # 遍历绿色LED轮廓并绘制矩形框
    for i, contour_green in enumerate(contours_green):
        area_green = cv2.contourArea(contour_green)
        if area_green > area_threshold:
            # 更新最大面积和对应的轮廓索引
            if area_green > max_area_green:
                max_area_green = area_green
                max_contour_index_green = i
            x1, y1, w1, h1 = cv2.boundingRect(contour_green)
            region = frame[y1:y1 + h1, x1:x1 + w1]
            cv2.rectangle(frame, (x1, y1), (x1 + w1, y1 + h1), (0, 0, 255), 2)
            print(cv2.mean(region))
            cv2.putText(frame, 'Green LED', (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 2)

    if max_contour_index_green != -1:
        # 获取最大轮廓的坐标值
        x1, y1, w1, h1 = cv2.boundingRect(contours_green[max_contour_index_green])
        print("green 最大轮廓的坐标值：", x1, y1, w1, h1)
    else:
        print("未找到最大轮廓")

    # 遍历红色LED轮廓并绘制矩形框
    for i, contour_red in enumerate(contours_red):
        area_red = cv2.contourArea(contour_red)
        if area_red > area_threshold:
            # 更新最大面积和对应的轮廓索引
            if area_red > max_area_red:
                max_area_red = area_red
                max_contour_index_red = i
            x2, y2, w2, h2 = cv2.boundingRect(contour_red)
            region=frame[y2:y2+h2,x2:x2+w2]
            cv2.rectangle(frame, (x2, y2), (x2+w2, y2+h2), (0, 0, 255), 2)
            print(cv2.mean(region))
            cv2.putText(frame, 'Green LED', (x2, y2-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 2)

    if max_contour_index_red != -1:
        # 获取最大轮廓的坐标值
        x2, y2, w2, h2 = cv2.boundingRect(contours_green[max_contour_index_red])
        print("red 最大轮廓的坐标值：", x2, y2, w2, h2)
    else:
        print("未找到最大轮廓")

    # 显示图像
    cv2.imshow('original',frame)

    # 按下Esc键退出程序
    if cv2.waitKey(1) == 27:
        break

# 释放摄像头和窗口
cap.release()
cv2.destroyAllWindows()