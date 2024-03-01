from tkinter import *

# Data
cs2v = 0.314
v2cs = 3.182
cs2ow = 3.333
v2ow = 10.606
rs = 0
fs = 0

# Functions
def from_cs():
    global fs
    fs = "cs"
    from_lable.config(text="From: CS2 ")
    from_cs_btn.config(bg="green")
    from_v_btn.config(bg="white")

def from_v():
    global fs
    fs = "v"
    from_lable.config(text="From: Valorant ")
    from_cs_btn.config(bg="white")
    from_v_btn.config(bg="green")

def to_cs():
    to_lable.config(text="To: CS2")
    to_cs_btn.config(bg="green")
    to_v_btn.config(bg="white")
    to_ow_btn.config(bg="white")
    global num
    global rs
    if fs == "v":
        num = v2cs
        rs = v2cs * float(from_s.get())
    elif fs == "cs":
        num = 1
        rs = 1
    rs = round(rs, 3)
    result.config(text=f"New sensitivity is: {rs}")

def to_v():
    to_lable.config(text="To: Valorant")
    to_cs_btn.config(bg="white")
    to_v_btn.config(bg="green")
    to_ow_btn.config(bg="white")
    global num
    global rs
    if fs == "cs":
        num = cs2v
        rs = cs2v * float(from_s.get())
    elif fs == "v":
        num = 1
        rs = 1
    rs = round(rs, 3)
    result.config(text=f"New sensitivity is: {rs}")

def to_ow():
    to_lable.config(text="To: Overwatch")
    to_cs_btn.config(bg="white")
    to_v_btn.config(bg="white")
    to_ow_btn.config(bg="green")
    global num
    global rs
    if fs == "v":
        rs = v2ow * float(from_s.get())
        num = v2ow
    elif fs == "cs":
        num = cs2ow
        rs = cs2ow * float(from_s.get())
    rs = round(rs, 3)
    result.config(text=f"New sensitivity is: {rs}")

def update_result(event=None):
    global num
    global rs
    rs = num * float(from_s.get())
    rs = round(rs, 3)
    result.config(text=f"New sensitivity is: {rs}")

# Windows setup
win = Tk()
win.title("Sensitivity Converter")
win.geometry("400x250")
win.resizable(False, False)
win.config(bg="#27262E")
win.attributes("-alpha", 1)
win.attributes("-topmost", 1)

# Buttons
button_frame = Frame(win, bg="#27262E")
button_frame.pack()
from_cs_btn = Button(button_frame, text="From CS2", command=from_cs)
from_v_btn = Button(button_frame, text="From Valorant", command=from_v)
from_cs_btn.pack(side=LEFT, padx=10, pady=10)
from_v_btn.pack(side=LEFT, padx=10, pady=10)

# Entry
entry_frame = Frame(win, bg="#27262E")
entry_frame.pack()
from_lable = Label(entry_frame, bg="#27262E", fg="white", text="From:")
from_lable.pack(padx=10)
from_s = Entry(entry_frame)
from_s.config(bg="black", fg="white", justify='center')
from_s.pack(pady=10)
to_lable = Label(entry_frame, bg="#27262E", fg="white", text="To:")
to_lable.pack(padx=10)


from_s.bind("<KeyRelease>", update_result)

# Buttons
button_frame2 = Frame(win, bg="#27262E")
button_frame2.pack()
to_cs_btn = Button(button_frame2, text="To CS2", command=to_cs)
to_v_btn = Button(button_frame2, text="To Valorant", command=to_v)
to_ow_btn = Button(button_frame2, text="To Overwatch2", command=to_ow)
to_cs_btn.pack(side=LEFT, padx=10, pady=5)
to_v_btn.pack(side=LEFT, padx=10, pady=5)
to_ow_btn.pack(side=LEFT, padx=10, pady=5)

# Result
result = Label(bg="#27262E", fg="white", text=f"New sensitivity: {rs}")
result.pack(pady=20)

# Start the main event loop
win.mainloop()
