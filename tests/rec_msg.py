# This script tests receiving socket messages.

import socket

IPADDR1 = '192.168.8.99'
PORTNUM = 1259
buffer_size = 4096

COMMAND1 = '81 09 04 47 FF'       # What is zoom position?

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0)

s.connect((IPADDR1, PORTNUM))
data = bytes.fromhex(COMMAND1)
s.send(data)
msg = s.recv(buffer_size)
print(f'Message back is: {msg.hex()}.')     # example b'\xde\xad\xbe\xef'.hex()

s.close()