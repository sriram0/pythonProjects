from tkinter import *
root = Tk()

root.title("Name Encrypter")
root.geometry("4000x2000")
root.configure(bg="blue")
l = Label(root, text="Enter your Name to Encrypt!", fg="yellow", bg="blue") 
inp = Entry(root)
label = Label(root, text="Encrypted Name: ", fg="yellow", bg="blue")
def run():
    for l in inp.get():
        label["text"]+=" "+str(ord(l))
    label.place(relx=0.5, rely=0.5, anchor=CENTER)

btn = Button(root, text="Show Encrypted Name", command=run, fg="blue", bg="yellow")
l.place(relx=0.5, rely=0.4, anchor=CENTER)
inp.place(relx=0.5, rely=0.45, anchor=CENTER)
btn.place(relx=0.5, rely=0.55, anchor=CENTER)

root.mainloop()
