print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ").lower()
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ").lower()
extra_cheese = input("Do you want extra cheese? Y or N: ").lower()

if size == "s":
    pizza = 15
elif size == "m":
    pizza = 20
elif size == "l":
    pizza = 25
else:
    pizza = 0

if pepperoni == "y":
    if size == "s":
        pep = 2
    else:
        pep = 3
else:
    pep = 0

if extra_cheese == "y":
    cheese = 1
else:
    cheese = 0

final_bill = pizza + pep + cheese

if final_bill > 0:
    print(f"Your final bill is: $ {final_bill}")
else:
    print("You entered an invalid number")