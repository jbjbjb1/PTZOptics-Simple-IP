# This script zooms all the way in with the camera.

import socket

IPADDR1 = '192.168.8.99'
PORTNUM = 1259
COMMAND1 = '8101040702FF'       # zooms all the way in

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0)

s.connect((IPADDR1, PORTNUM))

data = bytes.fromhex(COMMAND1)

s.send(data)

s.close()