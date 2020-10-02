import socket
                    #Using IPv4
HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept() #s.accept() returns a new socket as the old one is just used as primary point of interaction,ie handshaking etc.
    with conn:              #The new socket is actually used for data transmissiion
        print('Connected by', addr)
        while True:
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(data)      #Sends the data back to client