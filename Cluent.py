import socket
import threading

def receive_messages(client_socket):
    while True:
        message = client_socket.recv(1024).decode()
        if not message:
            break
        print(message)

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 12345))

threading.Thread(target=receive_messages, args=(client_socket,)).start()

while True:
    message = input("Scrivi un messaggio: ")
    client_socket.send(message.encode())
