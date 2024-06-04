from tkinter import *

window = Tk()
window.geometry('400x500')
window.title('Position')

frame1 = LabelFrame(text='Frame 1', width=300, height=100)
frame2 = LabelFrame(text='Frame 2', width=300, height=100)
frame3 = LabelFrame(text='Frame 3', width=300, height=100)

button = Button(frame1, text='Click Me')
button2 = Button(frame2, text='Click Me')
button3 = Button(frame3, text='Click Me')


frame1.pack(padx=30, pady=10)
frame2.pack(padx=30, pady=10)
frame3.pack(padx=30, pady=10)

button.pack(padx=10, pady=10)
button2.pack(padx=10, pady=10)
button3.pack(padx=10, pady=10)

mainloop()