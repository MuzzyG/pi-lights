#last updated 03/04/2019
#Murray Green

from tkinter import *
import socket


class menu:
    def __init__(self,master):
        self.menu = master
        #sets tile of window
        self.menu.title("Menu")

        #sets the available sequences, will be able to read from a file for custom sequences
        self.sequence = StringVar(self.menu)
        self.sequence.set("Select a sequence...")
        #get available choices from sequences.txt
        with open("sequences.txt","r") as file:
            self.choices = file.read().splitlines()
        print(self.choices)

        #define the defualt sequences
        self.defualt_sequences = ["Red", "Green", "Blue", "Clear", "close"]

        #Large text at the top of the window
        self.menu_title = Label(self.menu, text="LED control", font=("courier",28), bg=bg_colour)
        self.menu_title.grid(column=0,row=0,sticky="n")

        #Drop-down menu for selecting sequences
        self.sequence_menu = OptionMenu(self.menu, self.sequence, *self.choices)
        self.sequence_menu["highlightthickness"]=0
        self.sequence_menu.grid(column=0,row=1,sticky="nw",pady=20,padx=5)

        #Label for text above status window
        self.status_label = Label(self.menu, text="Status:", bg=bg_colour)
        self.status_label.grid(column=1,row=2,sticky="nw",padx=20)

        #Button to open the sequence creation window
        self.create_sequence = Button(self.menu, text="Create new sequence", command=self.open_sequence_page)
        self.create_sequence.grid(column=1,row=0,sticky="n",padx=20,pady=5)

        #Button to open the settings window
        self.settings_button = Button(self.menu, text="Settings", command=self.open_settings_page)
        self.settings_button.grid(column=3,row=0,sticky="ne",padx=20,pady=5)

        #Status window to display errors
        self.status_box = Label(self.menu,bg="white",relief=SUNKEN,width=50,height=5,anchor="w",justify=LEFT)
        self.status_box.grid(column=1,columnspan=3,row=3,rowspan=4,sticky="w",padx=20,pady=5)

        #Button to run the sequence
        self.run_button = Button(self.menu, font=("courier",16),text="Run", command=self.run_sequence)
        self.run_button.grid(column=0,row=3,sticky="sw",padx=20,pady=5)

    def open_settings_page(self):
        #opens the window for editing settings
        root2 = Tk()
        root2.configure(bg=bg_colour)
        settings_screen = Settings(root2)
        root2.mainloop()

    def open_sequence_page(self):
        #open the page for creating new sequences
        import sequence_page
        root3 = Tk()
        root3.configure(bg=bg_colour)
        sequences = sequence_page.sequence_window(root3)
        root3.mainloop()
        print("Open sequence page")

    def run_sequence(self):
        #runs the selected sequence
        print("Running sequence: "+self.sequence.get())
        try:
            with open("config.txt","r") as file:
                self.config_values = file.read().splitlines()
                print("Using " + self.config_values[0] + " and strip length " + self.config_values[1])
            #open socket
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            #change for port number
            sock.connect((self.config_values[0],6969))
            #cheack if sequence is defualt
            if self.sequence.get() in self.defualt_sequences:
                sock.send(self.sequence.get().encode())
            else:
                with open(self.sequence.get()+".txt","r") as file:
                    sock.send(file.read().encode())
            sock.close()
        except FileNotFoundError:
            #If no file is found, print error message
            print("No config file found.")


class Settings:
    def __init__(self,master):
        self.settings = master
        #Window title
        self.settings.title("Settings")

        #define the variables and set from config file
        #Checks if settings file exists
        try:
            with open("config.txt","r") as file:
                file = open("config.txt","r")
                self.config_values = file.read().splitlines()
            print("Using values from config file.")
        except FileNotFoundError:
            #If no file is found, use defualt values
            print("No config file found. Using defualt settings.")
            self.config_values = ['','','Select a sequence...']

        #Sets defualts values in text inputs
        self.sequence_defualt = StringVar(self.settings)
        self.sequence_defualt.set(self.config_values[2])
        self.choices = ["Red", "Green", "Blue"]
        self.local_ip = StringVar(self.settings)
        self.local_ip.set(self.config_values[0])
        self.led_number = StringVar(self.settings)
        self.led_number.set(self.config_values[1])

        #window title
        self.settings_title = Label(self.settings, text="Settings", font=("courier",28), bg=bg_colour)
        self.settings_title.grid(column=1,row=0,sticky="n")

        #Text to describe ip address input box
        self.ip_label = Label(self.settings, text="Raspberry pi IP:", bg=bg_colour)
        self.ip_label.grid(column=0,row=1,sticky="w")

        #text input for ip address
        self.ip_entry = Entry(self.settings, textvariable=self.local_ip)
        self.ip_entry.grid(column=1,row=1,sticky="w")

        #Text to describe the strip length input box
        self.length_label = Label(self.settings, text="LED strip length:", bg=bg_colour)
        self.length_label.grid(column=0,row=2,sticky="w")

        #text input for strip length
        self.length_entry = Entry(self.settings, textvariable=self.led_number)
        self.length_entry.grid(column=1,row=2,sticky="w")

        #Text to describe startup sequence input box
        self.startup_label = Label(self.settings, text="Startup sequence:", bg=bg_colour)
        self.startup_label.grid(column=0,row=3,sticky="w")

        #text input for startup sequence
        self.startup_menu = OptionMenu(self.settings, self.sequence_defualt, *self.choices)
        self.startup_menu["highlightthickness"]=0
        self.startup_menu.grid(column=1,row=3,sticky="w")

        #button to save changed settings
        self.save_button = Button(self.settings, text="Save settings", command=self.save)
        self.save_button.grid(column=2,row=4,sticky="w")

        #text label for errors/to tell user to restart for colour settings

    def save(self):
        #saves the user settings to file
        output = (self.local_ip.get() + "\n" + self.led_number.get() + "\n" + self.sequence_defualt.get())
        print(output)
        with open("config.txt","w") as file:
            file.write(output)


#defualt values
defualt_colour = "#ffffcc"
#set background colour from config file, otherwise:
bg_colour = defualt_colour

root = Tk()
root.configure(bg=bg_colour)
menu_screen = menu(root)
root.mainloop()
