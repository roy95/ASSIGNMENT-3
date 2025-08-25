what=input("what you want to perform: \n 1.Factorial: \n 2.Calculation: ")
what=int(what)
if what==1:
# Factorial
    def factorial(a):
        if a < 2:
            return 1
        else:
            return a * factorial(a - 1)

    z=int(input("Enter a Number: "))
    l=factorial(z)
    print("Factorial of",z, "is: ",l)

elif what==2:
# calculation using math module
    import math
    b=int(input("Enter the number you want to perform: "))
    print("Square root of",b,"is: ",math.sqrt(b))
    print("logarithm of",b,"is: ",math.log(b))
    print("Sine",b,"degree is: ",math.sin(b))
else:
     print("Enter a valid selection")

