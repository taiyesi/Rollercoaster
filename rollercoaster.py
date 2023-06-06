print("Welcome to the grand roller coaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height > 120:
    print("You can ride the rollercoaster!")
    age = int(input("How old are you? "))
    if age < 12:
        bill = 5
        print("Pay $5")
    elif age <= 18:
        bill = 7
        print("Pay $7")
    elif age >= 45 and age <= 55:
        bill = 0
        print("your ride is free")
    else:
        bill = 12
        print("Pay $12") 

    wants_photo = input("Do you want a photo taken? Y or N: ")
    if wants_photo == "Y":
        bill = bill + 3
    
    print(f"your final bill is {bill}")

else:
    print("Sorry, you're too short for this ride")

"""number = int(input("Which number do you want to check? "))
if number % 2:
    print("The number is not even") 
else:
    print("The number is even")"""   