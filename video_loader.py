######
## This file is responsisble for opening a video file, extracting the next frame, and saving it in the project's "temp" folder
## and then deleting the file afterwards so that lots of space isn't taken up
## I really need to clean my laptop screen lmao
######

import cv2 as cv
import os

class loader:
    def __init__(self, filename):
        self.filename_ = filename
        self.vid_ = cv.VideoCapture(self.filename_)
        self.count_ = 0

    def get_next_frame(self):
        self.vid_.set(cv.CAP_PROP_POS_FRAMES, self.count_)
        result, frame = self.vid_.read()
        print("next frame success: ", result)
        self.count_ += 1
        cv.imwrite("temp\\frame%d.jpg" % self.count_, frame)
        return str("temp\\frame" + str(self.count_) + ".jpg")

    def complete(self):
        return self.count_ == self.vid_.get(cv.CAP_PROP_FRAME_COUNT)

    def flush_temp(self):
        filelist = [f for f in os.listdir(".\\temp")]
        for f in filelist:
            os.remove(os.path.join(".\\temp", f))

