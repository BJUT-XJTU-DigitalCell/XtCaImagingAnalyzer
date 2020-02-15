from PyQt5.Qt import *
from resource.set_parameters import Ui_Dialog


class SetParameters(QDialog, Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    window = SetParameters()
    window.show()
    sys.exit(app.exec_())
