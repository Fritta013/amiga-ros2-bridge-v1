# amiga-ros2-bridge-v1

Changes made: 


*I got rid of all the files are not essential to run the pkg 
*I deleted the cmake file because according to ros2 humble official page, Python packages in ROS 2 do not use CMake, so delete the CMakeLists.txt. However i put it outside of src folder just in case (it's been adjusted to ros2) 
*Added setup.py, essential for ros2 
*Added setup.cfg file essential for ros2 
*Replace all the loginfo with node.get_logger().info(
*Change subscriber to fit ros2 again swapping name and type of topic 
*Edited the launch files 
*edited package.xml to fit ros2 requirements 
*In src/twist_control.py, replacing 
        rospy.init_node("amiga_twist_control") with 
        rclpy.init()
        node = rclpy.create_node("amiga_twist_control")
In src/farmng_ros_pipelines.py, replacing rospy.Publisher(topic, ros_msg_type, queue_size=10) with node.create_publisher(ros_msg_type, queue_size=10, topic), changing the publisher arguments order (between ros1 and ros2 type and name of topic are swapped) BUT order should be verified across the other py files in the same dir 
In src/amiga_streams.py, replacing 
        rospy.init_node("amiga_streams_node") with 
        rclpy.init()
        node = rclpy.create_node("amiga_streams_node")


