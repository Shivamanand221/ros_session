#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist

def func1():
	rospy.init_node('robot_cleaner', anonymous=True)
	velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
	vel_msg = Twist()
	print("Shivam Orangewoods task completed. Rectangle made")
	height = 4
	width= 5
	speed = 1
	isForward = 1
	speed = float(speed)
	isForward = int(isForward)
	vel_msg.linear.x = abs(speed)
	vel_msg.linear.y = 0
	vel_msg.linear.z = 0
	vel_msg.angular.x = 0
	vel_msg.angular.y = 0
	vel_msg.angular.z = 0
	count = 0
	while not rospy.is_shutdown():
		if count != 0 :
			break
		t0 = rospy.Time.now().to_sec()
		current_distance = 0
		while(current_distance < height):
			velocity_publisher.publish(vel_msg)
			t1=rospy.Time.now().to_sec()
			current_distance= speed*(t1-t0)
		vel_msg.linear.x = 0
		t0 = rospy.Time.now().to_sec()
		current_distance = 0
		vel_msg.linear.y = abs(speed)
		while(current_distance < width):
			velocity_publisher.publish(vel_msg)
			t1=rospy.Time.now().to_sec()
			current_distance= speed*(t1-t0)
		vel_msg.linear.y = 0
		velocity_publisher.publish(vel_msg)
		t0 = rospy.Time.now().to_sec()
		current_distance = 0
		vel_msg.linear.x = -abs(speed)
		while(current_distance < height):
			velocity_publisher.publish(vel_msg)
			t1=rospy.Time.now().to_sec()
			current_distance= speed*(t1-t0)
		vel_msg.linear.x = 0
		velocity_publisher.publish(vel_msg)		
		t0 = rospy.Time.now().to_sec()
		current_distance = 0
		vel_msg.linear.y = -abs(speed)
		while(current_distance < width):
			velocity_publisher.publish(vel_msg)
			t1=rospy.Time.now().to_sec()
			current_distance= speed*(t1-t0)
		vel_msg.linear.y = 0
		velocity_publisher.publish(vel_msg)
		count+=1

if __name__ == '__main__':
	try:
		func1()
	except rospy. ROSInterruptException: pass

