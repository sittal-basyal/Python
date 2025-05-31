num1 = int(input("Enter one number: "))
num2 = int(input("Enter another number: "))

choice = input("Enter required operator (+, -, *, /): ")
if choice=="/" and num2==0:
    while num2 == 0:
                num2 = int(input("Cannot divide by zero. Enter another number: "))

def calc(num1, num2, choice):
    match choice:
        case "+":
            return num1 + num2
        case "-":
            return num1 - num2
        case "*":
            return num1 * num2
        case "/":
            return num1 / num2
        case _:
            return "Invalid operator"

result = calc(num1, num2, choice)
print(f"{num1} {choice} {num2} = {result}")
