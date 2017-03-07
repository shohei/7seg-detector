import cv2

#x = 10  
#y = 233 
#width = 180 
#height = 70 
x = 172
y = 245
width = 138
height =  81
src = cv2.imread('image.jpg', 1)
dst = src[y:y+height, x:x+width]
cv2.imwrite('dst.jpg', dst)

