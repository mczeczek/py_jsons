#!/usr/bin/python

from Tkinter import *
import os, tkFileDialog

from py_jsons import *

class JsonCollectorGui:
    fileUrl = ""
    noFile = "File not chosen yet"
    groupJsonsBy=""
    def __init__(self, master):
        self.master = master
        self.attachOriginalLogFile = BooleanVar()
        self.groupJsonsBy = StringVar()
        self.customRegexPrefix = StringVar()
        master.title("JSON collector")
        master.minsize(width=260, height=120)

        Button(master, text="Choose file", command=self.choose_file).grid(row=2, column=1, sticky="W")
        self.labelFile = Label(master, text=self.noFile)
        self.labelFile.grid(row=2,column=2,sticky="W")
        
        Checkbutton(master, text="Attach original log file", variable=self.attachOriginalLogFile, onvalue=True, offvalue=False).grid(row=3,column=1, sticky="W")
        
        Label(master, text="Group JSONs by").grid(row=4,column=1,sticky="E")
        e = Entry(master, textvariable=self.groupJsonsBy, ).grid(row=4,column=2, sticky="W")
        self.groupJsonsBy.set("")

        #End of customized version

        self.collectButton = Button(master, text="Collect JSONs", command=self.process_file, state=DISABLED)
        self.collectButton.grid(row=6, column=1, sticky="W")
        Button(master, text="Close", command=master.quit).grid(row=7, column=1, sticky="W")

    def choose_file(self):
        self.fileUrl = tkFileDialog.askopenfilename()
        if (os.path.isfile(self.fileUrl)):
            self.labelFile['text'] = os.path.basename(self.fileUrl)
            self.collectButton['state'] = 'normal'
        else:
            self.labelFile['text'] = self.noFile
            self.collectButton['state'] = 'disabled'

    def process_file(self):
        py_jsons(self.fileUrl, self.groupJsonsBy.get(), self.attachOriginalLogFile.get())

root = Tk()
my_gui = JsonCollectorGui(root)
root.mainloop()
