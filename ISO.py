import cv2
import numpy as np


image = cv2.imread('color_text.jpg')

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

_, binary = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY_INV)

contours, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

colors = [(0, 0, 255), (0, 255, 0), (255, 0, 0), (0, 255, 255), (255, 0, 255), (255, 255, 0)]

for i, contour in enumerate(contours):
    color = colors[i % len(colors)]
    cv2.drawContours(image, [contour], -1, color, 2)

cv2.imshow('Processed Image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()

