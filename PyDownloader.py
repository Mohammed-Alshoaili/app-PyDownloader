from PyQt5 import QtCore, QtGui, QtWidgets
from main import Ui_MainWindow
import sys
import pafy


app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()




def save_location():
    save = QtWidgets.QFileDialog.getExistingDirectory(MainWindow , "Save_location")
    ui.lineEdit_2.setText(save)


def Download():
    video_link = ui.lineEdit.text()
    save_location = ui.lineEdit_2.text()
    video = pafy.new(video_link)
    best = video.getbest()
    best.download(save_location)




ui.pushButton.clicked.connect(save_location)
ui.pushButton_2.clicked.connect(Download)























sys.exit(app.exec_())