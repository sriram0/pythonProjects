from tkinter import *
root = Tk()
root.geometry("1000x500")
root.title("Fibonacci Series")

sl = Label(root, text="0, 1, 1")
fl = Label(root)



def fibo(): 
    counter = 0;
    numOfTimes =int(input("how many? "))-3  
    currentNums = [0, 1, 1];
    while counter<numOfTimes:
        currentNums[0] = currentNums[1]
        currentNums[1] = currentNums[2]
        currentNums[2] = currentNums[0] + currentNums[1]
        sl["text"]+=", "+str(currentNums[2])
        counter+=1
    fl["text"] = "The Variable Python Flower type "+str(numOfTimes+3)+" is fully bloomed and has "+str(currentNums[0])+" spirals on the left and "+str(currentNums[1])+" on the right making a total of "+str(currentNums[2])+" spirals."

sl.pack()
fl.pack()
fibo()
root.mainloop()
