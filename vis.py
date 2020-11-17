import cv2
import os
import time

import tensorflow as tf

from lib.core.api.face_detector import FaceDetector

os.environ["CUDA_VISIBLE_DEVICES"] = "0"
detector = FaceDetector(['./model/detector.pb'])


def GetFileList(dir, fileList):
    newDir = dir
    if os.path.isfile(dir):
        fileList.append(dir)
    elif os.path.isdir(dir):
        for s in os.listdir(dir):
            # if s == "pts":
            #     continue
            newDir = os.path.join(dir, s)
            GetFileList(newDir, fileList)
    return fileList


def face_detect():
    count = 0
    data_dir = 'people/'
    pics = []
    GetFileList(data_dir, pics)
    print(pics)
    pics = [x for x in pics if 'jpg' in x or 'png' in x]
    # pics.sort()

    img_count = 0
    for pic in pics:
        img_count += 1
        img = cv2.imread(pic)

        img_show = img.copy()

        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        star = time.time()
        boxes = detector(img, 0.5)

        print(boxes.shape[0])
        if boxes.shape[0] == 0:
            print(pic)
        for box_index in range(boxes.shape[0]):
            bbox = boxes[box_index]

            # crop and save faces here
            cv2.rectangle(img_show, (int(bbox[0]), int(bbox[1])),
                          (int(bbox[2]), int(bbox[3])), (255, 0, 0), 4)


        # cv2.namedWindow('res', 0)
        # cv2.imshow('res', img_show)
        cv2.imwrite('faces/' + str(img_count) + '.jpg', img_show)
        # cv2.waitKey(0)
    print(count)


if __name__ == '__main__':
    face_detect()
