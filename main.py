# ----------BLANKS----------
import random
from tkinter import *
#from tkinter import Tk, Label, PhotoImage, Entry, Button, END
root = Tk()
root.geometry("500x500")

# Reading the 3kwords file and assigning a random one to variable 'w'

with open("3kwords", "r") as f:
    w = random.choice(f.readlines())
w=w.lower()
sepword = []
dashes = []

index = -1
for char in w:
    if char != '\n':
        sepword.append(char)
print(f"{(len(sepword))} letters, 1 word!")
_l_w = Label(text=f"{len(sepword)} letters, 1 word!", anchor="s")
_l_w.pack()




#for char in sepword:
#    if inp in char:
#        print("ola")


#-----------------
for x in range(len(sepword)):
    dashes.append('-')
r = random.randint(0, (len(sepword)) - 1)
#TESTING ONLY
print(r)
print(f"word={w}")
print(f"sepword{sepword}")
#-----------------------------
for elem in sepword:
    index += 1
    if elem == sepword[r]:
        dashes[index] = sepword[r]
    if sepword[r] == sepword[-1]:
        dashes[-1] = sepword[r]

dash_lb = Label(text=" ".join(dashes), anchor="s", font="ComicSans")
dash_lb.pack()

# ----------GRAPHICS----------
img = ""



l=Label()
#SEVEN STAGES
def start():
    global img
    img = PhotoImage(file="4.png")
    l.configure(image=img)
    l.pack()


def first():
    global img
    img = PhotoImage(file="5.png")
    l.configure(image=img)
    l.pack()


def second():
    global img
    img = PhotoImage(file="6.png")
    l.configure(image=img)
    l.pack()


def third():
    global img
    img = PhotoImage(file="7.png")
    l.configure(image=img)
    l.pack()


def fourth():
    global img
    img = PhotoImage(file="8.png")
    l.configure(image=img)
    l.pack()


def fifth():
    global img
    img = PhotoImage(file="9.png")
    l.configure(image=img)
    l.pack()


def dead():
    global img
    img = PhotoImage(file="10.png")
    l.configure(image=img)
    l.pack()
    dash_lb.configure(text=f"The word was: {w}")
    _l_w.configure(text="---FAIL---")


start()

#INPUT-----

letters="a b c d e f g h i j k l m n o p q r s t u v w x y z".split()
print(f"let{letters}")
ent=Entry()
ent.focus_set()
ent.pack()

wrong_list=[]
killed=[]

done_lb=Label(text=f"All letters you have wrongly attempted: []", anchor="n", width=50)
done_lb.pack()
oof_counter=0
def button_pressed():
    global oof_counter
    global ent
    global inp

    where=-1
    inp = ent.get()
    if "".join(dashes).find("-")==-1:
        _l_w.configure(text="!!!Yay you win!!!")
    if inp.lower() not in wrong_list:
        if inp.lower() in letters:
            if inp.lower() not in sepword:
                wrong_list.append(inp.lower())
    conv=wrong_list
    "".join(conv)
    done_lb.configure(text=f"All letters you have wrongly attempted: {str(conv)}", anchor="n", width=50)

    if inp.lower() in letters:
        if inp.lower() in w.lower():
            for character in w.lower():
                where+=1
                if inp.lower()==character:
                    dashes[where]=inp.lower()
                    dash_lb.configure(text=" ".join(dashes))

        elif inp.lower() not in w.lower():
          if inp.lower() not in killed:
            killed.append(inp.lower())

            oof_counter+=1
            if oof_counter==0:
                start()
            if oof_counter==1:
                first()
            if oof_counter==2:
                second()
            if oof_counter==3:
                third()
            if oof_counter==4:
                fourth()
            if oof_counter==5:
                fifth()
            if oof_counter==6:
                dead()
    ent.delete(0, END)


    if inp.lower() not in letters:
        _l_w.configure(text="That's not a letter!")
        _l_w.after(2000,lambda: _l_w.configure(text=f"{len(sepword)} letters, 1 word!"))

def button_pressed_event(event):
    button_pressed()



complete=Button(root, text= "Okay", width= 20, command= button_pressed, ).pack(pady=20)
complete.bind("<Return>", button_pressed_event)


#INPUT PROCESSING--------------







