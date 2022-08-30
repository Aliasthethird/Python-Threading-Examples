import tkinter as tk
import time
import winsound


from lib.lib import Receiver
receiver = Receiver()


def send():
    receiver.put("Button was pressed")
    # winsound.Beep(340, 200)
    winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS)
    

root = tk.Tk()

# Open window having dimension 100x100
root.geometry('100x100')
 
# Create a Button
btn = tk.Button(root, text = 'Click me !', bd = '5',
                          command = send)
 
# Set the position of button on the top of window.  
btn.pack(side = 'top')   
 
root.mainloop()