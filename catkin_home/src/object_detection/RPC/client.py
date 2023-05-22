from __future__ import print_function

import logging

import grpc
import coordinates_pb2
import coordinates_pb2_grpc


def run():
    """
    Realiza una llamada RPC al servicio de coordenadas para obtener las coordenadas.

    Crea un canal inseguro de gRPC y llama al método GetCoordinates del servicio CoordinateService
    para obtener las coordenadas. Luego, imprime las coordenadas recibidas.

    Args:
        None

    Returns:
        None
    """

    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # of the code.
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = coordinates_pb2_grpc.CoordinateServiceStub(channel)
        response = stub.GetCoordinates(coordinates_pb2.Empty())
        print("Coords received: " + str(response))


if __name__ == '__main__':
    """
    Función principal del programa.

    Configura el registro de mensajes de registro y llama a la función run().

    Args:
        None

    Returns:
        None
    """

    logging.basicConfig()
    run()
