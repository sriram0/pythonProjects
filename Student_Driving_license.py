# Basic tkinter template
from tkinter import *
root = Tk()
root.title("Driver's License")
root.geometry("1000x500")

root.configure(bg="white")
canvas=Canvas(root,width=400,height=250)
canvas.create_image(0,0,anchor=NW)
canvas.create_rectangle(0, 0, 400, 45, fill="#F6091E")


label_heading = canvas.create_text(200,20, font=('Times', '24', 'bold italic') ,text="Driving License", fill = "white")
label_id_tag = canvas.create_text(25,60, font=('Times', '14', 'bold') ,text="ID :")
label_name_tag = canvas.create_text(30,100, font=('Times', '12', 'bold') ,text="Name :")
label_dob_tag = canvas.create_text(52,120, font=('Times', '12', 'bold') ,text="Date of birth :")
label_pin_tag = canvas.create_text(32,140, font=('Times', '12', 'bold') ,text="Pin no. :")
label_address_tag = canvas.create_text(36,160, font=('Times', '12', 'bold') ,text="Address :")
label_vehicle_type_tag = canvas.create_text(155,180, font=('Times', '12', 'bold') ,text="Authorisation to drive the following vehicles :")

# Create all the labels required to be displayed
label_id = Label(root)
label_name = Label(root)
label_dob = Label(root)
label_pin = Label(root)
label_address = Label(root)
label_vehicle_type = Label(root)

# Define the function
def myFunc():
    global label_id
    label_id["text"] = input("What id? ")
    global label_name
    label_name["text"] = input("What is your name? ")
    global label_dob
    label_dob["text"] = input("What is your date of birth? ")
    global label_pin
    label_pin["text"] = input("What pin? ")
    global label_address
    label_address["text"] = input("What is your address? ")

    while True:
        i = input("What vehicle type can you drive? (type 2 for a two wheeler, 4 for a four wheeler, or b for both)? ")
        if i=="2":      
            label_vehicle_type["text"] = "2 wheeler"
            break
        elif i=="4":
            label_vehicle_type["text"] = "4 wheeler"
            break
        elif i=="b":
            label_vehicle_type["text"] = "2 and 4 wheelers"
            break
        print(type(i))
    
    
# Create a button
button1 = Button(root, text="Show Card", command=myFunc)


button1.configure(width = 20 , activebackground = "#9EC6EE", relief= FLAT)
button1_window = canvas.create_window(200, 235, anchor=CENTER, window=button1)
label_id_window = canvas.create_window(80, 60, anchor=CENTER, window=label_id)
label_name_window = canvas.create_window(100, 100, anchor=CENTER, window=label_name)
label_dob_window = canvas.create_window(140, 120, anchor=CENTER, window=label_dob)
label_pin_window = canvas.create_window(85, 140, anchor=CENTER, window=label_pin)
label_address_window = canvas.create_window(130, 160, anchor=CENTER, window=label_address)
label_vehicle_no_window = canvas.create_window(335, 180, anchor=CENTER, window=label_vehicle_type)
canvas.pack()

# tkinter basic template end statement
