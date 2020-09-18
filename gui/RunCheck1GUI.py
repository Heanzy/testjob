import sys
import check1GUI
from PyQt5.QtWidgets import QApplication,QMainWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = QMainWindow()
    ui = check1GUI.Ui_MainWindow()
    #向主窗口mainWindow添加控件
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())