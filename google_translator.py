from tkinter import *
from tkinter import ttk
from googletrans import Translator, LANGUAGES

def change(text, src, dest):
    src1=src
    dest1=dest
    print(src)
    print(dest)
    print(text)
    trans = Translator()
    trans1 = trans.translate(text, src=src1, dest=dest1)
    print(trans1.src)
    print(trans1.dest)
    print(trans1.text)
    return trans1.text

def data():
    s=combobox_source.get()
    d=combobox_destination.get()
    masg=Source_txt.get(1.0,END)
    print(masg)
    textget=change(text=masg,src= s, dest=d) 
    print(textget)
    destination_txt.delete(1.0,END)
    destination_txt.insert(END,textget)

root=Tk()
root.title("Translator")
root.geometry("500x700")
root.config(bg="blue")

lable_txt=Label(root,text="TRANSLATOR", font=("Time New Roman", 20, "bold"), bg= "Red")
lable_txt.place(x=100, y=40, height=50, width=300)

frame = Frame(root).pack(side=BOTTOM)

lable_txt=Label(root,text="SOURCE TEXT", font=("Time New Roman", 20, "bold"), fg="Black", bg="Blue")
lable_txt.place(x=100, y=100, height=30, width=300)


Source_txt=Text(frame, font=("Time New Roman", 20, "bold"),wrap=WORD)
Source_txt.place(x=10, y=130, height=150, width=480)

list_txt= list(LANGUAGES.values())

combobox_source=ttk.Combobox(frame, value=list_txt, font=("Time New Roman", 20, "bold"))
combobox_source.place(x=10, y=300, height=40, width=150)
combobox_source.set("english")

button_change = Button(root, text="Translate", font=("Time New Roman", 20, "bold"), relief=RAISED, command=data)
button_change.place(x=170, y=300, height=40, width=150)

combobox_destination=ttk.Combobox(frame, value=list_txt, font=("Time New Roman", 20, "bold"))
combobox_destination.place(x=330, y=300, height=40, width=150)
combobox_destination.set("english")

lable_txt=Label(root,text="DESTINATION TEXT", font=("Time New Roman", 20, "bold"), fg="Black", bg="Blue")
lable_txt.place(x=100, y=360, height=30, width=300)

destination_txt=Text(frame, font=("Time New Roman", 20, "bold"),wrap=WORD)
destination_txt.place(x=10, y=400, height=150, width=480)

root.mainloop()