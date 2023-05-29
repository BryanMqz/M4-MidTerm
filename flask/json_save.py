from flask import Flask, render_template
import json
import grpc
import coordinates_pb2
import coordinates_pb2_grpc
from google.protobuf.json_format import MessageToJson

app = Flask(__name__,template_folder='jsons')

def get_coords():
    channel = grpc.insecure_channel('localhost:50052/coords')
    stub = coordinates_pb2_grpc.CoordinateServiceStub(channel)
    
    # Make the call to the gRPC server
    response = stub.GetCoordinates(coordinates_pb2.Empty())
    
    # Process the response
    return response

# Flask route to make the call to the gRPC server
@app.route('/call-api')
def call_go_api():
    coordinates = json.loads(MessageToJson(get_coords()))
    return render_template('home.html', coordinates=coordinates)
    

if __name__ == '__main__':
    app.run()