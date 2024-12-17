import socket
import sys

#creating a TCP socket that involves IPv4 addressing
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_connections_per_window = []
window_seconds = 5
num_of_connections_per_window = 10
while True:
    if len(client_connections_per_window) > num_of_connections_per_window:
            sys.exit()
            time.sleep(window_seconds)
while True: 
    print("Server socket has been created!")

    #bind the server socket to loopback address and chosen port number
    server_socket.bind(('127.0.0.1', 9876))

    #listen to incoming connections
    server_socket.listen()

    while True:
        #Accept connection request (client socket object and ipaddr+portnum)
        client_socket_obj, (client_ip, client_port) = server_socket.accept()
        client_connections_per_window.append(client_ip)
        print(f"Client has connected from {str(client_ip)} through port {client_port}")
        while True:
                client_data = client_socket_obj.recv(1024)
                client_message = client_data.decode()           
                if len(client_data) > 0:
                    end_marker = "./"
                    if end_marker in client_message:
                        client_actual_message = client_message[:client_message.index(end_marker)]
                        print(f"Message from client: {client_actual_message}")
                        client_socket_obj.sendall(client_actual_message.encode())              
                else:
                    break
