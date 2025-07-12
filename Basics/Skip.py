start = int(input("Enter start: "))
stop = int(input("Enter stop: "))

if(start>stop):
    print("Stop is greater than start")
else:
    skip=int(input("Enetr the number you want to skip: "))

for i in range(start,stop):
    if i == skip:
        continue
    print(i)