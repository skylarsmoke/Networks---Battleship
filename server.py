#Skylar Smoker, John Lambrecht, and Ben Barnett

import socket
import sys
import re

#Creates "boards" to be filled by text files
own_board = [[0 for x in range(10)] for y in range(10)]
opponent_board = [["_" for x in range(10)] for y in range(10)]

#Initializes Battleship Server
def startServer(port, file):
    #Binds sockets to set up server
    print("Starting server...")
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = socket.gethostbyname("localhost")
    sock.bind((host, int(port)))
    sock.listen(5)
    
    #Opens own_board.txt and creates arrays for both boards
    file = open(file, "r")
    
    #Fills own_board array from text
    transferBoard(own_board, file)
    
    #Prints a display for both Own and Opponents board
    print()
    print("        Own Board")
    displayBoard(own_board)
    print("     Opponent Board")
    displayBoard(opponent_board)
    
    print("Server Started, waiting for client...")
    print()
    
    #Connects to client and responds with hit or miss
    while True:
        s, addr = sock.accept()
        print(f"Connected to: {addr}")
        print()
        msg = s.recv(1024)
        
        #Checks message sent by client and sends the correct reply
        servMsg = checkMsg(msg.decode("utf-8"))       
        s.sendall(bytes(str(servMsg), "utf-8"))
        
        
        s.close()
        
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
    
def checkHit(x, y):
    #Ships health and associated char
    shipHealth = ["D", 2, "S", 3, "R", 3, "B", 4, "C", 5]
    servMsg = ""
    
def checkMsg(msg):
    servMsg = ""
    splitMsg = re.split("\n", msg)
    if "GET /opponent_board.html" in msg:
        servMsg = displayBoard(opponent_board)
    elif "GET /own_board.html" in msg:
        servMsg = displayBoard(own_board)
    elif re.search("x=\d&y=\d", msg):
        for i in splitMsg:
            if re.search("x=\d&y=\d", i):
                coord = re.split("&", i)
                for j in coord:
                    val = re.search("\d", j).group()
                    coord[j] = int(val)
                y = coord[1]
                x = coord[0]
                servMsg = checkHit(x, y)
    return servMsg
    
    
    
               
def main():
    startServer(sys.argv[1], sys.argv[2])
    
main()