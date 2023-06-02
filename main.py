from tkinter import *
from datetime import datetime




temp = 0
after_id = ''


def tick():
    global temp, after_id
    after_id = root.after(1000, tick)
    f_time = datetime.fromtimestamp(temp).strftime("%M:%S")
    label1.configure(text=str(f_time))
    temp += 1


def start_tick():
    butten_start.pack_forget()
    butten_stop.pack()
    tick()


def stop_tick():
    butten_stop.pack_forget()
    butten_contine.pack()
    butten_reset.pack()
    root.after_cancel(after_id)


def contine():
    butten_contine.pack_forget()
    butten_reset.pack_forget()
    butten_stop.pack()
    tick()


def reset():
    global temp
    temp = 0
    label1.configure(text="00:00")
    butten_contine.pack_forget()
    butten_reset.pack_forget()
    butten_start.pack()


root = Tk()
root.title("секундомер")
root.resizable(width=False, height=False)

root.geometry('300x200')

label1 = Label(root, width=10, font=('Comic Sans MS', 30), text='00:00')
label1.pack()

butten_start = Button(root, text="START", font=('Comic Sans MS', 20), width=15, command=start_tick)
butten_stop = Button(root, text="STOP", font=('Comic Sans MS', 20), width=15, command=stop_tick)
butten_reset = Button(root, text="reset", font=('Comic Sans MS', 20), width=15, command=reset)
butten_contine = Button(root, text="contine", font=('Comic Sans MS', 20), width=15, command=contine)

butten_start.pack()
butten_stop.pack()

root.mainloop()
