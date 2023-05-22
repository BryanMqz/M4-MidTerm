#!/usr/bin/env python3

import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2

def capture_image():
    """
    Captura imágenes de la cámara y las publica en un nodo de ROS.

    Utiliza la cámara para capturar imágenes, las convierte a un mensaje de ROS
    y las publica en el tópico 'captured_image'.

    Args:
        None

    Returns:
        None
    """

    rospy.init_node('camera_capture_node', anonymous=True)
    image_pub = rospy.Publisher('captured_image', Image, queue_size=10)
    bridge = CvBridge()

    camera = cv2.VideoCapture(0)  # Abre la cámara

    rate = rospy.Rate(10)  # Frecuencia de publicación en Hz

    while not rospy.is_shutdown():
        ret, frame = camera.read()  # Lee un fotograma de la cámara

        if ret:
            # Convierte la imagen de OpenCV a un mensaje de ROS
            image_msg = bridge.cv2_to_imgmsg(frame, encoding="bgr8")

            # Publica la imagen capturada
            image_pub.publish(image_msg)

        rate.sleep()

    camera.release()  # Libera la cámara cuando se detiene el nodo

if __name__ == '__main__':
    """
    Función principal del programa.

    Inicia el nodo y llama a la función capture_image().

    Args:
        None

    Returns:
        None
    """

    print("Running") 
    try:
        capture_image()
    except rospy.ROSInterruptException:
        pass
