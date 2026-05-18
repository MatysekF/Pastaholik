def information():
    try:
        num1 = input("enter a first number: ")
        num2 = input("enter a second number: ")
        operator = input("enter a operator- +,-,*,/ ")
        if operator == "*":
            return float(num1) * float(num2)
        elif operator == "/":
            return float(num1) / float(num2)
        elif operator == "+":
            return float(num1) + float(num2)
        else:
            return float(num1) - float(num2)
    except ZeroDivisionError:
        print("Sorry, zero division")
        return "Error"
    except Exception as err:
        print("Sorry, something went wrong")
        return "Error"
print(information())










