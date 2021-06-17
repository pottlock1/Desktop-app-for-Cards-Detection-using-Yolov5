import torch
from PIL import Image
import cv2


class Predict:
    def __init__(self):
        self.model = torch.hub.load('yolov5', 'custom', path='yolov5/yolov5s_cards.pt', source='local')

    def single_predict(self, path):
        img = cv2.imread(path)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        result = self.model(img)
        img = result.imgs[0]
        class_names = result.names
        rectangles = result.xywh[0]
        for rectangle in rectangles:
            rectangle = list(map(int, rectangle))
            x, y, w, h, conf, cls = rectangle
            cls = class_names[cls]

            img = cv2.rectangle(img, (x-int(w/2), y-int(h/2)), (x+int(w/2), y+int(h/2)), (0, 240, 0), 2)
            img = cv2.putText(img, cls, (x-int(w/2), y-int(h/2)-5), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (250, 0, 0), 2)

        return img

    def live_predict(self):
        camera = cv2.VideoCapture(0)

        while True:
            ret, frame = camera.read()
            frame = cv2.flip(frame, 1)
            result = self.model(frame)
            classes = result.names
            for rectangle in result.xywh[0]:
                x, y, w, h, conf, cls = list(map(int, rectangle))
                frame = cv2.rectangle(frame, (x-int(w/2), y-int(h/2)), (x + int(w/2), y + int(h/2)), (0, 255, 0), 2)
                cv2.putText(frame, classes[cls], (x-int(w/2), y-int(h/2)-5), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)
            cv2.imshow('result', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        camera.release()
        cv2.destroyAllWindows()
