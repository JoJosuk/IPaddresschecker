import tkinter as tk
import customtkinter as ctk
import socket
from tkinter import ttk

iplist1=[]
iplist2=[]
def submitvalues(Event=None):   
    ip1 = entrystr.get()
    ip2 = entrystr2.get()
   
    if ip1!='' and ip1 not in iplist1:
        iplist1.append(ip1)
    if ip2!='' and ip2 not in iplist2:
        iplist2.append(ip2)
    for ip in iplist1:
        try:
            socket.inet_aton(ip)
            label3.configure(text="IP1 exists\n\n\n", fg_color="green")
        except socket.error:
            label3.configure(text="IP1 does not exist,clearing latest", fg_color="red")
            iplist1.clear()
            break;
    for ip in iplist2:
        try:
            socket.inet_aton(ip)
            label4.configure(text="IP2 exists", bg="green")
        except socket.error:
            label4.configure(text="IP2 does not exists,clearing latest ", bg="red")
            iplist2.clear()
            break;
    print(iplist1,iplist2)        
    m.after(10000, submitvalues)

ctk.set_appearance_mode("system")
ctk.set_default_color_theme("blue")   
m=ctk.CTk()

m.title('IP Checker')
m.geometry("800x500")


label = ctk.CTkLabel(master=m, text="Place 1")
label.pack(padx=20,pady=20)
entrystr= ctk.CTkEntry(master=m, width=100)
entrystr.pack()
label2= ctk.CTkLabel(master=m, text="place2", width=20)
label2.pack()
entrystr2= ctk.CTkEntry(master=m, width=100)
entrystr2.pack()
label3 = ctk.CTkLabel(master=m, text="", width=30,height=10 )
label3.pack()
label4 = ctk.CTkLabel(master=m, text="", width=30,height=10)
label4.pack()
stopper = ctk.CTkButton(master=m, text='Stop', width=25, command=m.destroy)
submit=ctk.CTkButton(master=m,text='Submit',width=25,command=submitvalues)
m.bind('<Return>',submitvalues)
submit.pack()
stopper.pack()
m.mainloop()



