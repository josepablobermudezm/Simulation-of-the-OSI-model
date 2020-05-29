import socket, os

def iniciarCliente(host, puerto, msg_env):
    c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    c.connect((host, puerto))
    msg_rec = c.recv(1024)
    print()
    print (msg_rec.decode('utf8'))
    c.send(msg_env.encode('ascii', errors='replace'))
    c.close()

def CodificarMensaje(m):
    j = 0
    d = [3,5,2]
    mensaje = ""
    #archivo = open(os.path.dirname(__file__) + "/datos.txt", "r")
    #tam = os.path.getsize(os.path.dirname(__file__) + "/datos.txt")
    for x in m:
        c = ord(x)
        if (c >= 65 and c <= 90):
            c+= d[j]
            if (c < 65):
                c = c + 64 - 90
            elif (c > 90 and c <= 95):
                c = (c + 64 - 90)
        elif (c == 32):
            c = 126
        mensaje += chr(c)
        if(j < 2):
            j+=1
        else:
            j = 0

    return mensaje

def iniciarServidor(host, puerto):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host,puerto))
    s.listen(5) #hasta 5 repeticiones
    d = [3,5,2]
    while True:
        mensaje = ""
        j = 0
        # establecer conexión
        (c, addr) = s.accept()
        print("Se estableció conexión con: %s " % str(addr))

        msg = 'Conexion establecida con: %s' % socket.gethostname() + "\r\n"
        c.send(msg.encode('utf8'))
        msg_rec = c.recv(1024)
        
        print(msg_rec)

        for i in msg_rec:
            x = i
            if (x >= 65 and x <= 90):
                x-= d[j]
                if (x < 65):
                    x = x -64 + 90
            elif (x == 126):
                x = 32
            mensaje += chr(x)
            if(j < 2):
                j+=1
            else:
                j = 0

        print(mensaje)
        return mensaje

        c.close()

if __name__ == "__main__":
    host = ""
    puerto = 44440
    while True: # se inicia en modo servidor y se pasa a cliente se solicita LA IP del siguiente equipo y se pasa el mensaje, se regresa a modo servidor
        host = ""
        mensaje = iniciarServidor(host, puerto)
        print("Digita la dirección IP a donde deseas enviar el mensaje")
        host = input() 
        iniciarCliente(host,puerto,CodificarMensaje(mensaje))
