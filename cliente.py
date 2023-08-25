import socket

HOST = "127.0.0.1" # Direccion del servidor
PORT = 65123 # > 1023 (Puerto de envío)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))

    s.sendall(b"Hola mundo")

    data = s.recv(1024)

print("Recibido" , repr(data))