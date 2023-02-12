
'''
MAKE SURE TO INSTALL UXPLAY FIRST: https://github.com/FDH2/UxPlay
Developed for Ubuntu/Linux, you could prob figure out how to port to other systems if u wanted to
Make sure you installed the SF Pro font from apple's website

made with cheese by JmarbinGG
'''


#imports
import PySimpleGUI as sg #pip install pexpect
import pexpect #pip install pysimplegui
import os
import time

#Setting the fonts and theme 
sfFontBeeg = ('SF Pro', 250)
sfFontNormal = ('SF Pro', 30)
sg.theme('Black')
#setting the start command(runs the uxplay file with the following params: -n(name) -nh(dont append hostname) -fs(always start in fullscreen))
startCommand = '/home/[YOUR_USERNAME]/Downloads/uxplay/uxplay -n [AIRPLAY_SERVER_NAME] -nh -fs'

#starting the terminal to interact with uxplay
child = pexpect.spawn(startCommand)

#checks the status and updates the text appropriately 
def status():
    #setting the words to look for
    index = child.expect(['Initialized', 'Connection closed',  'Begin streaming to GStreamer video pipeline'], timeout=600)

    #checking for the initial start command
    if index == 0:
        window['status'].update('Ready')
    #checks if a device disconnects, making it available again
    elif index == 1:
        window['status'].update('Ready')
    #checks if a device is connected
    elif index == 2:
        window['status'].update('Connected')
    #if all the things above fail, it will set the text to starting(i have never had that happen to me)
    else:
        window['status'].update('Starting')
    



#defining the layout
layout = [ [sg.Text('Airplay', font=sfFontBeeg, size=1920, justification='center', text_color='white')],
		   [sg.Column([[sg.Image('airplay-final.png', size=(500,500), subsample=4)]], justification='center')],
           [sg.Text('Starting', font=sfFontNormal, size=1000, justification='center', text_color='white', key='status')]]

#starting the window
window = sg.Window('UxplayGUI', layout, location=(0,0), size=(1920,1080)) #you can replace the size attribute with your tv size in pixels

while True:
   #checking if the window is closed, with a 3 second timeout if nothing is recieved(to let the rest of the code execute)
    event, values = window.read(timeout=3)
    if event == sg.WIN_CLOSED:
        break    
    status()

#stopping uxplay(prob dont need to do this)    
child.sendcontrol('c')
#closing the window
window.close()
