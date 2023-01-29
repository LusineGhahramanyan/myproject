import cv2
import numpy as np

image = cv2.imread("main.jpg")
scale_percent = 30
width = int(image.shape[1] * scale_percent / 100)
height = int(image.shape[0] * scale_percent / 100)
dim = (width, height)
resized_image = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)

first = cv2.imread("anna1.jpg")
scale_percent2 = 30
width2 = int(first.shape[1] * scale_percent2 / 100)
height2 = int(first.shape[0] * scale_percent2 / 100)
dim2 = (width2, height2)
resized_first = cv2.resize(first, dim2, interpolation=cv2.INTER_AREA)

other = cv2.imread("flora1.jpg")
scale_percent3 = 30
width3 = int(other.shape[1] * scale_percent3 / 100)
height3 = int(other.shape[0] * scale_percent3 / 100)
dim3 = (width3, height3)
resized_other = cv2.resize(other, dim3, interpolation=cv2.INTER_AREA)

result = cv2.matchTemplate(resized_first, resized_image, cv2.TM_SQDIFF_NORMED)
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
# print(min_val, max_val, min_loc, max_loc)
x, y = min_loc
t_row, t_col = resized_first.shape[:2]
resized_image[y:y + t_row, x: x + t_col] = resized_other


cv2.imshow('Detect', resized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
print("hello Lusine")