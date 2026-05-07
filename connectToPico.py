import socket

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

client.connect(("172.20.10.3",2345))
print("Connected to Car...")

try:
    while True:
        command = input("Enter car command:")

        client.send((command+"\n").encode())

except KeyboardInterrupt:
    client.close()