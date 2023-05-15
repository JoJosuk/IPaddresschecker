import tkinter as tk
import socket

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
            label3.config(text="IP1 exists", bg="green")
        except socket.error:
            label3.config(text="IP1 does not exist,clearing latest", bg="red")
            iplist1.clear()
            break;
    for ip in iplist2:
        try:
            socket.inet_aton(ip)
            label4.config(text="IP2 exists", bg="green")
        except socket.error:
            label4.config(text="IP2 does not exists,clearing latest ", bg="red")
            iplist2.clear()
            break;
    print(iplist1,iplist2)        
    m.after(10000, submitvalues)
   
m=tk.Tk()

m.title('IP Checker')
m.geometry("800x800")

spacer1 = tk.Label(m, text="")
spacer1.grid(row=4, column=0)
spacer1.pack()
label = tk.Label(m, text="place1", width=20, bg="white")
label.pack()
entrystr= tk.Entry(m, width=100, borderwidth=5)
entrystr.pack()
label2= tk.Label(m, text="place2", width=20, bg="white")
label2.pack()
entrystr2= tk.Entry(m, width=100, borderwidth=5)
entrystr2.pack()
label3 = tk.Label(m, text="", width=30,height=10, bg="white")
label3.pack()
label4 = tk.Label(m, text="", width=30,height=10, bg="white")
label4.pack()
stopper = tk.Button(m, text='Stop', width=25, command=m.destroy)
submit=tk.Button(m,text='Submit',width=25,command=submitvalues)
m.bind('<Return>',submitvalues)
submit.pack()
stopper.pack()
m.mainloop()



