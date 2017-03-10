import cv2

#x = 10  
#y = 233 
#width = 180 
#height = 70 
x =  242
y =  258
width =  133
height = 75 
src = cv2.imread('image.jpg', 1)
dst = src[y:y+height, x:x+width]
cv2.imwrite('dst.jpg', dst)

