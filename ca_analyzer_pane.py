from PyQt5.Qt import *
from resource.ca_analyzer import Ui_MainWindow
import cv2 as cv
import numpy as np


class Analyzer(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.img = None
        self.setupUi(self)

    # def gray_to_rgb(self, rgb, img_gray):
    #     r = rgb[:, :, 0]
    #     g = rgb[:, :, 1]
    #     b = ((img_gray) - 0.299 * r - 0.587 * g) / 0.114
    #     gray_rgb = np.zeros((rgb.shape))
    #     gray_rgb[:, :, 2] = b
    #     gray_rgb[:, :, 0] = r
    #     gray_rgb[:, :, 1] = g
    #     return gray_rgb

    def xt_analyzer(self, files, files_num, file_no, data_type, signal_type, analyze_mode, channels):
        cur_file = files[file_no]
        self.img = cv.imread(cur_file, cv.IMREAD_UNCHANGED)
        img_trans = self.img.transpose()
        img_flip = cv.flip(img_trans, 0, dst=None)
        img_rgb = cv.cvtColor(img_flip, cv.COLOR_GRAY2RGB)
        x = img_rgb.shape[1]
        y = img_rgb.shape[0]
        print(x, y)
        img_rgb[:, :, 0] = np.zeros([y, x], self.img.dtype)
        img_rgb[:, :, 2] = np.zeros([y, x], self.img.dtype)
        frame = QImage(img_rgb, x, y, QImage.Format_RGB888)
        pix = QPixmap.fromImage(frame)
        self.item = QGraphicsPixmapItem(pix)
        self.scene = QGraphicsScene()
        self.scene.addItem(self.item)
        self.graphicsView.setScene(self.scene)

        # print(img_rgb)
        # print(img_rgb.shape)
        # cv.imshow('img_rgb', img_rgb)
        # cv.waitKey(0)
        # cv.destroyAllWindows()


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    window = Analyzer()
    window.show()
    sys.exit(app.exec_())
