from tkinter import *

root = Tk()
root.title("Project 146")
root.geometry("2000x1000")

label = Label(root, text="0, 1, 1")
Tinput = Entry(root)

def do():
    counter = 0
    nums = [0, 1, 1];
    sumN = 2
    label["text"] = "0, 1, 1"
    while counter<int(Tinput.get())-3:
        nums2 = nums[1:]
        nums[:2] = nums2
        nums[2] = nums[0] + nums[1]
        label["text"]+= ", "+str(nums[2])
        sumN+=nums[2]
        counter+=1
    label["text"]+="\n Total: "+str(sumN)

btn = Button(root, text="Show", command=do)

btn.pack()
label.pack()
Tinput.pack()
Tinput.focus_set()

root.mainloop()
