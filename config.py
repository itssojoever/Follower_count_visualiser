import tkinter
import json
import os
from tkinter import messagebox
from tkinter import ttk

root = tkinter.Tk()
root.geometry("410x100")
root.title("Visualiser configuration")
root.iconname(None)

def saveData():
    pass

programFrame1 = tkinter.LabelFrame(root)
programFrame1.grid(row=0, column=0)

l1 = tkinter.Label(programFrame1, font="helvetica, 12", text="Please select time")
chosenHourInput = tkinter.Spinbox(programFrame1, from_=0, to=24)
chosenMinuteInput = tkinter.Spinbox(programFrame1, from_=0, to=60)
l1.grid(row=0, column=1)
chosenHourInput.grid(row=0, column=2)
chosenMinuteInput.grid(row=0, column=3)

programFrame2 = tkinter.LabelFrame(root)
programFrame2.grid(row=1, column=0)

l2 = tkinter.Label(programFrame2, font="helvetica, 12", text="Profile link: ")
l2.grid(row=0, column=0)
profileInput = tkinter.Entry(programFrame2, font="helvetica, 12", relief="sunken")
profileInput.grid(row=0, column=1)


programFrame3 = tkinter.LabelFrame(root)
programFrame3.grid(row=2, column=0)

saveButton = tkinter.Button(programFrame3, text="Save config", command=lambda: saveData())
saveButton.grid(row=0, column=0)


root.mainloop()