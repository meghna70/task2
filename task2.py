from tkinter import Button, Entry, Label, StringVar
from tkinter.tix import Tk
from _tkinter import *
import pafy
import youtube_dl


Root= Tk()
Root.geometry("600x400")
Root.config(bg="#EC7063")
Root.title('YouTube Video Downloader')

Label(Root, text="YOUTUBE DOWNLOADER", font='san-serif 14 bold').place( relx = 0.3, rely = 0)
link = StringVar() # Specifying the variable type
Label(Root, text="Paste your link here", font='san-serif 15 bold').place(x=150, y=55)
link_enter = Entry(Root, width=70, textvariable=link).place(x=30, y=85)

def download():
    url = link.get()
    store_video= pafy.new(url)
    video = store_video.getbest() # This captures the streams available for downloaded for the video i.e. 360p, 720p, 1080p. etc.
    
    video.download()
    Label(Root, text="Downloaded", font="arial 15").place(x=100, y=120)

def getURL():
    value=link.get()
    Label(Root, text=value, font="arial 15").place(x=100, y=120)

Button(Root, text='Download', font='san-serif 16 bold', bg='red', padx=2,command=download).place(x=100, y=150)


Root.mainloop()




