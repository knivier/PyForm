from pathlib import Path
import json
import math


full_name = input('Hello, what is your full name? ')

if len(full_name) < 5:
    print("Name must be at least 5 characters")
    quit()
elif len(full_name) > 50:
    print("Name must be a max of 30 characters")
    quit()
else:
    print("Name verified.")

year = int(input('What is the year? '))
birth_year = int(input('What is your birth year? '))

weight = int(input('What is your weight? '))
unit = input('What units were used? L(bs) or (K)g: ')

if unit.upper() == "K":
    converted = weight / 0.45
    print(f"You are {converted} pounds ")
else:
    converted = weight / 0.45 * 0.45
    print(f"Conversion not required. Weight is already lb ({converted}lb) ")

height = int(float(input("What is your height? ")))
hunit = input('cm(centimeter) or in(inch)? ')
heq = ('cm/2.54')
if hunit == "cm":
    hcov = height/2.54
    print(f"You are {hcov}in high! (Converted CM to IN using {heq} )")
else:
    hcov = (height/2.54)*2.54
    print(f"Conversion not required")

country = input('Which country are you in? ')
providence = input('Which providence/state do you live in from ' + country + "? ")
city = input('What city do you live in from ' + providence + "? ")
age = year - birth_year
place = city + ", " + providence + ", " + country
colour = input("What is your favourite colour? ")

formatted_response = {
  "fullname": str(full_name),
  "age": str(age),
  "conbirthyear":  str(birth_year),
  "favcol": str(colour),
  "loc": str(place),
  "weight": str(converted) + "lb",
  "height": str(hcov) + "in"
}


json_file = json.dumps(formatted_response)
Path('details.json').write_text(json_file)
