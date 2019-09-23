#Skylar Smoker, John Lambrecht, and Ben Barnett

import socket
import sys

def startServer(port, file):
    #Binds sockets to set up server
    print("Starting server...")
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = socket.gethostbyname("localhost")
    sock.bind((host, int(port)))
    sock.listen(5)
    
    #Opens own_board.txt and creates arrays for both boards
    file = open(file, "r")
    own_board = [[0 for x in range(10)] for y in range(10)]
    opponent_board = [[0 for x in range(10)] for y in range(10)]
    
    #Fills own_board array from text
    transferBoard(own_board, file)
    transferBoard(opponent_board, open("opponent_board.txt", "r"))
    
    #Prints a display for both Own and Opponents board
    print()
    print("        Own Board")
    displayBoard(own_board)
    print("     Opponent Board")
    displayBoard(opponent_board)
    
    #Ships health and associated char
    shipHealth = ["D", 2, "S", 3, "R", 3, "B", 4, "C", 5]
    
    print("Server Started, waiting for client...")
    print()
    
    while True:
        s, addr = sock.accept()
        print(f"Connected to: {addr}")
        print()
        msg = s.recv(1024)
        print(msg.decode("utf-8"))
        
def transferBoard(board, file):
    for x in range(10):
        for y in range(11):
            if y > 9:
                file.read(1)
            else:
                board[x][y] = file.read(1)
                
def displayBoard(board):
    line = "  _____________________"
    for x in range(10):
        if x > 0:
            line += "|\n | "
        else:
            line += "\n | "
        for y in range(10):
            line += board[x][y] + " "
    print(line + "|")
    print("  _____________________")
    print()
               
def main():
    startServer(sys.argv[1], sys.argv[2])
    
main()