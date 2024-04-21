from math import pi

def calculateArea(shapeName, width, height=1):
    area = 0
    if shapeName.upper() == "CIRCLE":
        area = pi * width ** 2
    elif shapeName.upper() == "SQUARE":
        area = width * width
    elif shapeName.upper() == "RECTANGLE":
        area = width * height
    elif shapeName.upper() == "TRIANGLE":
        area = 0.5 * width * height
    with open("result.txt", "w") as myfile:
        myfile.write(f"The shape is : {shapeName} and It`s area is: {area}")

shape = input("Enter the shape name: ")
if shape.upper() == "RECTANGLE" or shape.upper() == "TRIANGLE":
    width = int(input("Enter width : "))
    height = int(input("Enter height: "))
    calculateArea(shape, width, height)
elif shape.upper() == "SQUARE" or shape.upper() == "CIRCLE":
    width = int(input("Enter width : "))
    calculateArea(shape, width)
else:
    print("Enter a valid shape name")
