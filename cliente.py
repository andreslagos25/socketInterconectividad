import socket
import time
import pickle
HOST = "127.0.0.1" # Direccion del servidor direccion propia
PORT = 65123 # > 1023 (Puerto de envío)
HEADER = 10 # Tamaño del encabezado que indica la longitud de los datos serializados

# Crear un socket usando IPv4 (AF_INET) y TCP (SOCK_STREAM)
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # Vincular el socket al HOST y al PORT especificados
    s.connect((HOST, PORT))

    # Vincular el socket al HOST y al PORT especificados
    names = [100, 
             'Maria', 
             'Rodrigo', 
             3.1416, 
             'Juan', 
             'Nabucondonsor', 
             'Sandro',
             (1+3j)]

    # Serializar la lista "names" utilizando pickle
    data_serial = pickle.dumps(names)
    # Obtener la longitud de los datos serializados y convertirla en una cadena
    data_len = str(len(data_serial))

    # Crear una cadena de encabezado que tenga un ancho fijo de HEADER (rellenado con espacios en blanco)
    # para indicar la longitud de los datos serializados
    data = bytes(f"{data_len:<{HEADER}}", 'utf-8') + data_serial
    
    print(data)
    # Enviar los datos al servidor a través del socket
    s.send(data)
        
        
    # Esperar 1 segundo (esto es opcional y se utiliza aquí para asegurarse de que el servidor tenga tiempo para recibir los datos)
    time.sleep(1) 