x = input("Enter Number 1: ")
y = input("Enter Number 2: ")
try:
    z = x / int(y)
except ZeroDivisionError as e:
    print("Divide by Zero: ",e)
    z = None
except TypeError as e:
    print('Type error exception: ')
    z = None
print("Division is: ", z)
