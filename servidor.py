import socket

HOST = "127.0.0.1" #Direccion loopback
PORT = 65123 # > 1023 (Puerto de escucha)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()

    with conn:
        print(f"Conectado a {addr}:")
        while True:
            data = conn.recv(1024)
            if not data:
                break
            
            conn.sendall(data)

