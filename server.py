#Skylar Smoker, John Lambrecht, and Ben Barnett

import socket

def startServer():
    print("Starting server...")
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = socket.gethostbyname("localhost")
    port = 1235
    sock.bind((host, port))
    sock.listen(5)

    while True:
        s, addr = sock.accept()
        print(f"Connected to: {addr}")
        s.send(bytes("Connected to server.", "utf-8"))

def main():
    startServer()
    
main()