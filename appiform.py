from tkinter.simpledialog import askstring
from tkinter import *
from tkinter.simpledialog import askinteger
import json
import uuid

top = Tk()
top.geometry("100x100") 
name = askstring("Input", "Enter your full name") #name verification follows
if name is not None and len(name) < 5:
  print("Your name is too short")
  quit()
if isinstance(name, str) and len(name) < 5:
  print("Your name is too long!")
  quit()

year = askinteger("Input", "Enter the current year")
birth_year = askinteger("Input", "What is your birth year")
if year is not None and birth_year is not None:
    age = year - birth_year
    print(age)
else:
    print("Invalid input for year or birth year")
    quit()

weight = askinteger("Input", "What is your weight? ")
unit = askstring("Input", "What is the units for your weight? (K)ilogram or (L) pounds")
if unit.upper() == "K":
  converted = weight / 0.45
else:
  converted = weight

height = askinteger("Input", "What is your height? ")
hunit = askstring("Input", "Height in cm(centimeter) or in(inch)? ")
hcov = None  # Initialize hcov with a default value
if height is not None:
    if hunit == "cm":
        hcov = height / 2.54
        print(f"You are {hcov} in height! ")
    else:
        hcov = height
        print("No conversion required")
else:
    print("Invalid input for height")
    quit()

country = askstring("Input", "What is your country that you live in?")

data = {
    "Name:": name,
    "Age": age,
    "Weight": converted,
    "Height": hcov,
    "Residence Country": country
}

file_name = str(uuid.uuid4()) + "{}.json"
with open(file_name, 'w') as f:
    json.dump(data, f)
B = Entry(top)
B.place(x=50,y=50)
top.mainloop()
