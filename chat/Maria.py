import socket
import threading

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 12345))

username = input("Inserisci il tuo nome: ")

def receive_messages():
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if message:
                print(message)  # Stampa i messaggi ricevuti
            else:
                break
        except Exception as e:
            print(f"Errore nella ricezione: {e}")
            break
    client_socket.close()

threading.Thread(target=receive_messages, daemon=True).start()

while True:
    message = input("Scrivi un messaggio: ")
    full_message = f"{username}: {message}"
    client_socket.send(full_message.encode('utf-8'))
