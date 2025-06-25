# server.py
import socket

# Setup server to listen to Client A
server_socket = socket.socket()
server_socket.bind(('localhost', 9999))
server_socket.listen(1)
print("Server: Waiting for Client A...")

clientA, addrA = server_socket.accept()
print(f"Server: Connected to Client A at {addrA}")

# Receive number from Client A
num = clientA.recv(1024).decode()
print(f"Server: Received number from Client A = {num}")

# Connect to Client B
clientB_socket = socket.socket()
clientB_socket.connect(('localhost', 8888))
print("Server: Connected to Client B")

# Send number to Client B
clientB_socket.send(num.encode())

# Receive processed result from Client B
result = clientB_socket.recv(1024).decode()
print(f"Server: Received result from Client B = {result}")

# Send result back to Client A
clientA.send(result.encode())

# Close all sockets
clientA.close()
clientB_socket.close()
server_socket.close()
