import tkinter
import json
import os
from tkinter import messagebox
from tkinter import ttk

root = tkinter.Tk()
root.geometry("410x100")
root.title("Visualiser configuration")
root.iconname(None)
    
def loadData():
    if os.path.isfile("configs.json"):
        print ("Config found and loaded")
        with open("configs.json") as f:
            try:
                data = json.load(f)
                chosenHourInput.delete(0, tkinter.END)
                chosenHourInput.insert(0, int(data["hours"]))
                chosenMinuteInput.delete(0, tkinter.END)
                chosenMinuteInput.insert(0, int(data["minutes"]))
                profileInput.insert(0, data["profileURL"])
            except json.JSONDecodeError:
                print ("Config file exists but is improperly configured")
    else:
        with open ("configs.json", "w") as f:
            pass
                

def saveData():
    profile = profileInput.get().lower().strip()
    chosenHours = chosenHourInput.get()
    chosenMinutes = chosenMinuteInput.get()

    information = {
        "profileURL" : profile,
        "hours" : chosenHours,
        "minutes" : chosenMinutes
    }

    with open("configs.json", "w")as f:
        json.dump(information, f)
        if len("configs.json") >1:
            messagebox.showinfo(title="Saved", message="Saved successfully")
        else:
            messagebox.showerror(title="Error", message="Something went wrong")

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

loadData()


root.mainloop()