from tkinter import *
import socket

#set defualt colour of the background
defualt_colour = "#ffffcc"
bg_colour = defualt_colour

class sequence_window:
    def __init__(self,master):
        self.seq = master
        #window title
        self.seq.title("Create a sequence")

        #declare variables for text input
        self.red = StringVar(self.seq)
        self.green = StringVar(self.seq)
        self.blue = StringVar(self.seq)
        self.light_start = StringVar(self.seq)
        self.light_end = StringVar(self.seq)
        self.sleep = StringVar(self.seq)
        self.sequence_name = StringVar(self.seq)

        self.command = []

        #Text at top of window
        self.sequence_title = Label(self.seq, text="Create a sequence", font=("courier",28), bg=bg_colour)
        self.sequence_title.grid(column=0,columnspan=10,row=0,sticky="nw")

        #text to describe window
        self.sequence_overview = Label(self.seq,bg="white",relief=SUNKEN,width=55,height=5,anchor="w",justify=LEFT)
        self.sequence_overview.grid(column=0,columnspan=10,row=1,rowspan=4,stick="w",padx=10)

        #text to describe red input
        self.red_label = Label(self.seq, text="Red:", bg=bg_colour)
        self.red_label.grid(column=0,row=5)

        #text input for red value
        self.red_entry = Entry(self.seq, textvariable=self.red, width=3)
        self.red_entry.grid(column=1,row=5,sticky="w")

        #text to describe green input
        self.green_label = Label(self.seq, text="Green:", bg=bg_colour)
        self.green_label.grid(column=2,row=5)

        #text input for green value
        self.green_entry = Entry(self.seq, textvariable=self.green, width=3)
        self.green_entry.grid(column=3,row=5,sticky="w")

        #text to describe blue input
        self.blue_label = Label(self.seq, text="Blue:", bg=bg_colour)
        self.blue_label.grid(column=4,row=5)

        #text input for blue value
        self.blue_entry = Entry(self.seq, textvariable=self.blue, width=3)
        self.blue_entry.grid(column=5,row=5,sticky="w")

        #text to describe light start input
        self.light_start_label = Label(self.seq, text="Light start:", bg=bg_colour)
        self.light_start_label.grid(column=6,row=5)

        #text input for light start value
        self.light_start_entry = Entry(self.seq, textvariable=self.light_start, width=3)
        self.light_start_entry.grid(column=7,row=5,sticky="w")

        #text to describe light end input
        self.light_end_label = Label(self.seq, text="Light end:", bg=bg_colour)
        self.light_end_label.grid(column=8,row=5)

        #text input for light end value
        self.light_end_entry = Entry(self.seq, textvariable=self.light_end, width=3)
        self.light_end_entry.grid(column=9,row=5,sticky="w")

        #button to add command to sequence
        self.add_button = Button(self.seq, text="Add command", command=self.add)
        self.add_button.grid(column=10,row=5,pady=10)

        #text to describe sleep input
        self.sleep_label = Label(self.seq, text="Time:", bg=bg_colour)
        self.sleep_label.grid(column=8,row=6)

        #text input for sleep value
        self.sleep_entry = Entry(self.seq, textvariable=self.sleep, width=3)
        self.sleep_entry.grid(column=9,row=6,sticky="w")

        #text to descrbe name input
        self.name_label = Label(self.seq, text="Sequence name:", bg=bg_colour)
        self.name_label.grid(column=10,row=0,sticky="s")

        #text input for sequecne name
        self.name_entry = Entry(self.seq, textvariable=self.sequence_name)
        self.name_entry.grid(column=10,row=1,padx=5)

        #button to save sequence
        self.write_button = Button(self.seq, text="Save", command=self.save)
        self.write_button.grid(column=10,row=2)

    def add(self):
        #prints out values for testing
        print(self.red.get())
        print(self.blue.get())
        print(self.green.get())
        print(self.light_start.get())
        print(self.light_end.get())
        print(self.sleep.get())

        #adds command to sequnce list
        self.command.append({"red":self.red.get(),"green":self.green.get(),"blue":self.blue.get(),"light_start":self.light_start.get(),"light_end":self.light_end.get(),"sleep":self.sleep.get()})
        print(self.command)

    def save(self):
        #saves sequence to text file
        print("saving")
        self.filename = self.sequence_name.get() + ".txt"
        print(self.filename)
        with open(self.filename,"w") as file:
            file.write(str(self.command))
        #add sequence name to list of available sequences
        with open("sequences.txt","a") as file:
            file.write("\n" + self.sequence_name.get())
