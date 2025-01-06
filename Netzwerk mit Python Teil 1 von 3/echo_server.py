import socket
def main():
    IP_ADDRESS = '127.0.0.1' # 'localhost' oder IP Konfig auslesen
    PORT = 12345
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_sock:
        server_sock.bind((IP_ADDRESS, PORT))
        server_sock.listen(1) # Wieviele Connects möglich, 0 ist unendlich
        server_sock.accept()

    if __name__ == '__main__':
        main()