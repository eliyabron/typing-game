import _thread  # thread module imported
import random
import tkinter
from tkinter import Label
import time
stop = 0
place = 0
game_over = 0
a=0
text_label=""
r = tkinter.Tk()
r.geometry("400x300")

def replay():
   global stop
   stop = 0
   list1 = r.place_slaves()
   for index in list1:
        index.place_forget()
        r.update()
   start_game()



def check(event=None):
    global place
    global stop
    string = e1.get()
    if string == text_label and place <= 300:
        l3.configure(text="correct", bg="green", fg="black")
        l3.place(x=20,y=120)
        stop = 1
        

    elif string != text_label and place <= 300:
        l3.configure(text="try again", bg="blue", fg="white")
        l3.place(x=20,y=120)
        
    else:
        l3.configure(text="you lost", bg="red", fg="black")
        l3.place(x=20,y=120)
        


def start_game():
   global text_label
   global place
   global stop
   global game_over
   list1 = r.place_slaves()
   for index in list1:
        index.place_forget()
   text_label=random.choice(my_list)
   l1.configure(text= text_label)
   l1.place(x=0,y=40)
   exit_button.place(x=0,y=0)
   l2.place(x=0,y=80)
   e1.delete(0, 'end')
   e1.place(x=70,y=80)
   l4.place(x=300,y=0)
   for place_x in range(303):
        if stop == 0 and place_x<=301:
            place = place_x
            time.sleep(0.01)
            l1.place(x=place_x,y=40)
            r.update()
        else:
            l1.place_forget()
            if stop==0:
                l3.configure(text="you lost", bg="red", fg="black")
                l3.place(x=20, y=120)    
   replay_button.place(x=0,y=40)           
    
my_list =[]
f = open("words.txt", "r")
tmp = f.read().splitlines()
for i in tmp:
   my_list.append(i)


l1 = tkinter.Label(r, text="text", fg="black")
l2 = Label(r, text="type here:")
l3 = tkinter.Label(r, text="correct", bg="green", fg="black")
l4 = Label(r, bg="black",fg="white",text="finish line")
e1 = tkinter.Entry(r)
start_button = tkinter.Button(r, text='start', activebackground='#78d6ff', command=start_game)
start_button.place(x=200,y=100)
exit_button = tkinter.Button(r, text='Exit', activebackground='#78d6ff', command=r.destroy)
exit_button.place(x=100,y=100)
replay_button = tkinter.Button(r, text='replay', activebackground='#78d6ff', command=replay)
e1.bind('<Return>',check)
#stuck in loop
r.mainloop()