from __future__ import print_function

import logging

import grpc
import coordinates_pb2
import coordinates_pb2_grpc


def run():
    """
    Function to establish a connection with the gRPC server and retrieve coordinates.

    Create an insecure gRPC channel and call the GetCoordinates method of the CoordinateService 
    service to get the coordinates. Then, it prints the received coordinates.
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
    Main function of the program.
    
    Sets up the logging of log messages and calls the run() function.
    """
    logging.basicConfig()
    run()
