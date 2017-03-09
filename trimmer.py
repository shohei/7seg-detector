import cv2

#x = 10  
#y = 233 
#width = 180 
#height = 70 
x =  227
y =  250
width =  137
height =  80 
src = cv2.imread('image.jpg', 1)
dst = src[y:y+height, x:x+width]
cv2.imwrite('dst.jpg', dst)

