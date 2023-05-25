# IP Address Checker

This project is a Network Monitoring System that allows users to monitor the accessibility of IP addresses in Jakarta and Surabaya, Indonesia. The application checks the validity and accessibility of an IP address along with its port number and provides feedback to the user. The project is implemented using Python and utilizes the Tkinter and Socket libraries.

## 🖥️ Technology Used
The following technologies and libraries are used in this project:

### Tkinter 🎨
Tkinter is the standard Python library for creating graphical user interfaces (GUI). It provides a set of tools and widgets to create windows, buttons, text fields, and other GUI components. Tkinter allows developers to build user-friendly interfaces for their Python applications. It is included with most Python installations and requires no extra installation. 

In this project, Tkinter is used to create the GUI components for the Network Monitoring System. It provides a straightforward way to design and manage windows, labels, buttons, entry fields, and other interactive elements. Tkinter's event-driven programming model enables the application to respond to user actions, such as button clicks and text input.

Using Tkinter, developers can create visually appealing interfaces by customizing the appearance of components, such as colors, fonts, and sizes. It also offers layout management options to organize and arrange components within windows.

### Socket 🌐
The socket module in Python provides low-level access to networking interfaces and enables communication between devices over a network. It allows the creation of network sockets, which are endpoints for sending and receiving data across a computer network. 

In this project, the socket module is used to check the accessibility of IP addresses and ports. The application creates socket objects, sets a timeout value, and attempts to establish a connection with the specified IP address and port to determine their accessibility. 

By utilizing socket programming, the IP Address Checker can perform network connectivity tests and provide feedback on whether an IP address is reachable or not. It helps users identify potential connectivity issues and monitor the availability of specific IP addresses and ports.

Socket programming with Python allows for the implementation of various network protocols, such as TCP (Transmission Control Protocol) and UDP (User Datagram Protocol). These protocols enable reliable and connection-oriented communication (TCP) or fast and connectionless communication (UDP) between devices.

Socket programming is a powerful feature for network-related applications, including network monitoring, data transfer, web scraping, and more. Python's socket module simplifies the process of creating network sockets and managing network connections, making it easier to build network-enabled applications.

## 🚀 Usage
The application provides a user-friendly interface for monitoring IP addresses. Upon launching the application, users are presented with the main menu, which includes three options: "Monitor," "Custom," and "About."

### Monitor 📡
This option allows users to monitor the accessibility of IP addresses. The monitor component includes the following elements:

#### IP Address Entry Field 🖊️
Users can input the IP address they want to monitor. The IP address must be in a valid format (e.g., "192.168.0.1").

#### Port Number Entry Field 🚪
Users can also specify an optional port number to check the accessibility of a specific port on the IP address. If no port number is provided, the application will use the default port for the selected protocol (e.g., port 80 for HTTP).

#### Monitor Button 📌
Clicking on the "Monitor" button initiates the accessibility check for the entered IP address and port number. The application will display the results in separate sections for Jakarta and Surabaya IP addresses.

#### Results Display 📊
The application will display the results of the accessibility check for the IP address and port number. The results will indicate whether the IP address is reachable or

 not, along with additional information such as response time and any error messages.

### Custom ✏️
This option allows users to customize the settings for the IP Address Checker. Users can modify the timeout value and the ports to check for accessibility.

### About ℹ️
Clicking on this option displays information about the project.

For more details, please visit the [GitHub repository](https://github.com/JoJosuk/IPaddresschecker).