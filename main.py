import network
import socket
import time
from machine import Pin

pin = Pin("LED", Pin.OUT)

SSID = "toko"

PASSWORD = "neuro123"

# Connect to Wi-Fi

wlan = network.WLAN(network.STA_IF)
wlan.active(True)

networks = wlan.scan()

for network_info in networks:
    print(network_info)

wlan.connect(SSID, PASSWORD)

while (not wlan.isconnected()):
    pin.toggle()
    time.sleep(1)
    print("Waiting for Hotspot...")

print("Connected:", wlan.ifconfig())

# Create socket server

addr = socket.getaddrinfo("0.0.0.0", 2345)[0][-1]
s = socket.socket()
s.bind(addr)
s.listen(1)
pin.off()

print("Listening on", addr)

try:
    while True:
        client, client_addr = s.accept()
        client.settimeout(100)
        print("Client connected from", client_addr)
        pin.on()
        try:
            while True:
                try:
                    data = client.recv(1024)
                except OSError:
                    continue

                if not data:
                    break

                pin.toggle()
                time.sleep(0.1)
                pin.toggle()
                time.sleep(0.1)
                pin.toggle()
                time.sleep(0.1)
                pin.toggle()
                time.sleep(0.1)
                pin.toggle()
                time.sleep(0.1)
                pin.toggle()


                data_decoded = data.strip().decode()
                
                if data_decoded == "RIGHT":
                    print("I AM GOING RIGHT!")
                    
                elif data_decoded == "LEFT":
                    print("I AM GOING LEFT!")
                elif data_decoded == "FORWARD":
                    print("I AM GOING FORWARD!")
                else:
                    print("Unknown Command: ", data_decoded)
        finally:
            client.close()
        
except KeyboardInterrupt:
    print("Closing socket")
    pin.off()
    s.close()

finally:
    print("Closing socket")
    pin.off()
    s.close()