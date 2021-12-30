# pip install qrcode[pil]

import pyqrcode #qrcode
from tkinter import *
from tkinter import messagebox

ws = Tk()
ws.title('PythonGuides')
ws.geometry('400x200')
ws.config(bg='#4a7a8c')


def generate():
    img = pyqrcode.make(msg.get()) ##qrcode
    type(img) 
    img.save(f'{save_name.get()}.png')
    Label(ws, text='File Saved!', fg='green').pack()

frame = Frame(ws, bg='#4a7a8c')
frame.pack(expand=True)

Label(
    frame,
    text='URL',
    font = ('Times', 18),
    bg='#4a7a8c'
    ).grid(row=0, column=0, sticky='w')

msg = Entry(frame)
msg.grid(row=0, column=1)

Label(
    frame,
    text='Save as',
    font = ('Times', 18),
    bg='#4a7a8c',
).grid(row=1, column=0, sticky='w')

save_name = Entry(frame)
save_name.grid(row=1, column=1)

btn = Button(
    ws, 
    text='Generate QR code',
    command=generate
    )
btn.pack()

ws.mainloop()