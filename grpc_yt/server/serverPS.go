package main

import (
	"context"
	"log"
	"net"

	pb "grpc_yt/gen/proto"

	"google.golang.org/grpc"
)

type CoordinateServiceServer struct {
	pb.UnimplementedCoordinateServiceServer
}

func (s *CoordinateServiceServer) GetCoordinates(ctx context.Context, req *pb.Empty) (*pb.Coordinates, error) {
	// Establish connection
	conn, err := grpc.Dial("localhost:50051", grpc.WithInsecure())
	if err != nil {
		log.Println(err)
		return nil, err
	}
	defer conn.Close()

	// Create client for external service
	coordinateServiceClient := pb.NewCoordinateServiceClient(conn)

	// Ask for coordinates
	resp, err := coordinateServiceClient.GetCoordinates(context.Background(), &pb.Empty{})
	if err != nil {
		log.Println(err)
		return nil, err
	}

	return resp, nil
}

func main() {
	listener, err := net.Listen("tcp", ":50052")
	if err != nil {
		log.Fatalf("Failed to listen: %v", err)
	}

	grpcServer := grpc.NewServer()

	pb.RegisterCoordinateServiceServer(grpcServer, &CoordinateServiceServer{})

	log.Println("Server started, listening on :50052")

	if err := grpcServer.Serve(listener); err != nil {
		log.Fatalf("Failed to serve: %v", err)
	}
}
