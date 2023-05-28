import tkinter as tk
from tkinter import messagebox
import customtkinter as ctk
import socket
import datetime
from PIL import Image, ImageTk

jakartaiplist=[]
jakartaportlist=[]
sirubayaiplist=[]
sirubayaportlist=[]

def log_output(output):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"[{timestamp}] {output}\n"
    with open("log.txt", "a") as log_file:
        log_file.write(log_entry)


def set_image_background(window, image_path):
    # Load the image and create a PhotoImage object
    bg_image =ctk.CTkImage(Image.open(image_path),size=(1200,1080))

    # Create a Label widget with the image as its background
    background_label = ctk.CTkLabel(window, image=bg_image,text='')
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    

    # Set the label as the lowest layer in the window
    background_label.lower()
    
def entry_changed(*args):
    input1 = entry1.get()
    if input1 == '':
        entry1.configure(fg_color="grey")
    else:
        try:
            socket.inet_aton(input1)
            entry1.configure(fg_color='green')
        except socket.error:
            entry1.configure(fg_color='red')

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

def add_input(event=None):
    input = entry1.get()
    port=entry3.get()
    if port=='':
        port='80'
        
    log_output(f"Adding IP {input} with port {port}")

    if input != '':
        if placestr.get()=="Jakarta":
            sirubayaiplist.append(input)
            textbox2.insert(tk.END, input+' Port:'+port+'\n')        
            sirubayaportlist.append(port)
            
        elif placestr.get()=="Sirubaya":
            jakartaiplist.append(input)
            textbox1.insert(tk.END, input+' Port:'+port+'\n')        
            jakartaportlist.append(port)
        
        
    entry1.delete(0, 'end')
    entry3.delete(0, 'end')

def outputshow():
    global new_window
    
    new_window = ctk.CTkToplevel()
    new_window.geometry("1000x700")
    new_window.title('IP values')
    set_image_background(new_window, "nms.webp")
    
    def outputiterate():
        for widget in new_window.winfo_children():
            if str(widget)=='.!ctktoplevel.!ctklabel':
                continue
            widget.destroy()
        flag1 = True
        flag2 = True
        value_string1 = 'Jakarta :\n\n\n'
        value_string2 = 'Sirubaya :\n\n\n'
        value_string1n = 'Jakarta Not Accessible:\n\n\n'
        value_string2n = 'Sirubaya Not Accessible:\n\n\n'
        for no, i in enumerate(jakartaiplist):

            if check_ip_accessibility(i, jakartaportlist[no]):
                value_string1 = value_string1 + i + ' is accessible on port :' + jakartaportlist[no] + '\n'
                log_output(f"IP {i} is accessible on port {jakartaportlist[no]} (Jakarta)")
            else:
                value_string1n = value_string1n + i + ' is not accessible on port :' + jakartaportlist[no] + '\n'
                flag1 = False
                log_output(f"IP {i} is not accessible on port {jakartaportlist[no]} (Jakarta)")
        for no, i in enumerate(sirubayaiplist):
            if check_ip_accessibility(i, sirubayaportlist[no]):
                value_string2 = value_string2 + i + ' is accessible on port :' + sirubayaportlist[no] + '\n'
                log_output(f"IP {i} is accessible on port {sirubayaportlist[no]} (Sirubaya)")
            else:
                value_string2n = value_string2n + i + ' is not accessible on port :' + sirubayaportlist[no] + '\n'
                flag2 = False
                log_output(f"IP {i} is not accessible on port {sirubayaportlist[no]} (Sirubaya)")

        output_frame = ctk.CTkFrame(new_window)
        output_frame.pack(padx=50, pady=50)

        output_frame.grab_set()
        labeled1 = ctk.CTkTextbox(output_frame, width=400, font=('Arial', 15))
        labeled1.configure(state='normal')
        labeled1.insert(tk.END, value_string1)
        labeled1n = ctk.CTkTextbox(output_frame, width=400, font=('Arial', 15))
        labeled1n.configure(state='normal')
        labeled1n.insert(tk.END, value_string1n)
        labeled2 = ctk.CTkTextbox(output_frame, width=400, font=('Arial', 15))
        labeled2.configure(state='normal')
        labeled2.insert(tk.END, value_string2)
        labeled2n = ctk.CTkTextbox(output_frame, width=400, font=('Arial', 15))
        labeled2n.configure(state='normal')
        labeled2n.insert(tk.END, value_string2n)
        labeled1.configure(state='disabled')
        labeled2.configure(state='disabled')
        
        labeled1.configure(fg_color='green')
        labeled2.configure(fg_color='green')
        labeled2.grid(row=0, column=1, padx=30, pady=30)
        labeled1.grid(row=0, column=0, padx=30, pady=30)
        if not flag1:
            labeled1n.grid(row=1, column=0, padx=30, pady=30)
            labeled1n.configure(fg_color='red')
            
        
        if not flag2:
            labeled2n.grid(row=1, column=1, padx=30, pady=30)
            labeled2n.configure(fg_color='red')
        
        
        

        new_window.after(10000, outputiterate)
    

    outputiterate()
    
def clearlist():
    jakartaiplist.clear()
    sirubayaiplist.clear()
    textbox1.delete('3.0', tk.END)


def go_back():
        for widget in m.winfo_children():
            widget.destroy()
        bg_image =ctk.CTkImage(Image.open('nms.webp'),size=(1000,250))

        spacer=ctk.CTkLabel(m, text="Network Monitoring System", padx=10, pady=10, font=('Arial', 50), image=bg_image)
        spacer.pack(fill='both', expand=True, anchor='center')


        # spacer.grid(sticky="nsew")


        buttonframe2= ctk.CTkFrame(m)
        buttonframe2.pack(fill='both', expand=True, anchor='center')

        buttonframe= ctk.CTkFrame(buttonframe2)
        buttonframe.pack(padx=10, pady=20)


        

        button1 = ctk.CTkButton(buttonframe, text="Monitor", command=button1_clicked)
        button1.grid(row=1, column=0, padx=10, pady=10)

        button2 = ctk.CTkButton(buttonframe, text="Custom")
        button2.grid(row=1, column=1, padx=10, pady=10)

        button3 = ctk.CTkButton(buttonframe, text="About", command=button3_clicked)
        button3.grid(row=1, column=2, padx=10, pady=10)

def place():
    if placestr.get()=='Jakarta':
        placestr.set('Sirubaya')
    else:
        placestr.set('Jakarta')


def button1_clicked():
    # Remove all widgets from the main window
    log_output("Monitor button clicked")
    for widget in m.winfo_children():
        widget.destroy()
    tb_frame=ctk.CTkFrame(m)
    tb_frame.pack()
    set_image_background(m, "nms.webp")
    global textbox1
    textbox1=ctk.CTkTextbox(tb_frame,width=300,font=('Arial', 15))
    textbox1.grid(row=0, column=0, padx=10, pady=10)
    textbox1.insert(tk.END, 'IP & Port in Jakarta :\n\n\n')
    global textbox2
    textbox2=ctk.CTkTextbox(tb_frame,width=300,font=('Arial', 15))  
    textbox2.grid(row=0, column=1, padx=10, pady=10)
    textbox2.insert(tk.END, 'IP & Port in Sirubaya :\n\n\n')
    
  
    
    frame_place1=ctk.CTkFrame(m)
    frame_place1.pack(padx=50, pady=50)
    label1 = ctk.CTkLabel(frame_place1, text="Ip address : ")
    label1.grid(row=0, column=0, padx=10, pady=10)
    global entry1
    global entry3
    global sv
    sv=tk.StringVar()
    
    entry1 = ctk.CTkEntry(frame_place1,width=300,textvariable=sv, validate="focusout", validatecommand=entry_changed)
    sv.trace('w', entry_changed)
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
    global placestr
    placestr=tk.StringVar()
    placestr.set('Sirubaya')
    
    place_button=ctk.CTkButton(frame_buttons, textvariable=placestr, command=place)
    place_button.grid(row=0, column=4, padx=10, pady=10)


def button3_clicked():
    messagebox.showinfo("About", "The project Network Monitoring System is all about the monitoring the network accessibility in Indonesia mainly in Jakarta and Sirubaya. This python code check the validity and accessibility of an ip address along with its port number and reminds the user if any issues pops up. ")
    m.messagebox("100x100")

ctk.set_appearance_mode("system")
ctk.set_default_color_theme("green")   
m=ctk.CTk()

m.title('NMS')
m.geometry("1000x500")
with open("log.txt", "w") as log_file:
    pass

log_output("Program started")



# spacermain=ctk.CTkLabel(m, text="", padx=100, pady=100)
# spacermain.pack()
width=m.winfo_width()
height=m.winfo_height()
print(width,height)
bg_image =ctk.CTkImage(Image.open('nms.webp'),size=(1000,375))

spacer=ctk.CTkLabel(m, text="Network Monitoring System", font=('Arial', 50),image=bg_image)
spacer.pack(fill='both', expand=True, anchor='center')


# spacer.grid(sticky="nsew")


buttonframe2= ctk.CTkFrame(m)
buttonframe2.pack(fill='both', expand=True, anchor='center')

buttonframe= ctk.CTkFrame(buttonframe2)
buttonframe.pack(padx=10, pady=20)

button1 = ctk.CTkButton(buttonframe, text="Monitor", command=button1_clicked)
button1.grid(row=1, column=0, padx=10, pady=10)

button2 = ctk.CTkButton(buttonframe, text="Custom")
button2.grid(row=1, column=1, padx=10, pady=10)

button3 = ctk.CTkButton(buttonframe, text="About", command=button3_clicked)
button3.grid(row=1, column=2, padx=10, pady=10)

m.mainloop()
log_output("Program ended")

