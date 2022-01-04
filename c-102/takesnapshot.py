import cv2
def takesnapshot():
    capture_obj=cv2.VideoCapture(0)
    result=True
    while(result):
        ret,frame=capture_obj.read()
        cv2.imwrite("newpicture1.jpg",frame)
        result=False
    capture_obj.release()
    cv2.destroyAllWindows()
takesnapshot()