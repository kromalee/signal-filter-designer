from PyQt5 import QtCore, QtGui, QtWidgets
from src.main_window_controller import MainWindow
import sys

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    # 类 MainWindow 的实例化
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())
