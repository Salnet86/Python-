import socket
import threading

def handle_client(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if message:
                print(message)
                for client in clients:
                    if client != client_socket:
                        client.send(message.encode('utf-8'))
            else:
                break
        except:
            break
    client_socket.close()
    clients.remove(client_socket)

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 12345))
server_socket.listen(5)
print("Server in ascolto...")

clients = []

while True:
    client_socket, addr = server_socket.accept()
    print(f'Connessione da {addr}')
    clients.append(client_socket)

    threading.Thread(target=handle_client, args=(client_socket,)).start()
