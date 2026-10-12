""""
def div_int(a,b):
    return a/b
print("Start program")
result = div_int(10,0)
print(result)
print("End program")


# Try/Except

print("Hello World")
try:
    result = 10/0
    print(result)
except Exception as e:
    print("An error occured:" , e)

#print("End program")

try:
    number = int(input("Enter a number: "))
    result = 100 / number
    print("Result:", result)
except ValueError:
    print("Invalid input, try again")
except ZeroDivisionError:
    print("You cannot divide by zero, try again")

"""

def is_number(text):
    try:
        float(text)
        return True
    except (ValueError, TypeError):
        return False

print(is_number("314"))
print(is_number("3.14"))
print(is_number("3,14"))
print(is_number("Nicole"))
print(is_number(None))

print()

try:
    value = int("39")
except ValueError:
    print("An error occurred:")
else:
    print("An error occurred" , value)
finally:
    print("End program")






