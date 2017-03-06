import cv2

def mouse_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONUP:
        print "(x,y)= ",x,y

img = cv2.imread("target.jpg", 1)
cv2.namedWindow("img")
cv2.setMouseCallback("img", mouse_event)

while (True):
    cv2.imshow("img", img)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cv2.destroyAllWindows()
