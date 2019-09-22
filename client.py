#Skylar Smoker, John Lambrecht, and Ben Barnett

import socket
import sys

def fire(IP, prt, x, y):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((socket.gethostbyname(IP), int(prt)))
    
    while True:
        
        msg = sock.recv(128)
        print(msg.decode("utf-8"))
        
        
def main():
    IP = sys.argv[1]
    prt = sys.argv[2]
    x = sys.argv[3]
    y = sys.argv[4]
    fire(IP, prt, x, y)
            
main()
            
        
    