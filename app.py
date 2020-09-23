import tkinter as tk
from tkinter import filedialog, Text
import os, sys, subprocess
from PIL import ImageTk, Image
# from os import startfile

root = tk.Tk()
root.title('Workspace Setter')
apps = []

#Check if there are any saved configurations
if os.path.isfile('save.txt'):
    with open('save.txt','r')as f:
        tempapps = f.read()
        tempapps = tempapps.split(',')
        apps = [x for x in tempapps if x.strip()]

#add apps to be opened
def addApp():

    for widget in frame.winfo_children(): 
        if widget != label1 :
            widget.destroy()

    filename=filedialog.askopenfilename(initialdir="/",title="Select File")
    apps.append(filename)
    for app in apps:
        label = tk.Label(frame,text=app,bg="gray")
        label.pack()

#open the selected apps
def runApps():
    for app in apps:
        if sys.platform == "win32":
            os.startfile(app)
        else:
            opener ="open" if sys.platform == "darwin" else "xdg-open"
            subprocess.call([opener, app])

# delete save.txt, clear app list
def clearApps():
    if os.path.isfile('save.txt'):
        os.remove('save.txt')

    apps.clear()

    for widget in frame.winfo_children(): 
        if widget!= label1:
            widget.destroy()

#Canvas for the window to attach our frame to
canvas = tk.Canvas(root, height=500, width=500, bg="white")
canvas.pack()

#Set the background for canvas

img = ImageTk.PhotoImage(Image.open('/home/jc/Resume_Projects/App_Opener_Simple/bg-image.jpg').resize((500,500), Image.ANTIALIAS))
canvas.background = img  # Keep a reference in case this code is put in a function.
bg = canvas.create_image(0, 0, anchor=tk.NW, image=img)

#Initialise and set the frame
frame = tk.Frame(root,bg="#eaffd0")
frame.place(relwidth=0.8,relheight=0.5,relx=0.1,rely=0.1)
label1 = tk.Label(frame,text="Your workspace :",font="Helvetica")
label1.pack()

#Define the buttons
clearApps = tk.Button(root,text="Clear Set Apps",fg="black",bg="#f7cac9",command=clearApps)
clearApps.pack(side=tk.RIGHT,padx=5,pady=5)

openFile = tk.Button(root,text="Set my Workspace",fg="black",bg="#f7cac9",command=addApp)
openFile.pack(side=tk.LEFT)

runApps = tk.Button(root,text="Start my Workspace",fg="black",bg="#f7cac9",command=runApps)
runApps.pack(side=tk.LEFT,padx=5,pady=5)

#Set the workspace window
for app in apps:
    label = tk.Label(frame,text=app)
    label.pack()

root.mainloop()

# Save the added apps to 'save.txt'
with open('save.txt','w') as f:
    for app in apps:
        f.write(app+',')