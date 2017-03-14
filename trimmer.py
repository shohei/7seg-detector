import cv2

# x = 10  
# y = 233 
# width = 180 
# height = 70 
# x = 229
# y = 253
# width = 138 
# height =  81
# x =  227
# y =  250
# width =  137
# height =  70
x =  259
y =  260
width =  138
height =  79

src = cv2.imread('image.jpg', 1)
dst = src[y:y+height, x:x+width]
cv2.imwrite('dst.jpg', dst)

