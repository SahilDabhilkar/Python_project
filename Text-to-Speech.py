from tkinter import *
import gtts
import playsound

top = Tk()

top.minsize(450, 300)

te1 = Label(text="Text-To-Speech Converter")
te1.pack()

text = Entry()
text.pack()

btn = Button(top, text="Convert", command=lambda: [speech(text.get())])
btn.pack()

btn1 = Button(top, text="Quit", command=lambda: [top.destroy()])
btn1.pack()


def speech(text):
    sound = gtts.gTTS(text, lang="hi")
    sound.save("/Users/sahildabhilkar/Desktop/pythonProject/music/welcome.mp3")
    playsound.playsound("/Users/sahildabhilkar/Desktop/pythonProject/music/welcome.mp3")


top.mainloop()
