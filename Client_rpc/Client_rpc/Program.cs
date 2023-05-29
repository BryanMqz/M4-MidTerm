using System;
using Grpc.Core;
using RPCDemoClient;

namespace clientns
{
    class Program
    {
        static void Main(string[] args)
        {
            Channel channel = new Channel("localhost:50051", ChannelCredentials.Insecure);
            var client = new CoordinateService.CoordinateServiceClient(channel);

            while(true)
            {
                var reply = client.GetCoordinates(new Empty());
                Console.WriteLine("Coordinates received: " + reply);
            }
        }
    }
}

