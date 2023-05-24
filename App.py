import tkinter as tk
import customtkinter as ctk
import socket
from PIL import Image
from tkinter import ttk
iplist1=[]
iplist2=[]
port1list=[]
port2list=[]


def check_ip_accessibility(ip_address,port):
    try:
        port=int(port)
        socket.inet_aton(ip_address)
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.1)  # Set a timeout value in seconds

        result = sock.connect_ex((ip_address, port))
        sock.close()
        if result == 0:
            return True
        else:
            return False

        
    except socket.error as e:
        return False

def append_input(event=None):
    input1 = entry1.get()
    input2 = entry2.get()
    port1=entry3.get()
    if port1=='':
        port1='80'
    port2=entry4.get()
    if port2=='':
        port2='80'
    if input1 != '':
        iplist1.append(input1)
        textbox1.insert(tk.END, input1+' Port:'+port1+'\n')        
        port1list.append(port1)
        
    if input2 != '':
        iplist2.append(input2)
        textbox2.insert(tk.END, input2+' Port:'+port2+'\n')
        port2list.append(port2)
        
    entry1.delete(0, 'end')
    entry2.delete(0, 'end')
    entry3.delete(0, 'end')
    entry4.delete(0, 'end')

def outputshow():
    global new_window
    
    new_window = ctk.CTkToplevel()
    new_window.geometry("1000x400")
    new_window.title('IP values')
    
    
    def outputiterate():
        for widget in new_window.winfo_children():
            widget.destroy()
        flag1=True
        flag2=True
        print('in outputiterate')
        value_string1='IPs in place 1 are:\n\n\n'
        value_string2='IPs in place 2 are:\n\n\n'
        for no,i in enumerate(iplist1):
            if check_ip_accessibility(i,port1list[no]):
                value_string1=value_string1+i+' is accessible on port :'+port1list[no]+'\n'
            else:
                value_string1=value_string1+i+' is not accessible on port :'+port1list[no]+'\n'
                flag1=False
        for no,i in enumerate(iplist2):
            if check_ip_accessibility(i,port2list[no]):
                value_string2=value_string2+i+' is accessible on port :'+port2list[no]+'\n'
            else:
                value_string2=value_string2+i+' is not accessible on port :'+port2list[no]+'\n'
                flag2=False
                
        output_frame=ctk.CTkFrame(new_window)
        output_frame.pack(padx=50, pady=50)
        
        output_frame.grab_set()
        labeled1 = ctk.CTkTextbox(output_frame,width=400,font=('Arial', 15))
        labeled1.configure(state='normal')
        labeled1.insert(tk.END, value_string1)
        labeled2 = ctk.CTkTextbox(output_frame,width=400,font=('Arial', 15))
        labeled2.configure(state='normal')
        labeled2.insert(tk.END, value_string2)
        labeled1.configure(state='disabled')
        labeled2.configure(state='disabled')
        if flag1:
            labeled1.configure(fg_color='green')
        else:
            labeled1.configure(fg_color='red')
        if flag2:
            labeled2.configure(fg_color='green')
        else:
            labeled2.configure(fg_color='red')
        labeled2.grid(row=0, column=1, padx=30, pady=30)
        labeled1.grid(row=0, column=0, padx=30, pady=30)
        

        new_window.after(10000, outputiterate)
        
            
        

    outputiterate()
    
def clearlist():
    iplist1.clear()
    iplist2.clear()
    textbox1.delete('3.0', tk.END)
    textbox2.delete('3.0', tk.END)


def button1_clicked():
    # Remove all widgets from the main window
    for widget in m.winfo_children():
        widget.destroy()
    tb_frame=ctk.CTkFrame(m)
    tb_frame.pack()
    global textbox1
    textbox1=ctk.CTkTextbox(tb_frame,width=300,font=('Arial', 15))
    textbox1.grid(row=0, column=0, padx=10, pady=10)
    textbox1.insert(tk.END, 'IPs in place 1 are:\n\n\n')
    global textbox2
    textbox2=ctk.CTkTextbox(tb_frame,width=300,font=('Arial', 15))  
    textbox2.grid(row=0, column=1, padx=10, pady=10)
    textbox2.insert(tk.END, 'IPs in place 2 are:\n\n\n')
    # Create a label saying "hi"
    frame_place1=ctk.CTkFrame(m)
    frame_place1.pack(padx=50, pady=50)
    label1 = ctk.CTkLabel(frame_place1, text="Place 1 Ip: ")
    label1.grid(row=0, column=0, padx=10, pady=10)
    global entry1
    global entry3
    entry1 = ctk.CTkEntry(frame_place1,width=300)
    entry1.grid(row=0, column=1, padx=10, pady=10)
    label3=ctk.CTkLabel(frame_place1, text="Enter the port number:")
    label3.grid(row=0, column=2, padx=10, pady=10)
    entry3 = ctk.CTkEntry(frame_place1,width=300)
    entry3.grid(row=0, column=3, padx=10, pady=10)
    entry3.bind('<Return>', append_input)
    entry1.bind('<Return>', append_input)
    

    label2 = ctk.CTkLabel(frame_place1, text="Place 2 Ip:")
    label2.grid(row=1, column=0, padx=10, pady=10)
    
    
    global entry2
    global entry4
    entry2 = ctk.CTkEntry(frame_place1,width=300)
    entry2.grid(row=1, column=1, padx=10, pady=10)
    entry2.bind('<Return>', append_input)
    label3=ctk.CTkLabel(frame_place1, text="Enter the port number:")
    label3.grid(row=1, column=2, padx=10, pady=10)
    entry4 = ctk.CTkEntry(frame_place1,width=300)
    entry4.grid(row=1, column=3, padx=10, pady=10)
    entry4.bind('<Return>', append_input)
    
    frame_buttons=ctk.CTkFrame(m)
    frame_buttons.pack(padx=20, pady=20)
    # Create an "Output" button
    output_button = ctk.CTkButton(frame_buttons, text="Output",command=outputshow)
    output_button.grid(row=0, column=0, padx=10, pady=10)

    #append the input to the list by append button
    append_button = ctk.CTkButton(frame_buttons, text="Append",command=append_input)
    append_button.grid(row=0, column=1, padx=10, pady=10)
    
    clear_button = ctk.CTkButton(frame_buttons, text="Clear",command=clearlist)
    clear_button.grid(row=0, column=2, padx=10, pady=10)
    # Create a label to display the output
    

ctk.set_appearance_mode("system")
ctk.set_default_color_theme("green")   
m=ctk.CTk()

m.title('IP Checker')
m.geometry("1200x500")

my_image = ctk.CTkImage(light_image=Image.open("./welcome.jpg"),
                                  dark_image=Image.open("./welcome.jpg"),
                                  size=(400, 400))

spacer=ctk.CTkLabel(m, text="",padx=10, pady=10)
spacer.pack()
image_label = ctk.CTkLabel(m, image=my_image, text="")
image_label.pack()

buttonframe= ctk.CTkFrame(m)
buttonframe.pack()

button1 = ctk.CTkButton(buttonframe, text="Monitor", command=button1_clicked)
button1.grid(row=1, column=0, padx=10, pady=10)

button2 = ctk.CTkButton(buttonframe, text="Custom")
button2.grid(row=1, column=1, padx=10, pady=10)

m.mainloop()
