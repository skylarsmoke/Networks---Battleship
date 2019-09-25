#Skylar Smoker, John Lambrecht, and Ben Barnett

# Help from Kyle J. B. code examples, as well as stack overflow examples

import socket
import sys
import re

def fire(IP, prt, x, y):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((socket.gethostbyname(IP), int(prt)))
    
    user = "Battleship Client"
    try:
        coord = "x=%d&y=%d" %(int(x), int(y))
    except:
        coord = "x={x}&y={y}" .format(x=x, y=y)
    contType = "application/x-www-form-urlencoded"
    length = len(coord)
    connectionType = "close"
    
    msg = "POST / HTTP/1.1\r\n" \
       "Connection: %s\r\n" \
       "Content-Type: %s\r\n" \
       "User-Agent: %s\r\n" \
       "Content-Length: %s\r\n" \
       "%s\n" \
       % (connectionType, contType, user, str(length), coord)
       
    sock.sendall(bytes(msg, "utf-8"))
    servResp = sock.recv(1024)
    
    servMsg = servResp.decode("utf-8")
    
    if "HTTP/1.1 410" in servMsg:
        print("HTTP/1.1 410 Gone")
    elif "HTTP/1.1 400" in servMsg:
        print("HTTP/1.1 400 Bad Request")
    elif "HTTP/1.1 404" in servMsg:
        print("HTTP/1.1 404 Not Found")
    else:
        servMsg = decodeMsg(servMsg)
        if servMsg == 0:
            
            coord = "hit=0"
            
            msg = "POST / HTTP/1.1\r\n" \
               "Connection: %s\r\n" \
               "Content-Type: %s\r\n" \
               "User-Agent: %s\r\n" \
               "Content-Length: %s\r\n" \
               "%s\n" \
               % (connectionType, contType, user, str(length), coord)
               
            #print("hit=0")
           
        elif servMsg == 1:
            
            coord = "hit=1"
            
            msg = "POST / HTTP/1.1\r\n" \
               "Connection: %s\r\n" \
               "Content-Type: %s\r\n" \
               "User-Agent: %s\r\n" \
               "Content-Length: %s\r\n" \
               "%s\n" \
               % (connectionType, contType, user, str(length), coord)
            
            #print("hit=1")
        else:
            
            coord = "hit=1\&sink=%s" % servMsg
            
            msg = "POST / HTTP/1.1\r\n" \
               "Connection: %s\r\n" \
               "Content-Type: %s\r\n" \
               "User-Agent: %s\r\n" \
               "Content-Length: %s\r\n" \
               "%s\n" \
               % (connectionType, contType, user, str(length), coord)
            
            #print("hit=1\&sink=%s" % servMsg)
    
    sock.close()
    
def decodeMsg(msg):
    n = 0
    answer = re.split("\n", msg)
    for i in answer:
        print(i)
        if re.search("hit=\d+&sink=\w", i):
            split = re.split("&", i)
            sink = re.split("=", split[1])
            n = re.search("\w", sink[1]).group()
        elif re.search("hit=\d+", i):
            n = int(re.search("\d+", i).group())
        
    return n
        
        
        
def main():
    IP = sys.argv[1]
    prt = sys.argv[2]
    x = sys.argv[3]
    y = sys.argv[4]
    fire(IP, prt, x, y)
            
main()
            
        
    