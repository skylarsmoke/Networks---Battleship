#Skylar Smoker, John Lambrecht, and Ben Barnett

import socket
import sys

def startServer(p, file):
    print("Starting server...")
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = socket.gethostbyname("localhost")
    sock.bind((host, int(p)))
    sock.listen(5)
    board = open(file, "r")
    print("Server Started.")
    print("Looking for client...")
    while True:
        s, addr = sock.accept()
        print("Client found.")
        print(f"Connected to: {addr}")
        s.send(bytes("Connected to server.", "utf-8"))

def main():
    startServer(sys.argv[1], sys.argv[2])
    
main()