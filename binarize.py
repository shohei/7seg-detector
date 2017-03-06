import cv2

im_gray = cv2.imread('dst.jpg', cv2.CV_LOAD_IMAGE_GRAYSCALE)
(thresh, im_bw) = cv2.threshold(im_gray, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
thresh = 70 
im_bw = cv2.threshold(im_gray, thresh, 255, cv2.THRESH_BINARY)[1]

im_wb = cv2.bitwise_not(im_bw)

#cv2.imwrite('bwimage.jpg',im_bw)
cv2.imwrite('bwimage.jpg',im_wb)


