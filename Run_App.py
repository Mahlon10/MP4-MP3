import customtkinter as ctk
import os
from MP4Convert import vid

#set root
root=ctk.CTk()
root.geometry('500x500')
root.title('MP4')
ctk.set_appearance_mode('dark')

#create a frame
frame=ctk.CTkFrame(master=root)
frame.pack(pady=20, padx=60,fill='both',expand=True)

#include a button
butt=ctk.CTkButton(master=frame,text='Convert',width=150,height=20,border_color='white',border_width=2,
                   hover=True,fg_color='blue',command=vid)
butt.pack(pady=200,padx=10)

root.mainloop()