from PyQt5.Qt import *
from resource.set_ca_analyzer import Ui_Form


class SetAnalyzer(QWidget, Ui_Form):
    open_analyzer_signal = pyqtSignal(list, int, int, str, str, str, list)

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.files = []
        self.files_num = 0
        self.file_no = 0
        self.data_type = "XT"
        self.signal_type = None
        self.mxt_signal_type = None
        self.xt_signal_type = None
        self.analyze_mode = None
        self.channels = []

    def select_data_type(self, current_no):
        self.data_type = self.sender().tabText(current_no)
        print(self.data_type)
        print("mxt_signal_type", self.mxt_signal_type)
        print("xt_signal_type", self.xt_signal_type)

    def select_xt_signal_type(self):
        self.xt_signal_type = self.sender().text()
        print(self.xt_signal_type)
        print(self.data_type)

    def select_mxt_signal_type(self):
        self.mxt_signal_type = self.sender().text()
        print(self.mxt_signal_type)
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
        self.analyze_mode = self.sender().text()
        print(type(self.sender().text()))
        print(self.sender().text())

    def select_channel(self, checked):
        if checked:
            self.channels.append(self.sender().text())
            print(self.channels)
        else:
            self.channels.remove(self.sender().text())
            print(self.channels)

    def execute_analyzer(self, files):
        self.files = files
        self.files_num = len(files)
        print(self.files)
        print(self.files_num)
        print(self.file_no)
        self.open_analyzer_signal.emit(self.files, self.files_num, self.file_no, self.data_type, self.signal_type, self.analyze_mode, self.channels)

    def open_file(self):
        file_dialog = QFileDialog(self)
        file_dialog.setAcceptMode(QFileDialog.AcceptOpen)
        file_dialog.setFileMode(QFileDialog.ExistingFiles)
        # file_dialog.setNameFilter("Images(*.tiff)")
        file_dialog.setViewMode(QFileDialog.Detail)

        # def execute_analyzer(files):
        #     print(files)
        #     self.open_analyzer_signal.emit()

        file_dialog.filesSelected.connect(self.execute_analyzer)
        file_dialog.open()


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    window = SetAnalyzer()
    window.show()
    sys.exit(app.exec_())
