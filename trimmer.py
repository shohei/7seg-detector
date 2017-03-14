import cv2

#x = 10  
#y = 233 
#width = 180 
#height = 70 
#x =  241
#y =  256
#width =  133
#height =  78
x =  250
y =  260
width =  138
height =  79
#x =  205
#y =  259
#width =  176
#height =  73

src = cv2.imread('image.jpg', 1)
dst = src[y:y+height, x:x+width]
cv2.imwrite('dst.jpg', dst)

