# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'set_ca_analyzer.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(439, 445)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 2, 0, 1, 2, QtCore.Qt.AlignHCenter)
        self.tabWidget = QtWidgets.QTabWidget(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tab.sizePolicy().hasHeightForWidth())
        self.tab.setSizePolicy(sizePolicy)
        self.tab.setObjectName("tab")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout.setObjectName("verticalLayout")
        self.radioButton = QtWidgets.QRadioButton(self.tab)
        self.radioButton.setObjectName("radioButton")
        self.verticalLayout.addWidget(self.radioButton)
        self.radioButton_2 = QtWidgets.QRadioButton(self.tab)
        self.radioButton_2.setObjectName("radioButton_2")
        self.verticalLayout.addWidget(self.radioButton_2)
        self.radioButton_3 = QtWidgets.QRadioButton(self.tab)
        self.radioButton_3.setObjectName("radioButton_3")
        self.verticalLayout.addWidget(self.radioButton_3)
        self.radioButton_4 = QtWidgets.QRadioButton(self.tab)
        self.radioButton_4.setObjectName("radioButton_4")
        self.verticalLayout.addWidget(self.radioButton_4)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.tab_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.radioButton_5 = QtWidgets.QRadioButton(self.tab_2)
        self.radioButton_5.setObjectName("radioButton_5")
        self.verticalLayout_2.addWidget(self.radioButton_5)
        self.radioButton_6 = QtWidgets.QRadioButton(self.tab_2)
        self.radioButton_6.setObjectName("radioButton_6")
        self.verticalLayout_2.addWidget(self.radioButton_6)
        self.radioButton_7 = QtWidgets.QRadioButton(self.tab_2)
        self.radioButton_7.setObjectName("radioButton_7")
        self.verticalLayout_2.addWidget(self.radioButton_7)
        self.radioButton_8 = QtWidgets.QRadioButton(self.tab_2)
        self.radioButton_8.setObjectName("radioButton_8")
        self.verticalLayout_2.addWidget(self.radioButton_8)
        self.tabWidget.addTab(self.tab_2, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)
        self.widget_2 = QtWidgets.QWidget(Form)
        self.widget_2.setObjectName("widget_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget_2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.widget_2)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_3.addWidget(self.label_2)
        self.widget_3 = QtWidgets.QWidget(self.widget_2)
        self.widget_3.setObjectName("widget_3")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.widget_3)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.radioButton_11 = QtWidgets.QRadioButton(self.widget_3)
        self.radioButton_11.setObjectName("radioButton_11")
        self.verticalLayout_5.addWidget(self.radioButton_11)
        self.radioButton_12 = QtWidgets.QRadioButton(self.widget_3)
        self.radioButton_12.setObjectName("radioButton_12")
        self.verticalLayout_5.addWidget(self.radioButton_12)
        self.radioButton_13 = QtWidgets.QRadioButton(self.widget_3)
        self.radioButton_13.setObjectName("radioButton_13")
        self.verticalLayout_5.addWidget(self.radioButton_13)
        self.verticalLayout_3.addWidget(self.widget_3)
        self.scrollArea = QtWidgets.QScrollArea(self.widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 197, 194))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.checkBox = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkBox.setObjectName("checkBox")
        self.verticalLayout_4.addWidget(self.checkBox)
        self.checkBox_2 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkBox_2.setObjectName("checkBox_2")
        self.verticalLayout_4.addWidget(self.checkBox_2)
        self.checkBox_4 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkBox_4.setObjectName("checkBox_4")
        self.verticalLayout_4.addWidget(self.checkBox_4)
        self.checkBox_3 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkBox_3.setObjectName("checkBox_3")
        self.verticalLayout_4.addWidget(self.checkBox_3)
        self.checkBox_5 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkBox_5.setObjectName("checkBox_5")
        self.verticalLayout_4.addWidget(self.checkBox_5)
        self.checkBox_6 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkBox_6.setObjectName("checkBox_6")
        self.verticalLayout_4.addWidget(self.checkBox_6)
        self.checkBox_7 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkBox_7.setObjectName("checkBox_7")
        self.verticalLayout_4.addWidget(self.checkBox_7)
        self.checkBox_8 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkBox_8.setObjectName("checkBox_8")
        self.verticalLayout_4.addWidget(self.checkBox_8)
        self.checkBox_9 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkBox_9.setObjectName("checkBox_9")
        self.verticalLayout_4.addWidget(self.checkBox_9)
        self.checkBox_10 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkBox_10.setObjectName("checkBox_10")
        self.verticalLayout_4.addWidget(self.checkBox_10)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_3.addWidget(self.scrollArea)
        self.verticalLayout_3.setStretch(0, 1)
        self.verticalLayout_3.setStretch(1, 4)
        self.verticalLayout_3.setStretch(2, 5)
        self.gridLayout.addWidget(self.widget_2, 0, 1, 2, 1)
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setObjectName("widget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 2)
        self.radioButton_9 = QtWidgets.QRadioButton(self.widget)
        self.radioButton_9.setObjectName("radioButton_9")
        self.gridLayout_2.addWidget(self.radioButton_9, 1, 0, 1, 1)
        self.radioButton_10 = QtWidgets.QRadioButton(self.widget)
        self.radioButton_10.setObjectName("radioButton_10")
        self.gridLayout_2.addWidget(self.radioButton_10, 1, 1, 1, 1)
        self.gridLayout.addWidget(self.widget, 1, 0, 1, 1)
        self.gridLayout.setRowStretch(0, 6)
        self.gridLayout.setRowStretch(1, 3)
        self.gridLayout.setRowStretch(2, 1)

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(0)
        self.radioButton_11.toggled['bool'].connect(Form.select_all_channel)
        self.radioButton_12.toggled['bool'].connect(Form.manual_by_files)
        self.radioButton_13.toggled['bool'].connect(Form.specified_by_laser)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "Execute Data Analysis"))
        self.radioButton.setText(_translate("Form", "Ca2+ sparks"))
        self.radioButton_2.setText(_translate("Form", "Ca2+ blinks"))
        self.radioButton_3.setText(_translate("Form", "Ca2+ sparks/blinks"))
        self.radioButton_4.setText(_translate("Form", "Ca2+ translents"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Form", "XT"))
        self.radioButton_5.setText(_translate("Form", "Ca2+ sparks"))
        self.radioButton_6.setText(_translate("Form", "Ca2+ blinks"))
        self.radioButton_7.setText(_translate("Form", "Ca2+ sparks/blinks"))
        self.radioButton_8.setText(_translate("Form", "Ca2+ translents"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Form", "mXT"))
        self.label_2.setText(_translate("Form", "Select Channel"))
        self.radioButton_11.setText(_translate("Form", "Select all"))
        self.radioButton_12.setText(_translate("Form", "Manual by files"))
        self.radioButton_13.setText(_translate("Form", "Specified by laser"))
        self.checkBox.setText(_translate("Form", "405nm"))
        self.checkBox_2.setText(_translate("Form", "445nm"))
        self.checkBox_4.setText(_translate("Form", "458nm"))
        self.checkBox_3.setText(_translate("Form", "488nm"))
        self.checkBox_5.setText(_translate("Form", "514nm"))
        self.checkBox_6.setText(_translate("Form", "532nm"))
        self.checkBox_7.setText(_translate("Form", "543nm"))
        self.checkBox_8.setText(_translate("Form", "555nm"))
        self.checkBox_9.setText(_translate("Form", "663nm"))
        self.checkBox_10.setText(_translate("Form", "transmitted"))
        self.label.setText(_translate("Form", "Analyze mode"))
        self.radioButton_9.setText(_translate("Form", "Auto"))
        self.radioButton_10.setText(_translate("Form", "Manual"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
