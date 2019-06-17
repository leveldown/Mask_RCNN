# *-*encoding:utf-8
import sys
import time
from PyQt5.QtCore import pyqtSignal
from UI import untitled
from UI import result
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtGui import QPixmap
import erosion_demo
from erosion_demo import detection
from PyQt5.QtCore import QBasicTimer
from PyQt5.QtCore import QThread


class Mywindow(QtWidgets.QMainWindow, untitled.Ui_MainWindow):

    def __init__(self, parent=None):
        # super(Mywindow, self).__init__()
        QtWidgets.QMainWindow.__init__(self, parent)
        self.setupUi(self)
        self.pbar = self.progressBar
        self.timer = QBasicTimer()  # 初始化一个时钟
        self.step = 0  # 进度条的值
        self.pbar.setValue(0)

    def view(self):
        file, filetype = QtWidgets.QFileDialog.getOpenFileName\
         (self, "open file", "E:/Anaconda/Python_workspace", "JPG Files (*.jpg);;PNG Files (*.png);;BMP Files (*.bmp)")
        self.lineEdit.setText(str(file))

    def test(self):
        self.timer.start(200, self)  # 启动QBasicTimer，每200ms调用一次事件回调函数
        self.thread = Example()
        self.thread.start()
        self.thread.signal.connect(self.callback)

    def callback(self):
        self.pbar.setValue(100)
        pix = QPixmap('E:/Anaconda/Python_workspace/Mask_RCNN/UI/test.png')
        child.show()
        child.label.setPixmap(pix)
        child.label.setScaledContents(True)

    def timerEvent(self, a0: 'QTimerEvent'):
        # 把进度条每次充值的值赋给进度条
        self.pbar.setValue(self.step)
        if self.step == 99:
            # 停止进度条
            self.timer.stop()
            self.step = 0
            return
        # 把进度条卡在99，等处理好了再到100
        if self.step < 99:
            self.step += 1


class Example(QThread):
    signal = pyqtSignal()

    def __init__(self):
        super().__init__()

    def run(self):
        path = window.lineEdit.text()
        start = time.clock()
        detection(str(path))
        end = time.clock()
        time_used = end - start
        window.lineEdit_2.setText(str(time_used))
        self.signal.emit()


class ChildWindow(QtWidgets.QDialog, result.Ui_Dialog):
    def __init__(self, parent=None):
        QtWidgets.QDialog.__init__(self, parent)
        self.setupUi(self)


app = QtWidgets.QApplication(sys.argv)
window = Mywindow()
child = ChildWindow()

# window.resize(700, 600)
window.show()
sys.exit(app.exec_())
