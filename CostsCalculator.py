__author__ = 'Qingwu'

# import the tkinter module
from tkinter import *
from tkinter.messagebox import *

MODES = [("USD", "1"),
         ("EUR", "2"), ]
USDCNY = "6.22"
EURCNY = "7.6"


# make window center of the screen
def make_window_center(rt_win):
    # rt_win.resizable(False,False) #can not change window size
    rt_win.update()  # update window, must do
    curWidth = rt_win.winfo_reqwidth()     # get current width
    curHeight = rt_win.winfo_height()      # get current height
    scnWidth, scnHeight = rt_win.maxsize()  # get screen width and height
    # now generate configuration information
    tmpcnf = '%dx%d+%d+%d' % (curWidth, curHeight, (scnWidth-curWidth)/2, (scnHeight-curHeight)/2)
    rt_win.geometry(tmpcnf)


# about message box
def aboutbox():
    showinfo("About", "Costs Calculator 2.0\nQingwu Zhang\n\nFor Sylvia Zou")


# calculate
def calculate():
    us_price_value = float(us_price.get())
    us_trans_cost_value = float(us_trans_cost.get())
    in_trans_cost_value = float(in_trans_cost.get())
    consumer_tax_value = float(consumer_tax.get())
    excharge_rate_value = float(excharge_rate.get())
    bought_rate_value = float(bought_rate.get())
    total_price = ((us_price_value * (1+consumer_tax_value) + us_trans_cost_value)*(1+bought_rate_value)
                   ) * excharge_rate_value + in_trans_cost_value
    total.set(round(total_price, 2))


# display function
def display(rt_win, string, StringVar, default_value):
    frame = Frame(rt_win)
    label = Label(frame, text=string)
    entry = Entry(frame, textvariable=StringVar)
    if default_value == 0:
        entry.focus()
    label.config(anchor="e", width=20, pady=3)
    label.pack(side=LEFT)
    entry.pack(side=LEFT, padx=8)
    if default_value != 0:
        entry.insert(1, default_value)
    frame.pack()


def call_radio_button():
    entry.delete(0, END)
    if v.get() == 1:
        entry.insert(1, USDCNY)
    else:
        entry.insert(1, EURCNY)
    if us_price.get() != "":
        calculate()

if __name__ == '__main__':
    root = Tk()  # create a root window
    root.title("Costs Calculator")
    # root.geometry("480x400+450+300")
    root.iconbitmap("CostsCalculator.ico")
    menubar = Menu(root)       # create a toplevel menu
    root.config(menu=menubar)  # display the menu
    root.bind("<Return>", calculate)  # bind ENTRY
    calbutton = Button(root, text="Calculate", command=calculate)  # create a button
    calbutton.pack(side=BOTTOM, padx=0, pady=5)  # display the button

    # create variables
    us_price = StringVar()
    us_trans_cost = StringVar()
    in_trans_cost = StringVar()
    consumer_tax = StringVar()
    excharge_rate = StringVar()
    bought_rate = StringVar()
    total = StringVar()

    # display radiobutton
    v = IntVar()
    v.set("1")  # initialize
    frame = Frame(root)
    label = Label(frame, text="Type: ")
    label.config(anchor="e", width=20, pady=3)
    label.pack(side=LEFT)
    for (text, value) in MODES:
        rb = Radiobutton(frame, text=text, variable=v, value=value, command=call_radio_button)
        rb.pack(side=LEFT, padx=10)
    frame.pack()

    display(root, "Price: ", us_price, 0)
    display(root, "Shipping cost: ", us_trans_cost, 8.5)
    display(root, "Intl shipping cost (RMB): ", in_trans_cost, 160)
    display(root, "Sales tax rate: ", consumer_tax, 0.07)
    # display(root, "Excharge rate: ", excharge_rate, 6.3)

    frame = Frame(root)
    label = Label(frame, text="Excharge rate: ")
    entry = Entry(frame, textvariable=excharge_rate)
    label.config(anchor="e", width=20, pady=3)
    label.pack(side=LEFT)
    entry.pack(side=LEFT, padx=8)
    entry.insert(1, "6.3")
    frame.pack()

    display(root, "My purchase rate: ", bought_rate, 0.1)

    Label(text="\nTotal (RMB): ", ).pack()
    Label(textvariable=total, font="Helvetica -20 bold").pack()

    # file menu
    filemenu = Menu(menubar, tearoff=0)  # create file menu
    menubar.add_cascade(label="File", menu=filemenu)
    filemenu.add_command(label="Exit", command=root.destroy)

    # help menu
    helpmenu = Menu(menubar, tearoff=0)  # create help menu
    menubar.add_cascade(label="Help", menu=helpmenu)
    helpmenu.add_command(label="About...", command=aboutbox)

    # make_window_center(root) #run this at last
    # root.update()
    root.mainloop()  # create an event loop
