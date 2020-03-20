from ca_analyzer_pane import Analyzer
from set_ca_analyzer_pane import SetAnalyzer
from PyQt5.Qt import *

if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    set_analyzer = SetAnalyzer()
    analyzer = Analyzer()


    def open_analyzer(files, files_num, file_no, data_type, signal_type, analyze_mode, channels):
        analyzer.show()
        set_analyzer.hide()
        analyzer.xt_analyzer(files, files_num, file_no, data_type, signal_type, analyze_mode, channels)


    set_analyzer.open_analyzer_signal.connect(open_analyzer)
    set_analyzer.show()
    sys.exit(app.exec_())
