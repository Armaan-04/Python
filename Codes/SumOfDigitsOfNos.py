original_num = int(input("Enter a number: "))
result = 0
num = original_num
while num > 0:
    
    digit = num % 10
    result = digit + result
    num = num // 10
print("The sum of digits of " , original_num , " is " , result)