create:
	protoc --proto_path=proto proto/*.proto --go_out=gen
	protoc --proto_path=proto proto/*.proto --go-grpc_out=gen
	protoc -I ./proto \
   --go_out ./proto --go_opt paths=source_relative \
   --go-grpc_out ./proto --go-grpc_opt paths=source_relative \
	proto/*.proto
clean:
	rm gen/proto/*.go
#protoc -I . --grpc-gateway_out ./gen/. \
    --grpc-gateway_opt logtostderr=true \
    --grpc-gateway_opt paths=source_relative \
	--grpc-gateway_opt generate_unbound_methods=true \
	proto/*.proto