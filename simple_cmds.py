import socket
import json

class Camera():
    def __init__(self):
        ''' Load settings, open socket '''

        # Laod variables else create default variables
        try:
            with open('simple_cmds_settings.txt', 'r') as f:
                variables = json.load(f)
                for key, value in variables.items():
                    setattr(self, key, value)
        except FileNotFoundError:
            # TODO automatically create the settings file from default values rather than below
            self.IPADDR = '192.168.8.99'
            self.PORTNUM = 1259
            self.zoompreacher = 18
            self.zoomstage = 10
            self.zoomout = 0

        # Open socket to communicate
        self.s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0)
        self.s.connect((self.IPADDR, self.PORTNUM))

    def cam_zoom_direct(self, zoom_x):
        ''' Zooms to a pre-defined locations. '''
        # 20x zoom, 0000 wide -> 4000 tele
        zoom_val = 4000 * (float(zoom_x)/20)        
        # get in format of four digits as intiger
        zoom_code = str(int(zoom_val)).zfill(4)   
        # split zoom code so variables in template can be replaced  
        command_template = '81 01 04 47 0p 0q 0r 0s FF'
        p = zoom_code[0]
        q = zoom_code[1]
        r = zoom_code[2]
        s = zoom_code[3]
        command = command_template.replace('p', p)
        command = command.replace('q', q)
        command = command.replace('r', r)
        command = command.replace('s', s)

        # format and send data
        data = bytes.fromhex(command)
        self.s.send(data)

        return command