#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist

def move_turtle():
    # Initialize the ROS node
    rospy.init_node('move_turtle_node', anonymous=True)
    
    # Create a publisher to send velocity commands to the turtle
    velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    
    # Define the rate at which the loop will run (10 Hz)
    rate = rospy.Rate(10)
    
    # Create a Twist message to set linear and angular velocity
    vel_msg = Twist()

    # Set initial linear velocity (forward speed)
    vel_msg.linear.x = 1.0  # Forward speed
    vel_msg.angular.z = 0.0  # No rotation initially
    
    # Function to move a given distance
    def move_distance(distance):
        # Calculate the travel time based on linear velocity
        travel_time = distance / vel_msg.linear.x
        start_time = rospy.Time.now().to_sec()
        
        while not rospy.is_shutdown():
            current_time = rospy.Time.now().to_sec()
            elapsed_time = current_time - start_time
            
            # Stop when the target distance has been traveled
            if elapsed_time >= travel_time:
                rospy.loginfo(f"Traveled {distance} meters, stopping the turtle.")
                vel_msg.linear.x = 0.0  # Stop forward motion
                velocity_publisher.publish(vel_msg)
                break  # Exit the loop

            # Publish the velocity message
            velocity_publisher.publish(vel_msg)
            rate.sleep()

    # Function to rotate by 90 degrees using a fixed angular velocity
    def turn_90_degrees():
        # Set angular velocity for the turn (turn speed)
        vel_msg.linear.x = 0.0  # No forward movement
        vel_msg.angular.z = 1.0  # Rotate clockwise (change the sign for counterclockwise)
        
        # Calculate the time needed to rotate 90 degrees (pi/2 radians)
        # angular.z = 1 rad/s => it will take pi/2 seconds to rotate 90 degrees
        turn_duration = 1.57 / abs(vel_msg.angular.z)  # 1.57 radians = 90 degrees
        
        start_time = rospy.Time.now().to_sec()
        
        while not rospy.is_shutdown():
            current_time = rospy.Time.now().to_sec()
            elapsed_time = current_time - start_time
            
            # Stop when the 90-degree turn is complete
            if elapsed_time >= turn_duration:
                rospy.loginfo("Completed 90-degree turn, stopping rotation.")
                vel_msg.angular.z = 0.0  # Stop rotation
                velocity_publisher.publish(vel_msg)
                break  # Exit the loop

            # Publish the velocity message for rotation
            velocity_publisher.publish(vel_msg)
            rate.sleep()

    # First movement: Move a specified distance (e.g., 5 meters)
    rospy.loginfo("Starting first movement (length of rectangle).")
    move_distance(5.0)  # Move 5 meters (length of rectangle)
    
    # Second movement: Turn 90 degrees
    rospy.loginfo("Starting 90-degree turn.")
    turn_90_degrees()  # Turn 90 degrees
    
    # Third movement: Move another specified distance (e.g., 3 meters)
    rospy.loginfo("Starting second movement (width of rectangle).")
    vel_msg.linear.x = 1.0  # Reset forward speed before moving
    move_distance(3.0)  # Move 3 meters (width of rectangle)
    
    # Fourth movement: Turn 90 degrees again
    rospy.loginfo("Starting second 90-degree turn.")
    turn_90_degrees()  # Turn 90 degrees again
    
    # Fifth movement: Move the same distance as the first movement (5 meters)
    rospy.loginfo("Starting third movement (length of rectangle).")
    vel_msg.linear.x = 1.0  # Reset forward speed again
    move_distance(5.0)  # Move 5 meters (length of rectangle)
    
    # Sixth movement: Turn 90 degrees to complete the rectangle
    rospy.loginfo("Starting third 90-degree turn.")
    turn_90_degrees()  # Turn 90 degrees
    
    # Seventh movement: Move the same distance as the second movement (3 meters)
    rospy.loginfo("Starting fourth movement (width of rectangle).")
    vel_msg.linear.x = 1.0  # Reset forward speed again
    move_distance(3.0)  # Move 3 meters (width of rectangle)
    
    # Optionally, stop the turtle at the end
    rospy.loginfo("Movement complete.")
    vel_msg.linear.x = 0.0  # Stop forward motion
    velocity_publisher.publish(vel_msg)

if __name__ == '__main__':
    try:
        # Call the function to move the turtle
        move_turtle()
    except rospy.ROSInterruptException:
        pass

