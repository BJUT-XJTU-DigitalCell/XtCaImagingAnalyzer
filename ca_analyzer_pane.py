from PyQt5.Qt import *
from resource.ca_analyzer import Ui_MainWindow
import cv2 as cv
import numpy as np
from struct import unpack


class Analyzer(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.img = None
        self.h_resolution = 0
        self.v_resolution = 0
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

    def read_resolution(self, file):
        with open(file, 'rb') as file_object:
            file_object.seek(4, 0)
            ifh_offset = unpack("L", file_object.read(4))[0]
            file_object.seek(ifh_offset, 0)
            de_num = unpack("H", file_object.read(2))[0]
            for index in range(de_num):
                de_tag = unpack("H", file_object.read(2))[0]
                if de_tag == 282:
                    file_object.seek(6, 1)
                    h_offset = unpack("L", file_object.read(4))[0]
                    file_object.seek(8, 1)
                    v_offset = unpack("L", file_object.read(4))[0]
                    file_object.seek(h_offset, 0)
                    h_molecule = unpack("L", file_object.read(4))[0]
                    h_denominator = unpack("L", file_object.read(4))[0]
                    file_object.seek(v_offset, 0)
                    v_molecule = unpack("L", file_object.read(4))[0]
                    v_denominator = unpack("L", file_object.read(4))[0]
                    h_resolution = h_molecule / h_denominator
                    v_resolution = v_molecule / v_denominator
                    return h_resolution, v_resolution
                else:
                    file_object.seek(10, 1)

    def change_channel_color(self):
        img_trans = self.img.transpose()
        img_flip = cv.flip(img_trans, 0, dst=None)
        img_rgb = cv.cvtColor(img_flip, cv.COLOR_GRAY2RGB)
        x = img_rgb.shape[1]
        y = img_rgb.shape[0]
        if self.comboBox_3.currentText() == "Red":
            img_rgb[:, :, 1] = np.zeros([y, x], self.img.dtype)
            img_rgb[:, :, 2] = np.zeros([y, x], self.img.dtype)
        elif self.comboBox_3.currentText() == "Green":
            img_rgb[:, :, 0] = np.zeros([y, x], self.img.dtype)
            img_rgb[:, :, 2] = np.zeros([y, x], self.img.dtype)
        elif self.comboBox_3.currentText() == "Blue":
            img_rgb[:, :, 0] = np.zeros([y, x], self.img.dtype)
            img_rgb[:, :, 1] = np.zeros([y, x], self.img.dtype)
        elif self.comboBox_3.currentText() == "Yellow":
            img_rgb[:, :, 2] = np.zeros([y, x], self.img.dtype)
        elif self.comboBox_3.currentText() == "Purple":
            img_rgb[:, :, 1] = np.zeros([y, x], self.img.dtype)
        elif self.comboBox_3.currentText() == "Cyan":
            img_rgb[:, :, 0] = np.zeros([y, x], self.img.dtype)
        elif self.comboBox_3.currentText() == "White":
            pass
        frame = QImage(img_rgb, x, y, QImage.Format_RGB888)
        pix = QPixmap.fromImage(frame)
        self.item = QGraphicsPixmapItem(pix)
        self.scene = QGraphicsScene()
        self.scene.addItem(self.item)
        self.graphicsView.setScene(self.scene)

    def xt_analyzer(self, files, files_num, file_no, data_type, signal_type, analyze_mode, channels):
        cur_file = files[file_no]
        print(cur_file)
        self.h_resolution, self.v_resolution = self.read_resolution(cur_file)
        print(self.h_resolution)
        print(self.v_resolution)
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
