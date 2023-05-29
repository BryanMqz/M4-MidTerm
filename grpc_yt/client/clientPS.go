package main

import (
	"context"
	"log"

	pb "grpc_yt/gen/proto"

	"google.golang.org/grpc"
)

func main() {
	// gRPC server connection
	conn, err := grpc.Dial("localhost:50052", grpc.WithInsecure())
	if err != nil {
		log.Fatalf("Failed to connect to server: %v", err)
	}
	defer conn.Close()

	// gRPC client
	client := pb.NewCoordinateServiceClient(conn)

	// Make request to server
	resp, err := client.GetCoordinates(context.Background(), &pb.Empty{})
	if err != nil {
		log.Fatalf("Failed to get coordinates: %v", err)
	}

	// Manejar la respuesta del servidor
	log.Printf("Received coordinates: %+v", resp)
}
