#a = lambda x:x*x
#print(a(3))

import cv2

img = cv2.imread(r'C:\Users\airrain\Desktop\jian.jpg', 0)
cv2.imshow('jian', img)
cv2.waitKey(0)