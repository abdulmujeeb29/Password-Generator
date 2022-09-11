import tkinter as tk
from tkinter import *
import string,random
import pyperclip

def generator():
     characters= name_box.get() + number_box.get()
     password_length=int(length_box.get())
     password=[]
     for _ in range(password_length):
         password.append(random.choices(characters))
     password_field.insert(0,password)

def copy():
     random_password=password_field.get()
     pyperclip.copy(random_password)


root=Tk()
root.config(bg='gray')
choice=IntVar()
Font=('calibri light',20,'italic')

passwordlabel=Label(root,text='Secured Password Generator',font=('calibri light',25,'bold'),bg='gray',fg= 'white')
passwordlabel.grid(pady=10)

namelength=Label(root,text='Enter a name::',font=('calibri light',20,'bold'),bg='gray',fg= 'white')
namelength.grid()
name_box=Entry(root,width=25,bd=2,font=Font)
name_box.grid()

numberlength=Label(root,text='Enter a secret number::',font=('calibri light',20,'bold'),bg='gray',fg= 'white')
numberlength.grid()
number_box=Entry(root,width=25,bd=2,font=Font)
number_box.grid()




passwordlength=Label(root,text='Password Length:',font=('calibri light',20,'bold'),bg='gray',fg= 'white')
passwordlength.grid()

length_box=Spinbox(root,from_=5,to_ =18,width=10,font=Font)
length_box.grid()

generatebutton=Button(root,text='Generate:',font=Font,command=generator)
generatebutton.grid(pady=5)

password_field=Entry(root,width=25,bd=2,font=Font)
password_field.grid()

copybutton=Button(root,text='Copy:',font=Font,command=copy)
copybutton.grid(pady=5)

root.mainloop()

