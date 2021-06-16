import sys

from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from PyQt5 import uic


import imugl
import ctrlros

form_class = uic.loadUiType("ngv.ui")[0]

class WindowClass(QMainWindow, form_class) :
	
	def __init__(self) :
		super(WindowClass, self).__init__()
		self.setupUi(self)
		self.imu_widget = imugl.ImuGL()
		self.imu_layout.addWidget(self.imu_widget)
		self.ctrlros = ctrlros.CtrlRos()
		self.ctrlros.sendQE.connect(self.updateQE)

		self.imu_widget.show()

	@pyqtSlot(object, object )
	def updateQE(self, quaternion, euler):
		quat_txt = "x : {}  y : {}  z : {}  w : {}".format(round(quaternion[0],4), round(quaternion[1],4), round(quaternion[2],4), round(quaternion[3],4))
		self.quat_label.setText(quat_txt)
		eul_txt = "X : {}  Y : {}  Z : {}".format(round(euler[1],4), round(euler[0],4), round(euler[2],4))
		self.eul_label.setText(eul_txt)

if __name__ == "__main__" :
	app = QApplication(sys.argv)
	myWindow = WindowClass()
	myWindow.show()
	app.exec_()