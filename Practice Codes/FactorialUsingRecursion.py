def fact(num):
    if num == 0:
        return 1
    else:
        return (num * fact(num - 1))
    
num = int(input("Enter a number: "))
result = fact(num)
print("The factorial of " , num , " is " , result)