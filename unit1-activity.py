#unit 1 activity 
#Author: Addiosn Chan
#Date: March,4 2024

# conditional statements

def numbers_of_feet (chicken, cow):
    return ((chicken * 2) + (cow * 4))

chicken = float(input("How many chicken are there in the farm?"))
cow = float(input("How many cows are there in the farm?"))

feet = numbers_of_feet(chicken, cow)
print(f"The number of feet is {feet}")

if feet > 100:
    print("There are more than 100 feet in the farm")

elif feet < 100:
    print("There are less than 100 feet in the farm")

else:
    print("There are 100 feet in the farm")

