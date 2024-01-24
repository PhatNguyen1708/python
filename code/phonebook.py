from tkinter import *
from tkinter import ttk

#colors
co0 = "#ffffff"
co1 = "#000000"
co2 = "#4456F0"

window = Tk()
window.title ("")
window.geometry('700x600')
window.configure(background=co0)
window.resizable(width=FALSE, height=FALSE)

#Khung trang
frame_up = Frame(window, width=700, height= 50, bg=co2)
frame_up.grid(row=0, column=0, padx=0, pady=0)

frame_down = Frame(window, width=700, height= 150, bg=co0)
frame_down.grid(row=1, column=0, padx=0, pady=50)

frame_table = Frame(window, width=700, height= 100, bg=co2)
frame_table.grid(row=2, column=0, columnspan=2, padx=0, pady=50)

#frame up widgets
app_name = Label(frame_up, text="DANH BẠ",height= 1, font=('Verdana 17 bold',20),fg=co0,bg=co2 )
app_name.place(x=300,y=10)

#frame down widgets
#Phần Tên
l_name = Label(frame_down, text="Tên:",width=20,height=1,font=('Ivy 10'),bg=co0,anchor=NW)
l_name.place(x=10,y=20)
e_name = Entry(frame_down, width=25, justify='left',highlightthickness=1, relief="solid")
e_name.place(x=80,y=20)


window.mainloop()