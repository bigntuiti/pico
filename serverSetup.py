import network
import socket
import time

SSID = "toko"

PASSWORD = "neuro123"

# Connect to Wi-Fi

wlan = network.WLAN(network.STA_IF)
wlan.active(True)

networks = wlan.scan()

for network_info in networks:
    print(network_info)

wlan.connect(SSID, PASSWORD)

max_time = 10

while (not wlan.isconnected() & max_time!=0):
    time.sleep(1)
    print("Waiting for Hotspot...")
    max_time = max_time-1

print("Connected:", wlan.ifconfig())

# Create socket server

addr = socket.getaddrinfo("0.0.0.0", 2345)[0][-1]
s = socket.socket()
s.bind(addr)
s.listen(1)

print("Listening on", addr)

try:
    while True:
        client, client_addr = s.accept()
        print("Client connected from", addr)

        data = client.recv(1024)
        print("Recieved Data: ", data)

        client.send(b"OK\n")

        client.close()
finally:
    print("Closing socket")
    s.close()