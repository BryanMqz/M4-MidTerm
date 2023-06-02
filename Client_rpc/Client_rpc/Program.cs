using System;
using Grpc.Core;
using RPCDemoClient;

namespace clientns
{
    /// <summary>
    /// Class representing the client application for obtaining coordinates from a gRPC service.
    /// </summary>
    class Program
    {
        static void Main(string[] args)
        {
            // Create a channel to connect to the gRPC service
            Channel channel = new Channel("localhost:50051", ChannelCredentials.Insecure);
            var client = new CoordinateService.CoordinateServiceClient(channel);

            while(true)
            {
                // Call the GetCoordinates method of the gRPC service
                var reply = client.GetCoordinates(new Empty());
                Console.WriteLine("Coordinates received: " + reply);
            }
        }
    }
}

