import tkinter as tk
from tkinter import messagebox
import customtkinter as ctk
import socket
from PIL import Image

iplist=[]
portlist=[]


def check_ip_accessibility(ip_address,port):
    try:
        port=int(port)
        socket.inet_aton(ip_address)
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.01)  # Set a timeout value in seconds

        result = sock.connect_ex((ip_address, port))
        sock.close()
        if result == 0:
            return True
        else:
            return False

        
    except socket.error as e:
        return False

def add_input(event=None):
    input = entry1.get()
    port=entry3.get()
    if port=='':
        port='80'
    if input != '':
        iplist.add(input)
        textbox1.insert(tk.END, input+' Port:'+port+'\n')        
        portlist.add(port)
        
    entry1.delete(0, 'end')
    entry3.delete(0, 'end')

def outputshow():
    global new_window
    
    new_window = ctk.CTkToplevel()
    new_window.geometry("1000x400")
    new_window.title('IP values')
    
    
    def outputiterate():
        for widget in new_window.winfo_children():
            widget.destroy()
        flag1=True
        print('in outputiterate')
        value_string1='IPs are:\n\n\n'
        for no,i in enumerate(iplist):
            if check_ip_accessibility(i,portlist[no]):
                value_string1=value_string1+i+' is accessible on port :'+portlist[no]+'\n'
            else:
                value_string1=value_string1+i+' is not accessible on port :'+portlist[no]+'\n'
                flag1=False
                
        output_frame=ctk.CTkFrame(new_window)
        output_frame.pack(padx=50, pady=50)
        
        output_frame.grab_set()
        labeled1 = ctk.CTkTextbox(output_frame,width=400,font=('Arial', 15))
        labeled1.configure(state='normal')
        labeled1.insert(tk.END, value_string1)
        labeled1.configure(state='disabled')
        if flag1:
            labeled1.configure(fg_color='green')
        else:
            labeled1.configure(fg_color='red')
        labeled1.grid(row=0, column=0, padx=30, pady=30)
        

        new_window.after(1000, outputiterate)       

    outputiterate()
    
def clearlist():
    iplist.clear()
    textbox1.delete('3.0', tk.END)


def go_back():
        for widget in m.winfo_children():
            widget.destroy()
        spacer=ctk.CTkLabel(m, text="Network Monitoring System", padx=10, pady=10, font=('Arial', 50))
        spacer.grid(sticky="nsew")
        spacer.pack()


        buttonframe= ctk.CTkFrame(m)
        buttonframe.pack()

        button1 = ctk.CTkButton(buttonframe, text="Monitor", command=button1_clicked)
        button1.grid(row=1, column=0, padx=10, pady=10)

        button2 = ctk.CTkButton(buttonframe, text="Custom")
        button2.grid(row=1, column=1, padx=10, pady=10)

        button3 = ctk.CTkButton(buttonframe, text="About", command=button3_clicked)
        button3.grid(row=1, column=2, padx=10, pady=10)



def button1_clicked():
    # Remove all widgets from the main window
    for widget in m.winfo_children():
        widget.destroy()
    tb_frame=ctk.CTkFrame(m)
    tb_frame.pack()
    global textbox1
    textbox1=ctk.CTkTextbox(tb_frame,width=300,font=('Arial', 15))
    textbox1.grid(row=0, column=0, padx=10, pady=10)
    textbox1.insert(tk.END, 'IP & Port are :\n\n\n')
    # Create a label saying "hi"
    frame_place1=ctk.CTkFrame(m)
    frame_place1.pack(padx=50, pady=50)
    label1 = ctk.CTkLabel(frame_place1, text="Ip address : ")
    label1.grid(row=0, column=0, padx=10, pady=10)
    global entry1
    global entry3
    entry1 = ctk.CTkEntry(frame_place1,width=300)
    entry1.grid(row=0, column=1, padx=10, pady=10)
    label3=ctk.CTkLabel(frame_place1, text="Port number :")
    label3.grid(row=0, column=2, padx=10, pady=10)
    entry3 = ctk.CTkEntry(frame_place1,width=300)
    entry3.grid(row=0, column=3, padx=10, pady=10)
    entry3.bind('<Return>', add_input)
    entry1.bind('<Return>', add_input)


    
    
    frame_buttons=ctk.CTkFrame(m)
    frame_buttons.pack(padx=20, pady=20)
    # Create an "Output" button
    output_button = ctk.CTkButton(frame_buttons, text="Output",command=outputshow)
    output_button.grid(row=0, column=0, padx=10, pady=10)

    #append the input to the list by append button
    add_button = ctk.CTkButton(frame_buttons, text="Add",command=add_input)
    add_button.grid(row=0, column=1, padx=10, pady=10)
    
    clear_button = ctk.CTkButton(frame_buttons, text="Clear",command=clearlist)
    clear_button.grid(row=0, column=2, padx=10, pady=10)

    back_button = ctk.CTkButton(frame_buttons, text="Back", command=go_back)
    back_button.grid(row=0, column=3, padx=10, pady=10)
    # Create a label to display the output


def button3_clicked():
    messagebox.showinfo("About", "The project Network Monitoring System is all about the monitoring the network accessibility in Indonesia mainly in Jakarta and Sirubaya. This python code check the validity and accessibility of an ip address along with its port number and reminds the user if any issues pops up. ")
    m.messagebox("100x100")

ctk.set_appearance_mode("system")
ctk.set_default_color_theme("green")   
m=ctk.CTk()

m.title('NMS')
m.geometry("1000x500")


spacer=ctk.CTkLabel(m, text="Network Monitoring System", padx=10, pady=10, font=('Arial', 50))
spacer.grid(sticky="nsew")
spacer.pack()


buttonframe= ctk.CTkFrame(m)
buttonframe.pack()

button1 = ctk.CTkButton(buttonframe, text="Monitor", command=button1_clicked)
button1.grid(row=1, column=0, padx=10, pady=10)

button2 = ctk.CTkButton(buttonframe, text="Custom")
button2.grid(row=1, column=1, padx=10, pady=10)

button3 = ctk.CTkButton(buttonframe, text="About", command=button3_clicked)
button3.grid(row=1, column=2, padx=10, pady=10)

m.mainloop()
