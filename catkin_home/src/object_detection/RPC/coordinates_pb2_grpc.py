# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import coordinates_pb2 as coordinates__pb2


class CoordinateServiceStub(object):
    """Client stub for the CoordinateService service."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetCoordinates = channel.unary_unary(
                '/multiplied_coordinates.CoordinateService/GetCoordinates',
                request_serializer=coordinates__pb2.Empty.SerializeToString,
                response_deserializer=coordinates__pb2.Coordinates.FromString,
                )


class CoordinateServiceServicer(object):
    """Base class for the CoordinateService service."""

    def GetCoordinates(self, request, context):
        """GetCoordinates RPC.

        This method is unimplemented and will raise an exception.

        Args:
            request: The request message.
            context: The context object for the RPC call.

        Returns:
            None
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_CoordinateServiceServicer_to_server(servicer, server):
    """Helper function to add a CoordinateServiceServicer to a grpc.Server."""
    rpc_method_handlers = {
            'GetCoordinates': grpc.unary_unary_rpc_method_handler(
                    servicer.GetCoordinates,
                    request_deserializer=coordinates__pb2.Empty.FromString,
                    response_serializer=coordinates__pb2.Coordinates.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'multiplied_coordinates.CoordinateService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


class CoordinateService(object):
    """Experimental API for the CoordinateService service."""

    @staticmethod
    def GetCoordinates(request, target, options=(), 
                       channel_credentials=None, 
                       call_credentials=None, 
                       insecure=False, 
                       compression=None, 
                       wait_for_ready=None, 
                       timeout=None, metadata=None):
        """GetCoordinates RPC.

        Args:
            request: The request message.
            target: The target address for the RPC.
            options: A list of key-value pairs to configure the RPC options.
            channel_credentials: Channel credentials for the RPC channel.
            call_credentials: Call credentials for the RPC call.
            insecure: Flag indicating whether to use insecure channel.
            compression: Compression options for the RPC.
            wait_for_ready: Flag indicating whether to wait for the server to be ready before sending the RPC.
            timeout: Timeout duration for the RPC.
            metadata: Additional metadata for the RPC call.

        Returns:
            The response message.
        """
        return grpc.experimental.unary_unary(request, target, '/multiplied_coordinates.CoordinateService/GetCoordinates',
            coordinates__pb2.Empty.SerializeToString,
            coordinates__pb2.Coordinates.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

