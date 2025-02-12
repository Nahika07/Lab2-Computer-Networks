import os
from socket import *
import sys  # In order to terminate the program

print(f"Server running in directory: {os.getcwd()}")

# Create a server socket using TCP (SOCK_STREAM)
serverSocket = socket(AF_INET, SOCK_STREAM)
serverPort = 6789  # Make sure this matches the browser request
serverSocket.bind(('0.0.0.0', serverPort))  # Listen on all interfaces
serverSocket.listen(5)  # Allow multiple clients

print(f"Server is running on port {serverPort}...")

while True:
    print('Ready to serve...')

    # Accept a new connection from a client
    connectionSocket, addr = serverSocket.accept()
    print(f"Connection from {addr}")

    try:
        # Receive the HTTP request
        message = connectionSocket.recv(1024).decode()
        print("Received request:\n", message)

        # Extract filename from the request (e.g., "GET /HelloWorld.html HTTP/1.1")
        filename = message.split()[1][1:]  # Remove the leading "/"
        filepath = os.path.join(os.getcwd(), filename)  # Get absolute path
        print(f"Looking for file: {filepath}")

        # Open and read the requested file
        with open(filepath, 'r') as f:
            outputdata = f.read()

        # Send HTTP header
        response_header = "HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n"
        connectionSocket.send(response_header.encode())

        # Send the file content
        connectionSocket.send(outputdata.encode())

    except Exception as e:
        print(f"Error opening file {filename}: {e}")

        # Send 404 response
        response = "HTTP/1.1 404 Not Found\r\nContent-Type: text/html\r\n\r\n"
        response += "<html><body><h1>404 Not Found</h1></body></html>\r\n"
        connectionSocket.send(response.encode())

    # Close the connection after sending the response
    connectionSocket.close()

# Close the server socket (won't reach here)
serverSocket.close()
sys.exit()
