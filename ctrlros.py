from PyQt5 import QtCore
from PyQt5.QtCore import pyqtSignal, QObject

import rospy
import rospkg
import roslib

from sensor_msgs.msg import Image,CompressedImage
from nav_msgs.msg import Odometry

class CtrlRos(QObject):
	sendRP = pyqtSignal(float, float, float)
	def __init__(self) :
		super(CtrlRos, self).__init__()
		rospy.init_node('visualizer', anonymous=True)
		self.sub_topic()

	def sub_topic(self) :
		rospy.Subscriber('/pose', Odometry, self.imuCallBack)

	def imuCallBack(self, data) :
		"""
		#calculate
		quaternion = (data.orientation.x,data.orientation.y, data.orientation.z,data.orientation.w  )
		euler = tf.transformations.euler_from_quaternion(quaternion)	
		PI = 3.141592
		pitch = round(euler[0]*180/PI, 4)
		roll = round(euler[1]*180/PI, 4)
		yaw = round(euler[2]*180/PI, 4)
		"""
		#test
		roll = data.pose.pose.position.z
		pitch = -data.pose.pose.position.z
		yaw = 0.0
		self.sendRP.emit(roll, pitch, yaw)


