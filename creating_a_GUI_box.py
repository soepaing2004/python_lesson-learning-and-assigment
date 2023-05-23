from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox

window =Tk()
window.title("Welcome")

label=Label(window,text="Hello",font=("Arial",20))
label.grid(column=0,row=0)

window.geometry("350x250")

combo=Combobox(window)
combo['values']=(1,2,3,4,5,"Hello")
combo.current(0)
combo.grid(column=0,row=2)

check_state=BooleanVar()
check_state.set(True)

dataType=IntVar()

radio1=Radiobutton(window,text="First",value=1,variable=dataType)
radio1.grid(column=3,row=0)
radio2=Radiobutton(window,text="Second",value=2,variable=dataType)
radio2.grid(column=3,row=1)
radio3=Radiobutton(window,text="Third",value=3,variable=dataType)
radio3.grid(column=3,row=2)
def click():
    lable2=Label(window,text="clicked")
    lable2.grid(column=1,row=2)
    print(combo.get())
    x=user_input.get()
    print(x)
    print(check_state.get())
    print(dataType.get())
    print(messagebox.askokcancel())

check=Checkbutton(window,text='Choose',command=click,var=check_state)
check.grid(column=0,row=4)

button=Button(window,text="Click",command=click)
button.grid(column=2,row=0)

user_input=Entry(window,width=10)
user_input.grid(column=0,row=3)
user_input.focus()

spin=Spinbox(window,from_=0,to=100,width=10)
spin.grid(column=4,row=3)
window.mainloop() #endlessloop






























