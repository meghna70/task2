from doctest import master
from logging import root
from tkinter import Button, Entry, Label, StringVar
from tkinter.tix import Tk
from _tkinter import *
from tkinter.ttk import LabelFrame
from turtle import left
import pafy
import youtube_dl


Root= Tk()
Root.geometry("600x400")
Root.config(bg="#ADD8E6")
Root.title('YouTube Video Downloader')

Label(Root, text="YOUTUBE DOWNLOADER", font='san-serif 25 bold').place(x = 90, y = 14)
link = StringVar() # Specifying the variable type
Label(Root, text="Paste your link above", font='san-serif 15 bold').place(x=200, y=130)
link_enter = Entry(Root, width=65, textvariable=link).place(x=95, y=100)

format= StringVar() # Specifying the variable type
Label(Root, text="Mention the format", font='san-serif 15 bold').place(x=220, y=250)
link_enter = Entry(Root, width=35, textvariable=format).place(x=210, y=280)




def download():
    url = link.get()
    store_video = pafy.new(url)
    video = store_video.getbest(preftype=format.get()) # This captures he streams available for downloaded for the video i.e. 360p, 720p, 1080p. etc. 
    video.download(quiet=False)
    Label(Root, text="Downloaded", font="arial 15").place(x=100, y=260)

def getURL():
    value=link.get()
    Label(Root, text=value, font="arial 15").place(x=200, y=320)


def extension():

    url = link.get()
    store_video = pafy.new(url)
    streams = store_video.allstreams

    possible_ext=[]
    for s in streams:
      if s.extension not in possible_ext:
           possible_ext.append(s.extension)
    
    extension_frame = LabelFrame( master, text="Available extensions", width=500, height=50).place(x=50, y=170)
    var=0
    for i in possible_ext:
      label = Label(extension_frame, text= i).place(x=50+var, y=190)
      print(var)
      #this creates a new label to the GUI
      var+=30
    label.pack()

Button(Root, text='Get extension', font='san-serif 16 bold', bg='grey', padx=2,command=extension).place(x=230, y=170)
Button(Root, text='Download', font='san-serif 16 bold', bg='grey', padx=2,command=download).place(x=200, y=350)


Root.mainloop()




