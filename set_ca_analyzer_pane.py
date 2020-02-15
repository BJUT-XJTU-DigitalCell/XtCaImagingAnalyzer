from PyQt5.Qt import *
from resource.set_ca_analyzer import Ui_Form


class SetAnalyzer(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def select_all_channel(self):
        self.change_channel(False, True)

    def manual_by_files(self):
        self.change_channel(False, False)

    def specified_by_laser(self):
        self.change_channel(True)

    def change_channel(self, enable, checked=False):
        self.checkBox.setEnabled(enable)
        self.checkBox.setChecked(checked)
        self.checkBox_2.setEnabled(enable)
        self.checkBox_2.setChecked(checked)
        self.checkBox_3.setEnabled(enable)
        self.checkBox_3.setChecked(checked)
        self.checkBox_4.setEnabled(enable)
        self.checkBox_4.setChecked(checked)
        self.checkBox_5.setEnabled(enable)
        self.checkBox_5.setChecked(checked)
        self.checkBox_6.setEnabled(enable)
        self.checkBox_6.setChecked(checked)
        self.checkBox_7.setEnabled(enable)
        self.checkBox_7.setChecked(checked)
        self.checkBox_8.setEnabled(enable)
        self.checkBox_8.setChecked(checked)
        self.checkBox_9.setEnabled(enable)
        self.checkBox_9.setChecked(checked)
        self.checkBox_10.setEnabled(enable)
        self.checkBox_10.setChecked(checked)


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    window = SetAnalyzer()
    window.show()
    sys.exit(app.exec_())
