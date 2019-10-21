import os
import cv2
import time
import matplotlib
matplotlib.use("Pdf")
import mxnet as mx
from gluoncv import model_zoo, data, utils

class ObjectDetection():

    def __init__(self):
        self.classes = ['cocacola', 'cocacola-zero', 'juice', 'noodles', 'hand']
        self.net = model_zoo.get_model('ssd_512_resnet50_v1_custom', classes=self.classes, pretrained_base=False)
        param_files = ([x for x in os.listdir('.') if x.endswith('.params')])
        selected = param_files[0]
        self.net.load_parameters(selected)

    def detect(self, filename):
        # x, img = data.transforms.presets.ssd.load_test(filename, short=512)
        # x, img = data.transforms.presets.ssd.transform_test([mx.nd.array(cv2.imread(filename))], short=512)
        img = cv2.imread(filename)
        img = cv2.resize(img, (512, 512))
        x = self.transform_image(img)
        class_IDs, scores, bounding_boxes = self.net(x)
        return class_IDs.asnumpy(), scores.asnumpy(), bounding_boxes.asnumpy()

    def transform_image(self, image):
        image = np.array(image) - np.array([123., 117., 104.])
        image /= np.array([58.395, 57.12, 57.375])
        image = image.transpose((2, 0, 1))
        image = image[np.newaxis, :]
        return mx.nd.array(image)

if __name__ == '__main__':
    objectDetection = ObjectDetection()
    filename = '../images/v1/test/frame_1571435703.4214327.jpg'
    start = time.time()
    class_IDs, scores, bounding_boxes = objectDetection.detect(filename)
    end = time.time()
    #print('class_IDs:', class_IDs)
    #print('scores:', scores)
    #print('bounding_boxes:', bounding_boxes)
    print('time:', end-start)
