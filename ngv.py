import sys

from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from PyQt5 import uic


import imugl

form_class = uic.loadUiType("ngv.ui")[0]

class WindowClass(QMainWindow, form_class) :
	
	def __init__(self) :
		super(WindowClass, self).__init__()
		self.setupUi(self)
		self.imu_widget = imugl.ImuGL()
		self.imu_layout.addWidget(self.imu_widget)
		self.imu_widget.show()


if __name__ == "__main__" :
	app = QApplication(sys.argv)
	myWindow = WindowClass()
	myWindow.show()
	app.exec_()