import numpy as np
import cv2

img = cv2.imread('')
img = cv2.resize(img, None, fx = 0.25, fy = 0.25)

brown = [0, 128, 0]  # RGB
diff = 20 
boundaries = [([brown[2]-diff, brown[1]-diff, brown[0]-diff],
               [brown[2]+diff, brown[1]+diff, brown[0]+diff])]
# in order BGR as opencv represents images as numpy arrays in reverse order

for (lower, upper) in boundaries:
  lower = np.array(lower, dtype=np.uint8)
upper = np.array(upper, dtype=np.uint8)
mask = cv2.inRange(img, lower, upper)
output = cv2.bitwise_and(img, img, mask=mask)

ratio_brown = cv2.countNonZero(mask)/(img.size/3)
print('brown pixel percentage:', np.round(ratio_brown*100, 2))

cv2.imshow("images", np.hstack([img, output]))
cv2.waitKey(0)