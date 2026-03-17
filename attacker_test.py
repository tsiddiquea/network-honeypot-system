import socket

HOST = "127.0.0.1"
PORT = 2222

s = socket.socket()
s.connect((HOST, PORT))

print(s.recv(1024).decode())
print(s.recv(1024).decode())

username = input("Enter username: ")
s.send((username + "\n").encode())

print(s.recv(1024).decode())

password = input("Enter password: ")
s.send((password + "\n").encode())

s.close()