# clientA.py
import socket
import time

# Connect to server
client_socket = socket.socket()
client_socket.connect(('localhost', 9999))

# Input number and send
num = input("Client A: Enter a number to send to Client B: ")
start_time = time.time()
client_socket.send(num.encode())

# Receive result from server
result = client_socket.recv(1024).decode()
end_time = time.time()

# Output result and delay
print(f"Client A: Received result from Client B = {result}")
print(f"Client A: Total round-trip delay = {end_time - start_time:.4f} seconds")

client_socket.close()
