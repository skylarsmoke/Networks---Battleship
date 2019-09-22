#Skylar Smoker, John Lambrecht, and Ben Barnett

import socket

def menu():
    print("Welcome to Battleship!")
    print()
    print("1) Play")
    print("2) Quit")
    print()

def play():
    print("Connecting to server...")
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((socket.gethostbyname("localhost"), 1235))
    
    while True:
        msg = sock.recv(128)
        print(msg.decode("utf-8"))
        
        
def main():
    choice = 0
    while (choice != 2):
        menu()
        choice = int(input("Selection: "))
        if (choice == 1):
            play()
            
main()
            
        
    