import random
import time
# // UtilityBox Version 2 //
# // Made by Federal //


# Right here will be all of the functions


def calc_short_for_calculator_btw():
    print("""
[+] Addition
[-] Subtraction
[*] Multiplication
[/] Division
[^] Exponents
""")
    operation = input("Choose an operation: ")
    if operation == "+":
        a = int(input("Number One: "))
        b = int(input("Number Two: "))
        print(a + b)
    elif operation == "-":
       	a = int(input("Number One: "))
       	b = int(input("Number Two: "))
       	print(a - b)
    elif operation == "*":
       	a = int(input("Number One: "))
       	b = int(input("Number Two: "))
       	print(a * b)
    elif operation == "/":
       	a = int(input("Number One: "))
       	b = int(input("Number Two: "))
       	print(a / b)
    elif operation == "^":
       	a = int(input("Number One: "))
       	b = int(input("Number Two: "))
       	print(a ** b)
    else:
        print("Invalid operation.")
# Function name is calc_short_for_calculator_btw (short for calculator btw)

def rockpaperscissors():
    print("Rock.. Paper.. Scissors.. SHOOT!")
    print("""
[1] Rock
[2] Paper
[3] Scissors
""")
    userchoice = input("What did you pick? ")
    botchoice = random.choice(["Rock!", "Paper!", "Scissors!"])
    print("The bot picked...")
    time.sleep(2)
    print(botchoice)
def roll():
    fihfiwuwghufefewfwewewfdfwwwfg = random.choice(["WIN", "Lose"])
    print(fihfiwuwghufefewfwewewfdfwwwfg) # I had a brainfart typing this out...

# Now on to the main code (finally)

print("UtilityBox Version 2 By Federal")
print("""
[1] Calc (short for calculator btw)
[2] Rock paper scissors (BOT)
[3] Gamble (50/50)
[4] Quit
## Note: doesnt have the lot of features yet cuz i made this at 3 am lol
""")
choice = int(input(">> "))
if choice == 1:
    calc_short_for_calculator_btw()
elif choice == 2:
    rockpaperscissors()
elif choice == 3:
    roll()
elif choice == 4:
   quit()
