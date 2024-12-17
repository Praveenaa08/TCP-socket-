# TCP-socket-
Simple TCP server using Python's socket library

1. Server Initialization: A TCP socket is created, bound to a local address (127.0.0.1) and port (9876), then set to listen for incoming connections.
2. Client Connection Handling: The server accepts client connections in a loop, storing client IPs in a list (client_connections_per_window).
3. Message Handling: For each connected client, the server receives data, processes the message, and sends back a response. The server looks for a specific end marker ("./") in messages and only processes messages before it.
4. Connection Limits: If more than 10 clients connect within 5 seconds, the server exits.
