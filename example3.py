from tkinter import *                                                                           #1
from tkinter import ttk                                                                         #2

def calculate(*args):                                                                           #3
    try:                                                                                        #4
        value = float(feet.get())                                                               #5
        meters.set((0.3048 * value * 10000.0 + 0.5)/10000.0)                                    #6
    except ValueError:                                                                          #7
        pass                                                                                    #8
    
root = Tk()                                                                                     #9
root.title("Feet to Meters")                                                                    #10

mainframe = ttk.Frame(root, padding="3 3 12 12")                                                #11
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))                                            #12
mainframe.columnconfigure(0, weight=1)                                                          #13
mainframe.rowconfigure(0, weight=1)                                                             #14

feet = StringVar()                                                                              #15
meters = StringVar()                                                                            #16

feet_entry = ttk.Entry(mainframe, width=7, textvariable=feet)                                   #17
feet_entry.grid(column=2, row=1, sticky=(W, E))                                                 #18

ttk.Label(mainframe, textvariable=meters).grid(column=2, row=2, sticky=(W, E))                  #19
ttk.Button(mainframe, text="Calculate", command=calculate).grid(column=3, row=3, sticky=W)      #20

ttk.Label(mainframe, text="Feet").grid(column=3, row=1, sticky=W)                               #21
ttk.Label(mainframe, text="Is Equivalent To : ").grid(column=1, row=2, sticky=E)                   #22
ttk.Label(mainframe, text="meters :").grid(column=3, row=2, sticky=W)                             #23

for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)                   #24

feet_entry.focus()                                                                              #25
root.bind('<Return>', calculate)                                                                #26

root.mainloop()                                                                                 #27
