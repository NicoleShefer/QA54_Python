# Only performs calculator
def calculator(a:float, b:float, operator:str):
    if operator == "+":
        return a+b
    elif operator == "-":
        return a-b
    elif operator == "*":
        return a*b
    elif operator == "/":
        return a/b
        #ZeroDivisionError


#Parsing convert string into numbers
def pars(a_str:str, b_str:str, operator:str):
    a = float(a_str) #ValueError
    b = float(b_str) #ValueError
    return calculator(a, b, operator)


#Dialog
def run():
    try:
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        operator = input("Enter operator: ( + , - , * , / ) ")
        result = calculator(a, b, operator)
        print(f"Result: {result}")
    except ValueError as e:
        print(f"invalid input: {e}")
    except ZeroDivisionError as e:
        print(f"division by zero: {e}")
run()

