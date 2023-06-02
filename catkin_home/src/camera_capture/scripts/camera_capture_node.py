#!/usr/bin/env python3

import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2

def capture_image():
    """
    Function to capture images from a camera and publish them as ROS Image messages.
    """

    rospy.init_node('camera_capture_node', anonymous=True)
    image_pub = rospy.Publisher('captured_image', Image, queue_size=10)
    bridge = CvBridge()

    camera = cv2.VideoCapture(0)  # Open the camera

    rate = rospy.Rate(10)  # Publishing rate in Hz

    while not rospy.is_shutdown():
        ret, frame = camera.read()  # Read a frame from the camera

        if ret:
            # Convert OpenCV image to ROS message
            image_msg = bridge.cv2_to_imgmsg(frame, encoding="bgr8")

            # Publica la imagen capturada
            image_pub.publish(image_msg)

        rate.sleep()

    camera.release()  # Releases the camera when the node stops

if __name__ == '__main__':
    """
    Función principal del programa.

    Inicia el nodo y llama a la función capture_image().
    """

    print("Running") 
    try:
        capture_image()
    except rospy.ROSInterruptException:
        pass
