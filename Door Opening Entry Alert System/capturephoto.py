import cv2
def photocapture():
    camera_port = 0
    camera = cv2.VideoCapture(camera_port)
    camera.set(cv2.cv.CV_CAP_PROP_FRAME_WIDTH, 1024)
    camera.set(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT, 768)
    return_value, image = camera.read()
    if return_value:
        cv2.imwrite("test.png", image)
    print "capturing new image"
    print "exit"
    camera.release() # so that others can use the camera as soon as possible
