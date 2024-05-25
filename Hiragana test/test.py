import os
import random
from tkinter import *
from PIL import ImageTk, Image

wrong_guesses = 0
correct_guesses = 0
picture_name = ''
hiragana = {}
for filename in os.listdir('Hiragana pictures'):
    hiragana[os.path.join('Hiragana pictures\\' + filename)] = filename.split('.')[0]
hiragana_photos = [i for i in hiragana.keys()]


def next():
    global picture_name
    picture_name = random.choice(hiragana_photos)
    img2 = ImageTk.PhotoImage(Image.open(picture_name))
    label.configure(image=img2)
    label.image = img2
    answer.delete(0, END)

def validate():
    global correct_guesses, wrong_guesses
    text = answer.get()
    if text == hiragana[picture_name]:
        correct_guesses += 1
        label3.configure(text=f'Correct {correct_guesses}', )
        answer.delete(0, END)
        next()
    else:
        wrong_guesses += 1
        label2.configure(text=f'Wrong: {wrong_guesses}')
        answer.delete(0, END)
        next()


window = Tk()
window.geometry('500x300')
frame = Frame(window)
frame2 = Frame(window)
frame3 = Frame(window)
img = random.choice(hiragana_photos)
picture_name = img
img = ImageTk.PhotoImage(Image.open(img))
label = Label(frame, image=img)
label.grid(row=0, column=0)
answer = Entry(frame2, font=50)
answer.grid(row=0, column=0)
next_button = Button(frame3, text='Next', command=next, font=20)
next_button.grid(row=0, column=0)
check_correct_button = Button(frame3, text='Check Correct', command=validate, font=20)
check_correct_button.grid(row=0, column=1, padx=30)
label2 = Label(window, text=f'Wrong: {wrong_guesses}', font=30)
label3 = Label(window, text=f'Correct {correct_guesses}', font=30)
label2.place(x=90, y=280)
label3.place(x=20, y=280)
frame.place(x=200, y=50)
frame2.place(x=170, y=170)
frame3.place(x=170, y=200)
window.mainloop()
