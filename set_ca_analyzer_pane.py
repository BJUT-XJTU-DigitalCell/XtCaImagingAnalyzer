from PyQt5.Qt import *
from resource.set_ca_analyzer import Ui_Form


class SetAnalyzer(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.data_type = "XT"
        self.signal_type = None

    def select_data_type(self, current_no):
        print(self.sender().tabText(current_no))
        self.data_type = self.sender().tabText(current_no)
        self.signal_type = None
        print(self.data_type)
        print(self.signal_type)

    def select_signal_type(self):
        self.signal_type = self.sender().text()
        print(self.signal_type)
        print(self.data_type)

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

    def select_analyze_mode(self):
        print(type(self.sender().text()))

    def open_file(self):
        file_dialog = QFileDialog(self)
        file_dialog.setAcceptMode(QFileDialog.AcceptOpen)
        file_dialog.setFileMode(QFileDialog.ExistingFiles)
        # file_dialog.setNameFilter("Images(*.tiff)")
        file_dialog.setViewMode(QFileDialog.Detail)

        def execute_analyzer(files):
            print(files)

        file_dialog.filesSelected.connect(execute_analyzer)
        file_dialog.open()


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    window = SetAnalyzer()
    window.show()
    sys.exit(app.exec_())
