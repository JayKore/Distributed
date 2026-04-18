import socket
import time

HOST = '127.0.0.1'
PORT = 5000

def start_client():
    time.sleep(1)  # ensure server starts first

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((HOST, PORT))

    message = "Hello Server, this is Client!"
    client_socket.send(message.encode())

    response = client_socket.recv(1024).decode()
    print("Client received:", response)

    client_socket.close()

if __name__ == "__main__":
    start_client()