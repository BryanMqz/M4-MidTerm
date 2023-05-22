#!/usr/bin/env python3

from concurrent import futures
import logging
import grpc
import coordinates_pb2
import coordinates_pb2_grpc
import rospy
from std_msgs.msg import Float64MultiArray


class CoordinateService(coordinates_pb2_grpc.CoordinateServiceServicer):
    """
    Implementa el servicio de gRPC para obtener las coordenadas.

    Esta clase implementa los métodos definidos en el archivo de definición de servicio gRPC.
    Proporciona las funciones para obtener las coordenadas y manejar las llamadas al servicio.

    Args:
        coordinates_pb2_grpc.CoordinateServiceServicer: Clase base para implementar el servicio.

    Returns:
        None
    """

    def __init__(self):
        """
        Constructor de la clase CoordinateService.

        Inicializa las variables cx, cy y time en 0.0.

        Args:
            None

        Returns:
            None
        """
        self.cx = 0.0
        self.cy = 0.0
        self.time = 0.0
    
    def GetEmpty(self, request, context):
        """
        Implementa el método GetEmpty del servicio.

        Retorna un mensaje Empty.

        Args:
            request: Objeto de solicitud enviado por el cliente.
            context: Contexto de la llamada del servicio.

        Returns:
            coordinates_pb2.Empty: Objeto Empty como respuesta.
        """
        return coordinates_pb2.Empty()
    
    def GetCoordinates(self, request, context):
        """
        Implementa el método GetCoordinates del servicio.

        Retorna un mensaje Coordinates con las coordenadas actuales.

        Args:
            request: Objeto de solicitud enviado por el cliente.
            context: Contexto de la llamada del servicio.

        Returns:
            coordinates_pb2.Coordinates: Objeto Coordinates con las coordenadas actuales.
        """
        reply = coordinates_pb2.Coordinates()
        reply.cx = self.cx  # TO DO: obtener cx del tópico de ROS
        reply.cy = self.cy  # TO DO: obtener cy del tópico de ROS
        reply.time = self.time  # TO DO: obtener time del tópico de ROS
        return reply

    def callback(self, data):
        """
        Callback para el suscriptor del tópico de ROS.

        Actualiza las coordenadas en la instancia de CoordinateService con los valores recibidos.

        Args:
            data: Mensaje recibido del tópico de ROS.

        Returns:
            None
        """
        # Recupera los valores del mensaje de ROS
        cx_, cy_, time_ = data.data

        # Actualiza los valores en la instancia de CoordinateService
        self.cx = cx_
        self.cy = cy_
        self.time = time_

def serve():
    """
    Inicia el servidor gRPC y suscripción al tópico de ROS.

    Crea un servidor gRPC, registra el servicio CoordinateService en el servidor,
    configura el puerto y el servidor inicia la escucha. Luego, inicia la suscripción
    al tópico de ROS y mantiene el servidor gRPC en ejecución hasta que se detiene.

    Args:
        None

    Returns:
        None
    """
    port = '50051'
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    coordinate_service = CoordinateService()
    coordinates_pb2_grpc.add_CoordinateServiceServicer_to_server(coordinate_service, server)
    server.add_insecure_port('[::]:' + port)
    server.start()
    print("Server started, listening on " + port)

    # Subscribe to the ROS topic
    coordinates_data = rospy.Subscriber("/multiplied_coordinates", Float64MultiArray, coordinate_service.callback)
    
    # Start the gRPC server
    server.wait_for_termination()
    
    try:
        rospy.spin()
    except KeyboardInterrupt:
        server.stop(0)
        print("Server stopped.")    


if __name__ == '__main__':
    """
    Función principal del programa.

    Inicia el nodo de ROS, configura el registro de mensajes de registro y llama a la función serve().

    Args:
        None

    Returns:
        None
    """
    rospy.init_node('grpc_server', anonymous=True)
    logging.basicConfig()
    serve()