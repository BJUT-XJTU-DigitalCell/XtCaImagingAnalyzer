from ca_analyzer_pane import Analyzer
from set_ca_analyzer_pane import SetAnalyzer
from PyQt5.Qt import *

if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    set_analyzer = SetAnalyzer()
    analyzer = Analyzer()


    def open_analyzer(files, files_num, file_no, data_type, signal_type, analyze_mode, channels):
        print(files)
        print(files_num)
        print(file_no)
        print(data_type)
        print(signal_type)
        print(analyze_mode)
        print(channels)
        analyzer.show()
        set_analyzer.hide()


    set_analyzer.open_analyzer_signal.connect(open_analyzer)
    set_analyzer.show()
    sys.exit(app.exec_())
