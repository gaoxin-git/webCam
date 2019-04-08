import cv2

class Camera(object):
    def __init__(self):
        self.cap = cv2.VideoCapture(0)

    def __del__(self):
        self.cap.release()

    def get_frame(self):
        ret, img = self.cap.read()
        # 因为openCV读取的图片并非jpeg格式，因此要用motion JPEG模式需要先将图片转码成jpg格式图片
        ret, jpg = cv2.imencode(".JPG",img)
        return jpg.tobytes()