from src import calculator

choice = True

while choice:
    print("\n-------------------------")
    print("------ CALCULATOR -------")
    print("-------------------------")
    num1 = int(input("\nEnter first number: "))
    num2 = int(input("\nEnter second number: "))

    print("\nSelect an option")
    print("1.Addition")
    print("2.Subtraction")
    print("3.Multiplication")
    print("4.Division")
    choose = input("Enter Your option:")

    if choose in ("1", "2", "3", "4"):
        if choose == "1":
            result = calculator.add(num1, num2)
            print(num1, "+", num2, "=", result)

        elif choose == "2":
            result = calculator.sub(num1, num2)
            print(num1, "-", num2, "=", result)

        elif choose == "3":
            result = calculator.multi(num1, num2)
            print(num1, "*", num2, "=", result)

        elif choose == "4":
            result = calculator.div(num1, num2)
            print(num1, "/", num2, "=", result)
    else:
        print("-----------------")
        print("--Invalid Input--")
        print("-----------------")
        break

    new = input("\nWould you want to contine?  Enter 'y' or 'n': ")
    if new[0].lower() == "y":
        choice = True
    else:
        choice = False
        print("\n---------------------------")
        print(" Thank You. See You Later ")
        print("---------------------------")