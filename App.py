import tkinter as tk
import customtkinter as ctk
import socket
from PIL import Image
from tkinter import ttk
iplist1=[]
iplist2=[]


def check_ip_accessibility(ip_address):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.1)  # Set a timeout value in seconds

        result = sock.connect_ex((ip_address, 80))
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
    if input1 != '':
        iplist1.append(input1)
        textbox.insert(tk.END, input1+'\t-PLACE 1\n')
    if input2 != '':
        iplist2.append(input2)
        textbox.insert(tk.END, input2+'\t-PLACE 2\n')
    entry1.delete(0, 'end')
    entry2.delete(0, 'end')
def outputshow():
    
    new_window = ctk.CTkToplevel()
    new_window.geometry("400x400")
    new_window.title('IP values')
    value_string=''
    value_string=value_string+'IPs in place 1 are:\n\n\n'
    for i in (iplist1):
        if check_ip_accessibility(i):
            value_string=value_string+i+' is accessible\n'
        else:
            value_string=value_string+i+' is not accessible\n'
    value_string=value_string+'\n\n\nIPs in place 2 are:\n\n\n'
    for i in (iplist2):
        if check_ip_accessibility(i):
            value_string=value_string+i+' is accessible\n'
        else:
            value_string=value_string+i+' is not accessible\n'
    labeled = ctk.CTkTextbox(new_window,width=350)
    labeled.insert(tk.END, value_string)
    labeled.pack()



def button1_clicked():
    # Remove all widgets from the main window
    for widget in m.winfo_children():
        widget.destroy()
    global textbox
    textbox=ctk.CTkTextbox(m,width=350)
    textbox.pack()
    # Create a label saying "hi"
    label1 = ctk.CTkLabel(m, text="Place 1")
    label1.pack()
    global entry1
    entry1 = ctk.CTkEntry(m)
    entry1.pack()
    entry1.bind('<Return>', append_input)
    
    label2 = ctk.CTkLabel(m, text="Place 2")
    label2.pack()
    global entry2
    entry2 = ctk.CTkEntry(m)
    entry2.pack()
    entry2.bind('<Return>', append_input)

    # Create an "Output" button
    output_button = ctk.CTkButton(m, text="Output",command=outputshow)
    output_button.pack()

    # Create a label to display the output
    

ctk.set_appearance_mode("system")
ctk.set_default_color_theme("green")   
m=ctk.CTk()

m.title('IP Checker')
m.geometry("800x500")

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
