import numpy as np
import cv2
import ftlib as ft

# img = cv2.imread('test_image.tif',0) #binary image
img = cv2.imread('up_image.png',0) #binary image
thinned_image = ft.fastThin(img)
res = np.hstack((img,thinned_image))
# cv2.imshow('original image',img)
# cv2.imshow('thinned image',thinned_image)
cv2.imshow("result_comparation",res)
cv2.imwrite(ft.dirname + 'res' + str(ft.time.time())+'.png', res)
cv2.waitKey(0) # press any key to close
cv2.destroyAllWindows()
