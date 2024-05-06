import cv2
import numpy as np

size = 400
image = np.ones((size, size, 3), dtype=np.uint8) * 255  # Белый фон

cv2.circle(image, (size // 2, size // 2), size // 3, (0, 0, 255), -1)  # Красный круг в центре
cv2.ellipse(image, (size // 2, size // 2), (size // 3, size // 6), 0, 0, 180, (0, 255, 0), -1)  # Зеленая половина эллипса
cv2.line(image, (size // 2 - size // 6, size // 2), (size // 2 + size // 6, size // 2), (255, 0, 0), 5)  # Синяя линия

cv2.imshow('Urban', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
