import socket
import threading

clients = []

def handle_client(client_socket):
    while True:
        message = client_socket.recv(1024).decode()
        if not message:
            break
        broadcast(message, client_socket)
    clients.remove(client_socket)
    client_socket.close()

def broadcast(message, sender_socket):
    for client in clients:
        if client != sender_socket:
            client.send(message.encode())

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 12345))
server_socket.listen()

while True:
    client_socket, addr = server_socket.accept()
    clients.append(client_socket)
    threading.Thread(target=handle_client, args=(client_socket,)).start()
