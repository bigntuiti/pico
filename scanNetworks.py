import network

wlan = network.WLAN(network.STA_IF)
wlan.active(True)

networks = wlan.scan()

print("Avaliable Wifi Networks: ")
for network_info in networks:
    print(network_info)
