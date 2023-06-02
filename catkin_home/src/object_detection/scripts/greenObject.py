#!/usr/bin/env python3

import rospy
from cv_bridge import CvBridge
from sensor_msgs.msg import Image
import cv2
import ctypes
from std_msgs.msg import Float64MultiArray
from std_msgs.msg import Header
from time import time

class GreenObjectDetector:
    """
    Clase que implementa un detector de objetos verdes.

    Este detector suscribe a la imagen capturada, aplica un filtro de color verde a la imagen
    y busca el contorno más grande en la imagen filtrada. Luego, calcula las coordenadas del
    centroide del contorno más grande y publica las coordenadas multiplicadas por 100 junto
    con una marca de tiempo.
    
    Attributes:
        bridge (CvBridge): Bridge for converting ROS Image messages to OpenCV images.
        image_sub (rospy.Subscriber): Subscriber for the "/captured_image" topic.
        green_lower (tuple): Lower HSV values for green color range.
        green_upper (tuple): Upper HSV values for green color range.
        coordinate_multiplier (ctypes.CDLL): Library for multiplying coordinates.
        coord_pub (rospy.Publisher): Publisher for the "/multiplied_coordinates" topic.
    """

    def __init__(self):
        """
        Constructor de la clase GreenObjectDetector.

        Inicializa los suscriptores, define el rango de color verde, carga la biblioteca externa
        'libcoordinate_multiplier.so' y crea el publicador para las coordenadas multiplicadas.
        """
        self.bridge = CvBridge()
        self.image_sub = rospy.Subscriber("/captured_image", Image, self.image_callback)
        self.green_lower = (40, 110, 40)
        self.green_upper = (80, 255, 200)
        
        # Step 3: Load the library
        self.coordinate_multiplier = ctypes.CDLL('/home/bryan/M4-MidTerm/catkin_home/src/object_detection/src/libcoordinate_multiplier.so')
        
        # Step 4
        self.coord_pub = rospy.Publisher("/multiplied_coordinates", Float64MultiArray, queue_size=5)

    def image_callback(self, data):
        """
        Callback para el suscriptor de la imagen capturada.

        Procesa la imagen capturada, detecta el objeto verde y calcula sus coordenadas.
        Luego, multiplica las coordenadas por 100, las publica junto con una marca de tiempo.

        Args:
            data: Mensaje de ROS de imagen capturada.
        """
        cv_image = self.bridge.imgmsg_to_cv2(data, "bgr8")
        hsv_image = cv2.cvtColor(cv_image, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsv_image, self.green_lower, self.green_upper)
        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        if contours:
            largest_contour = max(contours, key=cv2.contourArea)
            M = cv2.moments(largest_contour)
            cx = int(M["m10"] / M["m00"])
            cy = int(M["m01"] / M["m00"])
            rospy.loginfo("Green object detected at ({}, {})".format(cx, cy))
            
        # Multiply the coordinates by 100
        cx = ctypes.c_int(cx)
        cy = ctypes.c_int(cy)
        self.coordinate_multiplier.multiply_coordinates(ctypes.byref(cx), ctypes.byref(cy))
        
        # Publish multiplied coordinates with timestamp
        rospy.logwarn("Timestamp: {}".format(time()))
        coordinates = [cx.value, cy.value, time()]
        coordinates_msg = Float64MultiArray()
        coordinates_msg.data = coordinates
        self.coord_pub.publish(coordinates_msg)
        
        # Print the multiplied coordinates
        # rospy.loginfo("Multiplied coordinates: ({}, {})".format(cx, cy))
    
        # Show the image
        cv2.imshow("Image window", cv_image)
        cv2.waitKey(1)

if __name__ == '__main__':
    """
    Función principal del programa.

    Inicia el nodo de ROS, crea una instancia de GreenObjectDetector y mantiene el nodo en ejecución.
    """
    rospy.init_node('green_object_detector')
    #Run node
    print("Running") 
    detector = GreenObjectDetector()
    rospy.spin()
