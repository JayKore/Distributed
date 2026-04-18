import socket

HOST = '127.0.0.1'
PORT = 5000

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen(1)

    print("Server: Waiting for connection...")

    conn, addr = server_socket.accept()
    print(f"Server: Connected to {addr}")

    data = conn.recv(1024).decode()
    print("Server received:", data)

    response = "Hello Client, message received!"
    conn.send(response.encode())

    conn.close()
    server_socket.close()

if __name__ == "__main__":
    start_server()