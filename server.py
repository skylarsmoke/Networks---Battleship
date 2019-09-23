#Skylar Smoker, John Lambrecht, and Ben Barnett

import socket
import sys

def startServer(p, file):
    print("Starting server...")
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = socket.gethostbyname("localhost")
    sock.bind((host, int(p)))
    sock.listen(5)
    file = open(file, "r")
    own_board = [[0 for x in range(10)] for y in range(10)]
    opponent_board = [[0 for x in range(10)] for y in range(10)]
    makeBoard(own_board, file)
    makeBoard(opponent_board, file)
    print("Server Started.")
    
        
def makeBoard(board, file):
    for i in range(10):
        for j in range(11):
            pass
        

def main():
    startServer(sys.argv[1], sys.argv[2])
    
main()