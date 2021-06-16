from PyQt5 import QtCore
from PyQt5.QtCore import pyqtSignal, QObject

import rospy
import rospkg
import roslib
import tf

from sensor_msgs.msg import Image,CompressedImage
from nav_msgs.msg import Odometry
from sensor_msgs.msg import Imu

class CtrlRos(QObject):
	sendRP = pyqtSignal(float, float, float)
	sendQE = pyqtSignal(object, object)

	def __init__(self) :
		super(CtrlRos, self).__init__()
		rospy.init_node('visualizer', anonymous=True)
		self.sub_topic()

	def sub_topic(self) :
		rospy.Subscriber('/pose', Odometry, self.imuCallBack) #Odometry -> IMU


	def imuCallBack(self, data) :
		"""
		#calculate
		quaternion = (data.orientation.x,data.orientation.y, data.orientation.z,data.orientation.w  )
		euler = tf.transformations.euler_from_quaternion(quaternion)	
		PI = 3.141592
		pitch = round(euler[0]*180/PI, 4) #y
		roll = round(euler[1]*180/PI, 4) #x
		yaw = round(euler[2]*180/PI, 4) #z
		"""
		
		#test
		roll = data.pose.pose.position.z
		pitch = -data.pose.pose.position.z
		yaw = 0.0
		quaternion = (data.pose.pose.position.z,-data.pose.pose.position.z,data.pose.pose.position.z,-data.pose.pose.position.z  )
		euler = tf.transformations.euler_from_quaternion(quaternion)	

		self.sendRP.emit(roll, pitch, yaw)
		self.sendQE.emit(quaternion, euler)

