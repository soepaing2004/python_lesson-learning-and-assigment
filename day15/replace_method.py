from tkinter import *

window=Tk()
window.title("Welcome")
window.geometry('500x500')
button=Button(window,text="hello")
button.place(height=50,x=100,y=250)

button1=Button(window,text="width")
button1.place(width=60,x=200,y=200)

button2=Button(window,text="Relheight")
button2.place(relheight=0.6)

button3=Button(window,text="relwidth")
button3.place(relwidth=0.2)

button4=Button(window,text="x")
button4.place(x=400)

button5=Button(window,text="y")
button5.place(y=450)

window.mainloop()
