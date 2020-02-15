from PyQt5.Qt import *
from resource.ca_analyzer import Ui_MainWindow


class Analyzer(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    window = Analyzer()
    window.show()
    sys.exit(app.exec_())
