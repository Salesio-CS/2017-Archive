# -*- coding: utf-8 -*-
import cv2
import numpy as np
import collections

class KnowledgeImgTrim:
    def __init__(self, dirname, filename):
        self.dirname = dirname
        self.filename = filename
        self.image_load()
        self.analyze(filename)

    def image_load(self):
        path = "../img/taked/" + self.dirname + "/" + self.filename + ".jpg"
        print("> LOAD  IMAGE PATH ->  " + path)
        self.img = cv2.imread(path)

    def image_write(self):
        path = "../img/trimed/" + self.dirname + "/" + self.filename + ".png"
        cv2.imwrite(path, self.trimed)
        print("> WRITE IMAGE PATH -> " + path + "\n")

    def analyze(self, filename):
        hsv = cv2.cvtColor(self.img, cv2.COLOR_BGR2HSV)
        height, width = self.img.shape[:2]

        print("> ANALYZE BLACKBOARD")
        pixels = [[], [], []]

       # board_height,board_width=黒板のおおよそサイズ
        board_height = int(height // 5)
        board_width = int(width //  2)

        # 黒板の真ん中の方を撮影
        for i in range(board_height):
            for j in range(board_width):
                pixelValue = hsv[height//2-(board_height//2)+i,width//2-(board_width//2)+j]
                for k in range(3):
                    pixels[k].append(pixelValue[k])

        #cv2.rectangle(hsv, (width//2-(board_width//2),height//2-(board_height//2)), (width//2+(board_width//2),height//2+(board_height//2)), (0, 0, 255), 20)
        cv2.imwrite('../img/log/rect.png', hsv)
        avg = [sum(lst)/len(lst) for lst in pixels]

        leng = 30
        for i in range(3):
            if avg[i] < leng:
                avg[i] = leng
            elif avg[i] + leng > 255:
                avg[i] -= leng

        # 黒板の色で二値化をする
        len_min = np.array([avg[0]-leng, avg[1]-leng, avg[2]-leng], np.uint8)
        len_max = np.array([avg[0]+leng, avg[1]+leng, avg[2]+leng], np.uint8)
        threshold = cv2.inRange(hsv, len_min, len_max)
        cv2.imwrite('../img/log/thres.png', threshold)

        kernel = np.ones((5,5), np.uint8)
        closing = cv2.morphologyEx(threshold, cv2.MORPH_CLOSE, kernel)
        opening = cv2.morphologyEx(closing, cv2.MORPH_OPEN, kernel)
        kernel = np.ones((10,10), np.uint8)
        closing = cv2.morphologyEx(opening, cv2.MORPH_CLOSE, kernel)
        opening = cv2.morphologyEx(closing, cv2.MORPH_OPEN, kernel)
        # cv2.imwrite('../img/log/opening.png', opening)

        #輪郭検出
        image, contours, hierarchy = cv2.findContours(opening,cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        # print("====== FIND CONTOURS =======")
        # print(">> " + str(len(contours)) + " CONTOURS FOUND\n")

        # 最大領域の導出
        areas = []
        for contour in contours:
            area = cv2.contourArea(contour)
            areas.append(area)

        self.x_sizes = []
        self.y_sizes = []
        for item in contours[areas.index(max(areas))]:
            self.x_sizes.append(item[0][0])
            self.y_sizes.append(item[0][1])

        self.size = [min(self.y_sizes),max(self.y_sizes),min(self.x_sizes),max(self.x_sizes)]
        self.original = self.img[self.size[0]:self.size[1], self.size[2]:self.size[3]]

        print("> BLACKBOARD RANGE" + str(self.original))
        print("> COMPLETE\n")


        # 以下ループ，以上一回

    def trimming (self, dirname, filename):
        self.dirname = dirname
        self.filename = filename
        self.image_load()
        self.trimed = self.img[self.size[0]:self.size[1], self.size[2]:self.size[3]]
        self.teacher_proc()
        self.image_write()

    def teacher_proc(self):
        print("> BEGIN TEACHER PROCESS")
        sabun = abs(self.trimed - self.original)

        cv2.imwrite("../img/log/delete_t/trimed.jpg", self.trimed)
        cv2.imwrite("../img/log/delete_t/orig.jpg", self.original)

        gray = cv2.cvtColor(sabun, cv2.COLOR_BGR2GRAY)
        ret, thres = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY)
        cv2.imwrite("../img/log/delete_t/sabun.jpg", thres)

        kernel = np.ones((5,5), np.uint8)
        #closing = cv2.morphologyEx(thres, cv2.MORPH_CLOSE, kernel)
        #cv2.imwrite("../img/log/delete_t/morph0.jpg", closing)
        opening = cv2.morphologyEx(thres, cv2.MORPH_OPEN, kernel)
        cv2.imwrite("../img/log/delete_t/morph1.jpg", opening)
        kernel = np.ones((10,10), np.uint8)
        closing = cv2.morphologyEx(opening, cv2.MORPH_CLOSE, kernel)
        opening = cv2.morphologyEx(closing, cv2.MORPH_OPEN, kernel)
        cv2.imwrite("../img/log/delete_t/morph2.jpg", opening)

        image, contours, hierarchy = cv2.findContours(opening, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        if(len(contours) == 0):
            return

        areas = []
        for contour in contours:
            area = cv2.contourArea(contour)
            areas.append(area)

        x_sizes = []
        for item in contours[areas.index(max(areas))]:
            x_sizes.append(item[0][0])

        # print([min(x_sizes),max(x_sizes), 0,self.trimed.shape[0]])
        self.trimed[0:self.trimed.shape[0],min(x_sizes):max(x_sizes)] = self.original[:self.trimed.shape[0],min(x_sizes):max(x_sizes)]

        cv2.imwrite("../img/log/delete_t/after.jpg", self.trimed)
        print("> END TEACHER PROCESS")

        '''t = self.trimed
        cv2.rectangle(t, (min(x_sizes), 0), (max(x_sizes),
        opening.shape[0]), (0, 0, 0), -1, 8)
        cv2.imwrite("../img/log/rect.jpg", t)'''
