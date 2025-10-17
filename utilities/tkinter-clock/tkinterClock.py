import time
import tkinter as tk

root = tk.Tk()
root.title("Clock") #Title of the window
root.geometry('400x100+700+300') #Size of the window
root.configure(bg='darkblue') 

label = tk.Label(root, text='Hello, I am a Label')
label.config(fg='white', bg='darkblue', font=('Arial', 50, 'bold'))
label.pack()

def clock():
    label.config(text=time.strftime('%H:%M:%S'))
    root.after(1000, clock) #Update every second

clock()
root.mainloop()