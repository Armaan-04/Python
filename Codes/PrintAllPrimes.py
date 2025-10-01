LowerLimit = int(input("Enter Lower Limit: "))
UpperLimit = int(input("Enter Upper Limit: "))

print("The prime numbers from" , LowerLimit , "to" , UpperLimit , "are: ")

for num in range (LowerLimit , UpperLimit + 1):
    if num > 1:
        for i in range (2 , num):
            if num % i == 0:
                break
        else:
            print(num)
