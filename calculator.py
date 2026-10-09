# Calculator

# This calculator program has addition, subtraction, multiplication, division, and exponents.

print("""
calculator.py
""")

print('''
    [+] Addition
    [-] Subtraction
    [*] Multiplication
    [/] Division
    [^] Exponents
''')

operation = input('Choose an operation: ')

if operation == "+":
    a = int(input("Number 1: "))
    b = int(input("Number 2: "))
    print(a + b)
elif operation == "-":
    a = int(input("Number 1: "))
    b = int(input("Number 2: "))
    print(a - b)
elif operation == "*":
    a = int(input("Number 1: "))
    b = int(input("Number 2: "))
    print(a * b)
elif operation == "/":
    a = int(input("Number 1: "))
    b = int(input("Number 2: "))
    print(a / b)
elif operation == "^":
    a = int(input("Number 1: "))
    b = int(input("Number 2: "))
    print(a ** b)
else:
    print("Invalid operation.")
# You've reached the bottom!
    
