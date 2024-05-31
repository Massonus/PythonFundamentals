import calculations as calc

print("1. To choose addition")
print("2. To choose subtraction")
print("3. To choose multiplication")
print("4. To choose division")
user_choice = input("Enter your choice: ")

match user_choice:
    case "1":
        print("Result:", calc.plus(int(input("Enter a first number: ")), int(input("Enter a second number: "))))
    case "2":
        print("Result:", calc.minus(int(input("Enter a first number: ")), int(input("Enter a second number: "))))
    case "3":
        print("Result:", calc.multiply(int(input("Enter a first number: ")), int(input("Enter a second number: "))))
    case "4":
        print("Result:", calc.divide(int(input("Enter a first number: ")), int(input("Enter a second number: "))))
    case _:
        print("Invalid choice, try again")
