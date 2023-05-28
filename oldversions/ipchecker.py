# %% [markdown]
# ## Python Program to Validate IP Addresses and Correct Incorrect IPs
# 
# This Python program reads a list of IP addresses from a text file named `ipaddress.txt`, validates them to check if they are correct IP addresses, and then writes the correct IP addresses to the same file. If there are any incorrect IP addresses, the program asks the user to enter the website for that IP address, corrects the IP address and writes it to the file.
# 
# ## Steps
# 
# The program performs the following steps:
# 
# - It imports the `socket` module to work with IP addresses.
# 
# - Defines a function `isvalid(ip)` that takes an IP address as input and checks if it is a valid IP address. The `socket.inet_aton()` function is used to validate the IP address.
# 
# - Creates a list `avoidstrings` that contains some strings which should not be written to the output file.
# 
# - Initializes two empty lists `correctips` and `incorrectips`.
# 
# - Opens the input file `ipaddress.txt` and reads each IP address. If the IP address is in the `avoidstrings` list, it is skipped. If the IP address is valid, it is added to the `correctips` list, otherwise, it is added to the `incorrectips` list.
# 
# - Writes the correct IP addresses to the file `ipaddress.txt`.
# 
# - For each incorrect IP address, the program prompts the user to enter the website for that IP address. It corrects the IP address using `socket.gethostbyname()` function, writes the corrected IP address to the file `ipaddress.txt`.
# 
# This program helps in validating IP addresses and correcting the incorrect ones.
# 

# %% [markdown]
# ### import socket
# - This imports the `socket` module which provides low-level networking interfaces. 
# - It is used later in the program to check if an IP address is valid.
# 
# 
# 
# 
# 

# %%
import socket
import tkinter as tk

# %% [markdown]
# #### Function to Check if IP Address is Valid
# 
# The `isvalid()` function takes an IP address as input and returns `True` if the IP address is valid, and `False` otherwise.
# 
# - `socket.inet_aton(ip)` converts the IP address string to an IP address in packed 32-bit binary format.
# - If the IP address is invalid, a `socket.error` exception is raised, which is caught by the `except` block and returns `False`.
# 
# ```python
# def isvalid(ip):
#     try:
#         socket.inet_aton(ip)
#         return True
#     except socket.error:
#         return False
# 

# %%
def isvalid(ip):
    try:
        socket.inet_aton(ip)
        return True
    except socket.error:
        return False

# %% [markdown]
# ### Initializing the avoidstrings list
# 
# Creating a list `avoidstrings` to store the strings `Correct ips are:`, `Incorrect ips are:` and `Incorrect ips which corrected are:` which will be avoided while processing the input file. 
# 

# %%
avoidstrings=['Correct ips are: \n','Incorrect ips are: \n','Incorrect ips which corrected are: \n','\n','']

# %% [markdown]
# #### Initializing the lists for storing the correct and incorrect IPs
# 
# Creating two empty lists `correctips` and `incorrectips` to store the valid and invalid IPs respectively. 
# 

# %%
correctips=[]
incorrectips=[]

# %%
iplist=[]

# %%
def submitvalues(event=None):
    
    iplist.append(entrystr.get())
    entrystr.delete(0,tk.END)
 
   

# %%
m=tk.Tk()

m.title('IP Checker')
m.geometry("800x100")

entrystr= tk.Entry(m, width=100, borderwidth=5)
entrystr.pack()
 
stopper = tk.Button(m, text='Stop', width=25, command=m.destroy)
submit=tk.Button(m,text='Submit',width=25,command=submitvalues)
m.bind('<Return>',submitvalues)
submit.pack()
stopper.pack()
m.mainloop()
print(iplist)


# %% [markdown]
# #### Reading input file and processing the IPs
# 
# Reading the input file `ipaddress.txt` and processing each line. If the line is a string present in `avoidstrings`, it is skipped. If the line is a valid IP address, it is added to the `correctips` list. Otherwise, it is added to the `incorrectips` list. At the end, printing the `correctips` and `incorrectips` lists. 
# 

# %%
# f=open('ipaddress.txt','r')
for i in iplist:
    if i in avoidstrings:
        continue
    if isvalid(i.strip()):
        correctips.append(i.strip())
    else:
        incorrectips.append(i.strip())
print("Correct IPs are: ",correctips)
print("Incorrect IPs are: ",incorrectips)

# %% [markdown]
# #### Writing the correct IPs to output file
# 
# Opening the input file `ipaddress.txt` in write mode and writing the string `Correct ips are:` followed by each correct IP address in a new line. 
# 

# %%
f=open('ipaddress.txt','w')
f.write('Correct ips are: \n')
for i in correctips:
    f.write(i+"\n")

# %% [markdown]
# #### Correcting and writing the incorrect IPs to output file
# 
# Appending the string `Incorrect ips which corrected are:` to the output file `ipaddress.txt` followed by the IP addresses that were incorrect but could be corrected by converting them to their respective website's IP address. For each incorrect IP, the user is prompted to enter the website address for that IP and the corrected IP is written to the output file. 
# 

# %%
# f.write('Incorrect ips which corrected are: \n')
# for i in incorrectips:
#     print('Enter the website for this ip you entered: ',i)
#     print('eg: www.google.com')
#     a=input()
#     try:     
#         correctedip=socket.gethostbyname(a)
#     except:
#         continue
#     f.write(correctedip+"\n")


