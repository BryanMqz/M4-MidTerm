"""
@file json_save.py
@brief This is a Python file that uses Flask and gRPC to make 
a call to a gRPC server and render the response in a template.
"""
from flask import Flask, render_template
import json
import grpc
import coordinates_pb2
import coordinates_pb2_grpc
from google.protobuf.json_format import MessageToJson

app = Flask(__name__,template_folder='jsons')

def get_coords():
    """
    @brief This function establishes a connection with the gRPC server and retrieves coordinates.
    @return The response containing the coordinates.
    """
    channel = grpc.insecure_channel('localhost:50052/coords')
    stub = coordinates_pb2_grpc.CoordinateServiceStub(channel)
    
    # Make the call to the gRPC server
    response = stub.GetCoordinates(coordinates_pb2.Empty())
    
    # Process the response
    return response

# Flask route to make the call to the gRPC server
@app.route('/call-api')
def call_go_api():
    """
    @brief This Flask route calls the gRPC server and renders the coordinates in a template.
    @return The rendered template with the coordinates.
    """
    coordinates = json.loads(MessageToJson(get_coords()))
    return render_template('home.html', coordinates=coordinates)
    

if __name__ == '__main__':
    app.run()