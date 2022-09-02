import tkinter as tk
import winsound

# from mylib.mylib import Receiver
from mylib.mylib import Receiver

'''
Demonstrate how to use a thread that runs parallel to the Tkinter event loop.
It uses a queue to communicate between Tkinter and the parallels thread
'''

receiver = Receiver()

def send():
    receiver.put("Button was pressed")
    # winsound.Beep(340, 200)
    winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS)
    

root = tk.Tk()

# Open window having dimension 100x100
root.geometry('100x50')
 
# Create a Button
btn = tk.Button(root, text = 'Click me !', bd = '5',
                          command = send)
 
# Set the position of button on the top of window.  
btn.pack(side = 'top')   
 
root.mainloop()