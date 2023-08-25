#import the moviepy library
import moviepy.editor
#import tkinter libraries
from tkinter import filedialog,messagebox
from tkinter.filedialog import *
#create a function
def vid():
    video=askopenfilename()
#display the loading message
    if video:
        messagebox.showinfo('Load', 'Loading....')
    video=moviepy.editor.VideoFileClip(video)
#transmission codec
    audio=video.audio
    files=[('mp3', '*.mp3')]
##export to mp3 format
    url=filedialog.asksaveasfilename(defaultextension='.mp3', filetypes=files)
    if url:
        audio.write_audiofile(url)
        messagebox.showinfo('File Saved', 'Audio File Complete')


