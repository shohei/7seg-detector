import cv2

counter = 0
x0 = 0
y0 = 0

class MyCounter:
    def __init__(self):
        self.counter = 0
        self.x0= 0
        self.y0= 0
        self.x1= 0
        self.y1= 0

def mouse_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONUP:
        print "(x,y)= ",x,y
        if mc.counter==0:
            mc.x0 = x
            mc.y0 = y
            mc.counter = mc.counter+1
        elif mc.counter==1:
            mc.x1 = x
            mc.y1 = y
            width = mc.x1-mc.x0
            height = mc.y1-mc.y0
            print "x = ",mc.x0
            print "y = ",mc.y0
            print "width = ",width
            print "height = ",height
            mc.counter = 0

img = cv2.imread("image.jpg", 1)
cv2.namedWindow("img")
cv2.setMouseCallback("img", mouse_event)

mc = MyCounter()

while (True):
    cv2.imshow("img", img)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cv2.destroyAllWindows()
