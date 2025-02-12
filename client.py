import socket
import sys

# Ensure correct command-line arguments
if len(sys.argv) != 4:
    print("Usage: python3 client.py <server_host> <server_port> <filename>")
    sys.exit()

# Get server details from command-line arguments
server_host = sys.argv[1]  # e.g., "localhost" or CloudLab IP
server_port = int(sys.argv[2])  # e.g., 6789
filename = sys.argv[3]  # e.g., "HelloWorld.html"

try:
    # Create a TCP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect to the server
    client_socket.connect((server_host, server_port))
    print(f"Connected to server {server_host} on port {server_port}")

    # Send an HTTP GET request
    request = f"GET /{filename} HTTP/1.1\r\nHost: {server_host}\r\n\r\n"
    client_socket.send(request.encode())

    # Receive and print the response
    response = client_socket.recv(4096).decode()
    print("\nServer Response:\n")
    print(response)

    # Close the socket
    client_socket.close()

except Exception as e:
    print(f"Error: {e}")
    sys.exit()