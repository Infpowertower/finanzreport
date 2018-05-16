import log_helper as log
import database_helper as db
from threading import Thread
import time
import tkinter as tk

'''
class startGui(Thread):

    def __init__(self):
        """Constructor. """
        self.counter = 10
        Thread.__init__(self)

    def run(self):
        root = tk.Tk()
        root.title("Finanzreport")
        # label = tk.Label(root, fg="green")
        # label.pack()
        # self.counter_label(label)
        w = tk.Label(root, text="Deine Zeit läuft ab!")
        w.pack()
        button = tk.Button(root, text='Stop', width=25, command=root.destroy)
        button.pack()

        root.mainloop()
        root.quit()
'''


class Gui:
    def __init__(self):
        self.mainWindow = tk.Tk()
        self.mainWindow.geometry("800x600")
        self.mainWindow.title("Finanzreport")
        # self.mainWindow.configure(background='white')
        self.mainWindow.tk_setPalette(background='#FFFFFF')

    def start(self):  # Start
        label = tk.Label(self.mainWindow)
        label.pack()
        get_current_user(label)
        w = tk.Label(self.mainWindow, text="Work in progress")
        w.pack()
        canvas = tk.Canvas(self.mainWindow)
        canvas.pack()
        canvas.create_text(0, 0, text="TEST")
        self.mainWindow.mainloop()

    def quit(self):
        if tk.messagebox.askyesno('App', 'Are you sure you want to quit?'):
            # In order to use quit function, mainWindow MUST BE an attribute of Interface.
            self.mainWindow.destroy()
            self.mainWindow.quit()


arr_colour = [0] * 6
reverse = False


def count_colour():
    global arr_colour
    global reverse
    for n, i in enumerate(arr_colour):
        if reverse:
            if not i <= 0:
                arr_colour[n] -= 1
                return
        else:
            if not i >= 16:
                arr_colour[n] += 1
                return
    reverse = not reverse


def convert_to_hexstring(num):
    if num < 10:
        return str(num)
    elif num == 10:
        return "a"
    elif num == 11:
        return "b"
    elif num == 12:
        return 'c'
    elif num == 13:
        return 'd'
    elif num == 14:
        return 'e'
    else:
        return 'f'


def get_current_user(label):
    global arr_colour
    label.config(text="Welcome Mr Robert Richter!", font=("Helvetica", 24), fg="#{}".format(''.join(convert_to_hexstring(e) for e in arr_colour)))

    def rainbow_colours():
        global arr_colour
        count_colour()
        label.config(fg="#{}".format(''.join(convert_to_hexstring(e) for e in arr_colour)))
        label.after(100, rainbow_colours)
    rainbow_colours()


def get_current_saldo(label):
    label.config(text="25000$", fg="grey")


def init_logs():
    log.init_log('main')
    log.init_log('database')
    log.init_log('logging')
    log.init_log('sql')


if __name__ == "__main__":
    init_logs()

    # gui = startGui()
    # gui.setName('GUI')
    # Start running the threads!
    # gui.start()
    # Wait for the threads to finish...
    # gui.join()
    interface = Gui()
    interface.start()
    print('Main Terminating...')
