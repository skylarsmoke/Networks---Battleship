#Skylar Smoker, John Lambrecht, and Ben Barnett

import socket
import sys

def fire(IP, prt, x, y):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((socket.gethostbyname(IP), int(prt)))
    
    user = "Battleship Client"
    coord = "x = %d, y = %d" %(int(x), int(y))
    contType = "application/x-www-form-urlencoded"
    length = str(len(coord))
    connectionType = "close"
    
    msg = "POST / HTTP/1.1\r\n" \
       "Connection: %s\r\n" \
       "Content-Type: %s\r\n" \
       "User-Agent: %s\r\n" \
       "Content-Length: %s\r\n" \
       "%s" \
       % (connectionType, contType, user, length, coord)
       
    sock.send(msg.encode("utf-8"))
    servResp = sock.recv(1000).decode()
    
    sock.close()
        
        
def main():
    IP = sys.argv[1]
    prt = sys.argv[2]
    x = sys.argv[3]
    y = sys.argv[4]
    fire(IP, prt, x, y)
            
main()
            
        
    