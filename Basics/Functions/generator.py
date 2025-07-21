def CountDown(num):
    while num > 0:
        yield num #yield values one at a time
        num-=1
        
#using the generator
for number in CountDown(5):
    print(number)