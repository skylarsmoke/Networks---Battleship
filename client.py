#Skylar Smoker, John Lambrecht, and Ben Barnett

import socket
import sys

def play(ad, p, x, y):
    print("Connecting to server...")
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((socket.gethostbyname(ad), int(p)))
    
    while True:
        msg = sock.recv(128)
        print(msg.decode("utf-8"))
        
        
def main():
    play(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
            
main()
            
        
    