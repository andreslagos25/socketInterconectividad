import socket
import pickle
HOST = "192.168.137.9" #Direccion loopback direccion propia pc
PORT = 65123 # > 1023 (Puerto de escucha)
HEADER = 10 # Tamaño del encabezado que indica la longitud de los datos serializados

# Crear un socket usando IPv4 (AF_INET) y TCP (SOCK_STREAM)
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # Vincular el socket al HOST y al PORT especificados
    s.bind((HOST, PORT))
    # Comenzar a escuchar conexiones entrantes
    s.listen()
    # Aceptar una conexión entrante y obtener la conexión y la dirección del cliente
    conn, addr = s.accept()

    try:
        with conn:
            # Imprimir que se ha conectado al cliente
            print(f"Conectado a {addr}:{addr[1]}")
            # Bucle para recibir datos continuamente
            while True:
                # Recibir el encabezado que contiene la longitud de los datos
                data_len = conn.recv(HEADER)
                # Si no se recibe ningún dato, salir del bucle
                if not data_len:
                    break
                else:
                    # Inicializar una variable para almacenar los datos recibidos
                    data = b''
                    # Recibir los datos en fragmentos hasta que se reciba la cantidad especificada por data_len
                    data += conn.recv(int(data_len))
                    # Deserializar los datos utilizando pickle
                    data_deserial = pickle.loads(data)
                    # Imprimir los datos deserializados y su tipo
                    print(data_deserial)
                    print(type(data_deserial))
    except KeyboardInterrupt: # Capturar una interrupción de teclado (CTRL + C)
        pass
    # Imprimir un mensaje de cierre de conexión una vez que se sale del bucle
print("Cerrando conexion")

