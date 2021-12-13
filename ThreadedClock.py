import tkinter as tk
import time
import threading
import queue

SLEEP_TIME = 1

def update_clock1(sleep_time):
    clock1.configure(text = time.strftime("%H:%M:%S"))
    #time.sleep(sleep_time) # This will freeze the GUI for 1 second
    root.after(1000, update_clock1, SLEEP_TIME)

def update_clock2(sleep_time):
    while True:
        clock2.configure(text = time.strftime("%H:%M:%S"))
        time.sleep(sleep_time)

def update_clock3(sleep_time):

    def clock3_tread(sleep_time):
        clock3.configure(text = time.strftime("%H:%M:%S"))
        time.sleep(sleep_time) # This will NOT freeze the GUI for 1 second

    #threading.Thread(target = lambda: clock3_tread(sleep_time)).start() # using lambda
    #root.after(1000, lambda : update_clock3(SLEEP_TIME)) # using lambda
    threading.Thread(target = clock3_tread, args=[sleep_time]).start()  # using args   
    root.after(1000, update_clock3, SLEEP_TIME) # using args




root = tk.Tk()
root.title('Timer')

clock1 = tk.Label(root, text="", font=('Helvetica', 48), fg='red')
clock1.pack(pady = 0)
clock2 = tk.Label(root, text="", font=('Helvetica', 48), fg='green')
clock2.pack(pady = 0)
clock3 = tk.Label(root, text="", font=('Helvetica', 48), fg='blue')
clock3.pack(pady = 0)


update_clock1(SLEEP_TIME)
threading.Thread(target = lambda: update_clock2(SLEEP_TIME), daemon = True).start()
update_clock3(SLEEP_TIME)

# Clock 4 via Queue
q_clock4 = queue.Queue()

def set_clock4(q): 
    while True:
        q.put(time.strftime("%H:%M:%S"))
        time.sleep(1)

def update_clock4(q):
    if not q.empty():        
        clock4.configure(text = q.get())
    root.after(100, update_clock4, q_clock4)

clock4 = tk.Label(root, text="", font=('Helvetica', 48), fg='yellow')
clock4.pack(pady = 0)

threading.Thread(target = set_clock4, args = [q_clock4], daemon = True).start()
update_clock4(q_clock4)

# Start main tk loop
root.mainloop()