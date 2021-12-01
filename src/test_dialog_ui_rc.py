# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test_dialog_ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1366, 768)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.wavePlot = PlotWidget(Dialog)
        self.wavePlot.setObjectName("wavePlot")
        self.gridLayout.addWidget(self.wavePlot, 0, 0, 1, 2)
        self.wavePlotFAfter = PlotWidget(Dialog)
        self.wavePlotFAfter.setObjectName("wavePlotFAfter")
        self.gridLayout.addWidget(self.wavePlotFAfter, 1, 1, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonBox.sizePolicy().hasHeightForWidth())
        self.buttonBox.setSizePolicy(sizePolicy)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel)
        self.buttonBox.setCenterButtons(False)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 2, 1, 1, 1)
        self.wavePlotFBefore = PlotWidget(Dialog)
        self.wavePlotFBefore.setObjectName("wavePlotFBefore")
        self.gridLayout.addWidget(self.wavePlotFBefore, 1, 0, 1, 1)
        self.path = QtWidgets.QLabel(Dialog)
        self.path.setGeometry(QtCore.QRect(686, 9, 671, 96))
        self.path.setText("")
        self.path.setObjectName("path")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))

from pyqtgraph import PlotWidget
