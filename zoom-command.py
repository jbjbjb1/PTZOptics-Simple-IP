# This script asks the user what level zoom to do.

import socket

# Camera settings
IPADDR1 = '192.168.8.99'
PORTNUM = 1259

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0)
s.connect((IPADDR1, PORTNUM))

# Commands
COMMAND1 = '8101040702FF'       # zooms all the way in

def COMMAND2(zoom_code):
    ''' Zooms to a pre-defined locations. '''
    command_template = '81010447pqrsFF'
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
    # Range for p, q, r , s is: 0000 to 1770 (for 20X zoom)
    # Above info from: https://ptzoptics.com/wp-content/uploads/2014/09/PTZOptics-VISCA-Commands-r1.pdf
    zoom = float(input('What is the desired zoome level (0 to 20)?'))
    zoom_val = 1770 * (zoom/20)
    zoom_code = str(int(zoom_val)).zfill(4)
    print(f'Zoom code for {zoom} of zoom val {zoom_val} is {zoom_code} will be sent by {COMMAND2(zoom_code)}.')

    data = bytes.fromhex(COMMAND2(zoom_code))

    s.send(data)

    s.close()