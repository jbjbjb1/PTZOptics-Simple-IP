# GUI code for script

import webbrowser

import wx

import simple_cmds as sc


# Create GUI window
class MainWindow(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title)
        self.sizer = wx.BoxSizer(wx.VERTICAL)

        # Give some padding
        self.sizer.Add(250, 0)

        # Add buttons
        self.buttons = []
        button_list = ['Zoom Preacher', 'Zoom Stage', 'Zoom Out', 'Instructions']
        for i, button_name in enumerate(button_list):
            self.buttons.append(wx.Button(self, -1, button_name, size=(-1, 50)))
            self.sizer.Add(self.buttons[i], 1, wx.EXPAND)

        # Layout sizers
        self.SetSizer(self.sizer)
        self.SetAutoLayout(1)
        self.sizer.Fit(self)
        self.Show()

        # Bind button events
        self.Bind(wx.EVT_BUTTON, self.zoompreacher, self.buttons[0])
        self.Bind(wx.EVT_BUTTON, self.zoomstage, self.buttons[1])
        self.Bind(wx.EVT_BUTTON, self.zoomout, self.buttons[2])
        self.Bind(wx.EVT_BUTTON, self.Instructions, self.buttons[3])

        # Initiate class object for actions
        self.cam = sc.Camera()

    def zoompreacher(self, event):
        ''' Zoom in on the preacher ''' 
        self.cam.cam_zoom_direct(self.cam.zoompreacher)
    
    def zoomstage(self, event):
        ''' Zoom on the stage ''' 
        self.cam.cam_zoom_direct(self.cam.zoomstage)
    
    def zoomout(self, event):
        ''' Zoom fully out ''' 
        self.cam.cam_zoom_direct(self.cam.zoomout)

    def Instructions(self, event):
        ''' Open the Github website. '''
        webbrowser.open('https://github.com/jbjbjb1/PTZOptics-Simple-IP')


# Start GUI
app = wx.App(False)
frame = MainWindow(None, "Camera Zoom")
app.MainLoop()