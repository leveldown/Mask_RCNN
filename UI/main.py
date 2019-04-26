# *-*encoding:utf-8
import sys
import cv2
from UI import untitled
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtGui import QPixmap
import erosion_demo
from erosion_demo import detection
from PyQt5.QtWidgets import QFileDialog


class Mywindow(QtWidgets.QMainWindow,untitled.Ui_MainWindow):
    def __init__(self,parent = None):
        # super(Mywindow, self).__init__()
        QtWidgets.QMainWindow.__init__(self,parent)
        self.setupUi(self)

    def show_img(self):
        self.filepath = self.lineEdit.text()
        # pix = QPixmap(self.filepath)
        detection(self.filepath)
        pix = QPixmap('E:/Anaconda/Python_workspace/Mask_RCNN/test.png')
        self.label.setPixmap(pix)
        self.label.setScaledContents(True)


# MAIN
app = QtWidgets.QApplication(sys.argv)
window = Mywindow()
# window.resize(700, 600)
window.show()
sys.exit(app.exec_())
