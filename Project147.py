from tkinter import *
root = Tk()

root.title("Name Encoder")
root.geometry("4000x2000")
root.configure(bg="blue")

lab1 = Label(root, text="Enter your Name here:", bg="blue", fg="yellow")
lab2 = Label(root, text="Encoded Name: ", bg="blue", fg="yellow")
inp = Entry(root, bg="yellow", fg="blue")

def encode():
    lab2["text"] = "Encoded Name: "
    for x in inp.get():
        lab2["text"]+=chr(ord(x)+1)

btn = Button(root, bg="yellow", fg="blue", command=encode, text="Encode")

lab1.place(relx=0.5, rely=0.425, anchor=CENTER)
lab2.place(relx=0.5, rely=0.525, anchor=CENTER)
inp.place(relx=0.5, rely=0.475, anchor=CENTER)
btn.place(relx=0.5, rely=0.575, anchor=CENTER)

root.mainloop()
