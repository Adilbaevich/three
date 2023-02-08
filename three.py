import tkinter
import webbrowser
from tkinter import messagebox

window = tkinter.Tk()
window.resizable(False, False)
window.geometry('400x500')
window['bg'] = 'gray'

def search():
    webbrowser.open('https://github.com/login?return_to=' + ent.get() + ent1.get())
    if len('ent') == 0 and len('ent1') == 0:
        messagebox.showinfo(message='Fill in the feild!')


qr = tkinter.PhotoImage(file='./images/лого.png')
label_photo = tkinter.Label(image=qr)
label_photo.place(x=40, y=45, width=350, height=180)



lbl = tkinter.Label(text='Username / email : ')
lbl['bg'] = 'gray'
lbl['font'] = 'Roboto 12'
lbl.place(x=50, y=240)



lbl1 = tkinter.Label(text='Login')
lbl1['font'] = 'Roboto 15'
lbl1['bg'] = 'gray'
lbl1.place(x=0, y=0)

lbl2 = tkinter.Label(text='Password :')
lbl2['bg'] = 'gray'
lbl2['font'] = 'Roboto 12'
lbl2.place(x=50, y=320)


ent = tkinter.Entry(width=40)
ent.place(x=70, y=270)
ent.focus()

ent1 = tkinter.Entry(width=40)
ent1.place(x=70, y=350)

btn = tkinter.Button(text='   Login   ', command=search)
btn['fg'] = 'white'
btn['bg'] = 'green'
btn['font'] = 'Roboto 12'
btn.place(x=150, y=390)

window.mainloop()