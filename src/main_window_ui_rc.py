# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window_ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(1366, 768)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(mainWindow.sizePolicy().hasHeightForWidth())
        mainWindow.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setBold(False)
        font.setWeight(50)
        mainWindow.setFont(font)
        mainWindow.setAutoFillBackground(False)
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName("groupBox_2")
        self.phaseResponse = PlotWidget(self.groupBox_2)
        self.phaseResponse.setGeometry(QtCore.QRect(20, 30, 411, 321))
        self.phaseResponse.setObjectName("phaseResponse")
        self.gridLayout_2.addWidget(self.groupBox_2, 1, 1, 1, 1)
        self.ana = QtWidgets.QGroupBox(self.centralwidget)
        self.ana.setObjectName("ana")
        self.label_27 = QtWidgets.QLabel(self.ana)
        self.label_27.setGeometry(QtCore.QRect(511, 33, 16, 18))
        self.label_27.setText("")
        self.label_27.setObjectName("label_27")
        self.line = QtWidgets.QFrame(self.ana)
        self.line.setGeometry(QtCore.QRect(1017, 21, 16, 309))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.amplitudeResponse = PlotWidget(self.ana)
        self.amplitudeResponse.setGeometry(QtCore.QRect(10, 30, 421, 321))
        self.amplitudeResponse.setObjectName("amplitudeResponse")
        self.gridLayout_2.addWidget(self.ana, 1, 2, 1, 1)
        self.design = QtWidgets.QGroupBox(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setBold(False)
        font.setWeight(50)
        self.design.setFont(font)
        self.design.setObjectName("design")
        self.gridLayout = QtWidgets.QGridLayout(self.design)
        self.gridLayout.setObjectName("gridLayout")
        self.optionalSet = QtWidgets.QGroupBox(self.design)
        self.optionalSet.setObjectName("optionalSet")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.optionalSet)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.windowTypeInput = QtWidgets.QComboBox(self.optionalSet)
        self.windowTypeInput.setObjectName("windowTypeInput")
        self.windowTypeInput.addItem("")
        self.windowTypeInput.addItem("")
        self.windowTypeInput.addItem("")
        self.windowTypeInput.addItem("")
        self.windowTypeInput.addItem("")
        self.gridLayout_4.addWidget(self.windowTypeInput, 1, 1, 1, 1)
        self.windowTypeLabel = QtWidgets.QLabel(self.optionalSet)
        self.windowTypeLabel.setObjectName("windowTypeLabel")
        self.gridLayout_4.addWidget(self.windowTypeLabel, 1, 0, 1, 1)
        self.betaInput = QtWidgets.QDoubleSpinBox(self.optionalSet)
        self.betaInput.setMaximum(1.0)
        self.betaInput.setProperty("value", 0.05)
        self.betaInput.setObjectName("betaInput")
        self.gridLayout_4.addWidget(self.betaInput, 2, 1, 1, 1)
        self.betaLabel = QtWidgets.QLabel(self.optionalSet)
        self.betaLabel.setObjectName("betaLabel")
        self.gridLayout_4.addWidget(self.betaLabel, 2, 0, 1, 1)
        self.scaleInput = QtWidgets.QCheckBox(self.optionalSet)
        self.scaleInput.setObjectName("scaleInput")
        self.gridLayout_4.addWidget(self.scaleInput, 0, 0, 1, 2)
        self.gridLayout.addWidget(self.optionalSet, 0, 1, 1, 1)
        self.fSet = QtWidgets.QGroupBox(self.design)
        self.fSet.setObjectName("fSet")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.fSet)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.fe3Label = QtWidgets.QLabel(self.fSet)
        self.fe3Label.setObjectName("fe3Label")
        self.gridLayout_5.addWidget(self.fe3Label, 8, 0, 1, 1)
        self.fsLabel = QtWidgets.QLabel(self.fSet)
        self.fsLabel.setObjectName("fsLabel")
        self.gridLayout_5.addWidget(self.fsLabel, 1, 0, 1, 1)
        self.fe4Input = QtWidgets.QSpinBox(self.fSet)
        self.fe4Input.setMaximum(4000)
        self.fe4Input.setProperty("value", 1600)
        self.fe4Input.setObjectName("fe4Input")
        self.gridLayout_5.addWidget(self.fe4Input, 9, 1, 1, 1)
        self.fe1Input = QtWidgets.QSpinBox(self.fSet)
        self.fe1Input.setMaximum(4000)
        self.fe1Input.setProperty("value", 160)
        self.fe1Input.setObjectName("fe1Input")
        self.gridLayout_5.addWidget(self.fe1Input, 6, 1, 1, 1)
        self.fe3Input = QtWidgets.QSpinBox(self.fSet)
        self.fe3Input.setMaximum(4000)
        self.fe3Input.setProperty("value", 1500)
        self.fe3Input.setObjectName("fe3Input")
        self.gridLayout_5.addWidget(self.fe3Input, 8, 1, 1, 1)
        self.fc2Label = QtWidgets.QLabel(self.fSet)
        self.fc2Label.setObjectName("fc2Label")
        self.gridLayout_5.addWidget(self.fc2Label, 3, 0, 1, 1)
        self.fc1Label = QtWidgets.QLabel(self.fSet)
        self.fc1Label.setObjectName("fc1Label")
        self.gridLayout_5.addWidget(self.fc1Label, 2, 0, 1, 1)
        self.fc2Input = QtWidgets.QSpinBox(self.fSet)
        self.fc2Input.setMaximum(4000)
        self.fc2Input.setProperty("value", 1000)
        self.fc2Input.setObjectName("fc2Input")
        self.gridLayout_5.addWidget(self.fc2Input, 3, 1, 1, 1)
        self.fe4Label = QtWidgets.QLabel(self.fSet)
        self.fe4Label.setObjectName("fe4Label")
        self.gridLayout_5.addWidget(self.fe4Label, 9, 0, 1, 1)
        self.fe1Label = QtWidgets.QLabel(self.fSet)
        self.fe1Label.setObjectName("fe1Label")
        self.gridLayout_5.addWidget(self.fe1Label, 6, 0, 1, 1)
        self.fe2Label = QtWidgets.QLabel(self.fSet)
        self.fe2Label.setObjectName("fe2Label")
        self.gridLayout_5.addWidget(self.fe2Label, 7, 0, 1, 1)
        self.fsInput = QtWidgets.QSpinBox(self.fSet)
        self.fsInput.setMaximum(100000)
        self.fsInput.setProperty("value", 8000)
        self.fsInput.setObjectName("fsInput")
        self.gridLayout_5.addWidget(self.fsInput, 1, 1, 1, 1)
        self.labelForFUnit = QtWidgets.QLabel(self.fSet)
        self.labelForFUnit.setObjectName("labelForFUnit")
        self.gridLayout_5.addWidget(self.labelForFUnit, 0, 0, 1, 1)
        self.fUnitSelect = QtWidgets.QComboBox(self.fSet)
        self.fUnitSelect.setObjectName("fUnitSelect")
        self.fUnitSelect.addItem("")
        self.gridLayout_5.addWidget(self.fUnitSelect, 0, 1, 1, 1)
        self.fe2Input = QtWidgets.QSpinBox(self.fSet)
        self.fe2Input.setMaximum(4000)
        self.fe2Input.setProperty("value", 240)
        self.fe2Input.setObjectName("fe2Input")
        self.gridLayout_5.addWidget(self.fe2Input, 7, 1, 1, 1)
        self.fc1Input = QtWidgets.QSpinBox(self.fSet)
        self.fc1Input.setMaximum(4000)
        self.fc1Input.setProperty("value", 200)
        self.fc1Input.setObjectName("fc1Input")
        self.gridLayout_5.addWidget(self.fc1Input, 2, 1, 1, 1)
        self.feLabel = QtWidgets.QLabel(self.fSet)
        self.feLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.feLabel.setObjectName("feLabel")
        self.gridLayout_5.addWidget(self.feLabel, 5, 0, 1, 1)
        self.gridLayout.addWidget(self.fSet, 0, 2, 1, 1)
        self.aSet = QtWidgets.QGroupBox(self.design)
        self.aSet.setEnabled(True)
        self.aSet.setObjectName("aSet")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.aSet)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.rpLabel = QtWidgets.QLabel(self.aSet)
        self.rpLabel.setObjectName("rpLabel")
        self.gridLayout_6.addWidget(self.rpLabel, 2, 0, 1, 1)
        self.aUnitSelect = QtWidgets.QComboBox(self.aSet)
        self.aUnitSelect.setObjectName("aUnitSelect")
        self.aUnitSelect.addItem("")
        self.gridLayout_6.addWidget(self.aUnitSelect, 0, 1, 1, 1)
        self.rsInput = QtWidgets.QSpinBox(self.aSet)
        self.rsInput.setMinimum(0)
        self.rsInput.setMaximum(100)
        self.rsInput.setProperty("value", 60)
        self.rsInput.setObjectName("rsInput")
        self.gridLayout_6.addWidget(self.rsInput, 3, 1, 1, 1)
        self.labelForAUnit = QtWidgets.QLabel(self.aSet)
        self.labelForAUnit.setObjectName("labelForAUnit")
        self.gridLayout_6.addWidget(self.labelForAUnit, 0, 0, 1, 1)
        self.rsLabel = QtWidgets.QLabel(self.aSet)
        self.rsLabel.setObjectName("rsLabel")
        self.gridLayout_6.addWidget(self.rsLabel, 3, 0, 1, 1)
        self.rpInput = QtWidgets.QDoubleSpinBox(self.aSet)
        self.rpInput.setProperty("value", 1.0)
        self.rpInput.setObjectName("rpInput")
        self.gridLayout_6.addWidget(self.rpInput, 2, 1, 1, 1)
        self.gridLayout.addWidget(self.aSet, 0, 3, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(self.design)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.orderTypeLabel = QtWidgets.QLabel(self.groupBox)
        self.orderTypeLabel.setObjectName("orderTypeLabel")
        self.gridLayout_3.addWidget(self.orderTypeLabel, 2, 2, 1, 1)
        self.orderTypeInput = QtWidgets.QComboBox(self.groupBox)
        self.orderTypeInput.setObjectName("orderTypeInput")
        self.orderTypeInput.addItem("")
        self.orderTypeInput.addItem("")
        self.gridLayout_3.addWidget(self.orderTypeInput, 2, 4, 1, 1)
        self.responseTypeLabel = QtWidgets.QLabel(self.groupBox)
        self.responseTypeLabel.setObjectName("responseTypeLabel")
        self.gridLayout_3.addWidget(self.responseTypeLabel, 0, 2, 1, 1)
        self.designMethodInput = QtWidgets.QComboBox(self.groupBox)
        self.designMethodInput.setObjectName("designMethodInput")
        self.designMethodInput.addItem("")
        self.designMethodInput.addItem("")
        self.designMethodInput.addItem("")
        self.designMethodInput.addItem("")
        self.designMethodInput.addItem("")
        self.gridLayout_3.addWidget(self.designMethodInput, 1, 4, 1, 1)
        self.orderInput = QtWidgets.QSpinBox(self.groupBox)
        self.orderInput.setMaximum(999)
        self.orderInput.setProperty("value", 10)
        self.orderInput.setObjectName("orderInput")
        self.gridLayout_3.addWidget(self.orderInput, 2, 5, 1, 1)
        self.impulseResponseTypeLabel = QtWidgets.QLabel(self.groupBox)
        self.impulseResponseTypeLabel.setObjectName("impulseResponseTypeLabel")
        self.gridLayout_3.addWidget(self.impulseResponseTypeLabel, 1, 5, 1, 1, QtCore.Qt.AlignRight)
        self.designMethodLabel = QtWidgets.QLabel(self.groupBox)
        self.designMethodLabel.setObjectName("designMethodLabel")
        self.gridLayout_3.addWidget(self.designMethodLabel, 1, 2, 1, 1)
        self.responseTypeInput = QtWidgets.QComboBox(self.groupBox)
        self.responseTypeInput.setObjectName("responseTypeInput")
        self.responseTypeInput.addItem("")
        self.responseTypeInput.addItem("")
        self.responseTypeInput.addItem("")
        self.responseTypeInput.addItem("")
        self.gridLayout_3.addWidget(self.responseTypeInput, 0, 4, 1, 1)
        self.doDesign = QtWidgets.QPushButton(self.groupBox)
        self.doDesign.setObjectName("doDesign")
        self.gridLayout_3.addWidget(self.doDesign, 3, 4, 1, 1)
        self.doTest = QtWidgets.QPushButton(self.groupBox)
        self.doTest.setObjectName("doTest")
        self.gridLayout_3.addWidget(self.doTest, 3, 5, 1, 1)
        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.design, 0, 0, 1, 3)
        self.info = QtWidgets.QGroupBox(self.centralwidget)
        self.info.setFlat(False)
        self.info.setCheckable(False)
        self.info.setObjectName("info")
        self.scrollArea = QtWidgets.QScrollArea(self.info)
        self.scrollArea.setGeometry(QtCore.QRect(0, 30, 441, 321))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.scrollArea.setFont(font)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 439, 319))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.orderResultLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.orderResultLabel.setGeometry(QtCore.QRect(60, 30, 381, 16))
        self.orderResultLabel.setObjectName("orderResultLabel")
        self.label_3 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_3.setGeometry(QtCore.QRect(9, 30, 51, 18))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label.setGeometry(QtCore.QRect(10, 110, 31, 17))
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.goodLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.goodLabel.setGeometry(QtCore.QRect(60, 80, 331, 71))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.goodLabel.sizePolicy().hasHeightForWidth())
        self.goodLabel.setSizePolicy(sizePolicy)
        self.goodLabel.setTextFormat(QtCore.Qt.AutoText)
        self.goodLabel.setWordWrap(True)
        self.goodLabel.setObjectName("goodLabel")
        self.label_4 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_4.setGeometry(QtCore.QRect(10, 190, 24, 18))
        self.label_4.setObjectName("label_4")
        self.label_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_2.setGeometry(QtCore.QRect(10, 270, 24, 18))
        self.label_2.setObjectName("label_2")
        self.badLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.badLabel.setGeometry(QtCore.QRect(60, 150, 341, 81))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.badLabel.sizePolicy().hasHeightForWidth())
        self.badLabel.setSizePolicy(sizePolicy)
        self.badLabel.setWordWrap(True)
        self.badLabel.setObjectName("badLabel")
        self.featureLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.featureLabel.setGeometry(QtCore.QRect(60, 240, 351, 71))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.featureLabel.sizePolicy().hasHeightForWidth())
        self.featureLabel.setSizePolicy(sizePolicy)
        self.featureLabel.setWordWrap(True)
        self.featureLabel.setObjectName("featureLabel")
        self.label_5 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_5.setGeometry(QtCore.QRect(10, 10, 41, 18))
        self.label_5.setObjectName("label_5")
        self.nameLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.nameLabel.setGeometry(QtCore.QRect(60, 10, 371, 18))
        self.nameLabel.setObjectName("nameLabel")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout_2.addWidget(self.info, 1, 0, 1, 1)
        mainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(mainWindow)
        self.statusbar.setObjectName("statusbar")
        mainWindow.setStatusBar(self.statusbar)
        self.windowTypeLabel.setBuddy(self.windowTypeInput)
        self.betaLabel.setBuddy(self.betaInput)
        self.fe3Label.setBuddy(self.fe3Input)
        self.fsLabel.setBuddy(self.fsInput)
        self.fc2Label.setBuddy(self.fc2Input)
        self.fc1Label.setBuddy(self.fc1Input)
        self.fe4Label.setBuddy(self.fe4Input)
        self.fe1Label.setBuddy(self.fe1Input)
        self.fe2Label.setBuddy(self.fe2Input)
        self.labelForFUnit.setBuddy(self.fUnitSelect)
        self.labelForAUnit.setBuddy(self.aUnitSelect)
        self.rsLabel.setBuddy(self.rsInput)

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "??????????????????"))
        self.groupBox_2.setTitle(_translate("mainWindow", "????????????"))
        self.ana.setTitle(_translate("mainWindow", "????????????"))
        self.design.setTitle(_translate("mainWindow", "???????????????"))
        self.optionalSet.setTitle(_translate("mainWindow", "????????????"))
        self.windowTypeInput.setItemText(0, _translate("mainWindow", "Kaiser"))
        self.windowTypeInput.setItemText(1, _translate("mainWindow", "?????????"))
        self.windowTypeInput.setItemText(2, _translate("mainWindow", "Hann"))
        self.windowTypeInput.setItemText(3, _translate("mainWindow", "Hamming"))
        self.windowTypeInput.setItemText(4, _translate("mainWindow", "Blackman"))
        self.windowTypeLabel.setText(_translate("mainWindow", "???"))
        self.betaLabel.setText(_translate("mainWindow", "Kaiser ??"))
        self.scaleInput.setText(_translate("mainWindow", "????????????"))
        self.fSet.setTitle(_translate("mainWindow", "????????????"))
        self.fe3Label.setText(_translate("mainWindow", "?????????3"))
        self.fsLabel.setText(_translate("mainWindow", "????????????"))
        self.fc2Label.setText(_translate("mainWindow", "????????????2"))
        self.fc1Label.setText(_translate("mainWindow", "????????????1"))
        self.fe4Label.setText(_translate("mainWindow", "?????????4"))
        self.fe1Label.setText(_translate("mainWindow", "?????????1"))
        self.fe2Label.setText(_translate("mainWindow", "?????????2"))
        self.labelForFUnit.setText(_translate("mainWindow", "??????"))
        self.fUnitSelect.setItemText(0, _translate("mainWindow", "Hz"))
        self.feLabel.setText(_translate("mainWindow", "??????/??????????????????"))
        self.aSet.setTitle(_translate("mainWindow", "????????????"))
        self.rpLabel.setText(_translate("mainWindow", "??????????????????"))
        self.aUnitSelect.setItemText(0, _translate("mainWindow", "dB"))
        self.labelForAUnit.setText(_translate("mainWindow", "??????"))
        self.rsLabel.setText(_translate("mainWindow", "??????????????????"))
        self.groupBox.setTitle(_translate("mainWindow", "????????????"))
        self.orderTypeLabel.setText(_translate("mainWindow", "??????"))
        self.orderTypeInput.setItemText(0, _translate("mainWindow", "????????????"))
        self.orderTypeInput.setItemText(1, _translate("mainWindow", "????????????"))
        self.responseTypeLabel.setText(_translate("mainWindow", "????????????"))
        self.designMethodInput.setItemText(0, _translate("mainWindow", "ButterWorth"))
        self.designMethodInput.setItemText(1, _translate("mainWindow", "Chebyshev I "))
        self.designMethodInput.setItemText(2, _translate("mainWindow", "Chebyshev II "))
        self.designMethodInput.setItemText(3, _translate("mainWindow", "Cauer/elliptic"))
        self.designMethodInput.setItemText(4, _translate("mainWindow", "Window"))
        self.impulseResponseTypeLabel.setText(_translate("mainWindow", "IIR"))
        self.designMethodLabel.setText(_translate("mainWindow", "????????????"))
        self.responseTypeInput.setItemText(0, _translate("mainWindow", "??????"))
        self.responseTypeInput.setItemText(1, _translate("mainWindow", "??????"))
        self.responseTypeInput.setItemText(2, _translate("mainWindow", "??????"))
        self.responseTypeInput.setItemText(3, _translate("mainWindow", "??????"))
        self.doDesign.setText(_translate("mainWindow", "??????"))
        self.doTest.setText(_translate("mainWindow", "??????"))
        self.info.setTitle(_translate("mainWindow", "???????????????"))
        self.orderResultLabel.setText(_translate("mainWindow", "?????????????????????"))
        self.label_3.setText(_translate("mainWindow", "??????"))
        self.label.setText(_translate("mainWindow", "??????"))
        self.goodLabel.setText(_translate("mainWindow", "?????????????????????"))
        self.label_4.setText(_translate("mainWindow", "??????"))
        self.label_2.setText(_translate("mainWindow", "??????"))
        self.badLabel.setText(_translate("mainWindow", "?????????????????????"))
        self.featureLabel.setText(_translate("mainWindow", "?????????????????????"))
        self.label_5.setText(_translate("mainWindow", "??????"))
        self.nameLabel.setText(_translate("mainWindow", "?????????????????????"))

from pyqtgraph import PlotWidget
