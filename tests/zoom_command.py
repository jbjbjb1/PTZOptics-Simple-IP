# This script asks the user what level zoom to do.

import socket

# Camera settings
IPADDR = '192.168.8.99'
PORTNUM = 1259

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0)
s.connect((IPADDR, PORTNUM))

# Commands
def COMMAND2(zoom_code):
    ''' Zooms to a pre-defined locations. '''
    command_template = '81 01 04 47 0p 0q 0r 0s FF'
    p = zoom_code[0]
    q = zoom_code[1]
    r = zoom_code[2]
    s = zoom_code[3]
    command = command_template.replace('p', p)
    command = command.replace('q', q)
    command = command.replace('r', r)
    command = command.replace('s', s)

    return command

# Command line to call and send commands
while True:
    zoom = input('What is the desired zoome level (0 to 20) or "e" to exit?')
    if zoom == 'e':
        break
    zoom_val = 4000 * (float(zoom)/20)      # needed to estimate, 0000 zoom out, 4000 zoom in
    zoom_code = str(int(zoom_val)).zfill(4)
    print(f'Zoom code for {zoom} of zoom val {zoom_val} is {zoom_code} will be sent by {COMMAND2(zoom_code)}.')

    data = bytes.fromhex(COMMAND2(zoom_code))

    s.send(data)

s.close()