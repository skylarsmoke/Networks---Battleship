import socket

def startServer():
    print("Starting server...")
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = socket.gethostbyname("localhost")
    port = 1235
    sock.bind((host, port))
    sock.listen(5)

    while True:
        addr = sock.accept()
        print(f"Connected to: {addr}")
        addr.send(bytes("Connected to server."), "UTF-8")

def main():
    startServer()
    
main()