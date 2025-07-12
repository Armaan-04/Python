text1 = "My name is Armaan Alam"
s = (text1[1:8:2])
print(s)


number= " 10 "
print(number * 15)


name = "Armaan"
s_name = "Alam"
print ("Hi",  name + s_name)


email = "user@2004"
if "@" in email:
    print("Valid email")
else:
    print("Invalid email")
    

#.lower() converts the string to lower case
#.upper() converts the string to uppercase
#capitalize() capitalises the first letter
#title() capitalises the first letter of every word in a sentence
#swapcase() swaps the upper case to lower case and lower case to upper case


text2 = "Python programming"
print(text2.find("h"))


text3 = "Python programming"
print(text3.replace("Python" , "Java"))
    

str = "a , b , c  , d"  
s=(str.split(","))
print(s)
print("." .join(s))


str1="Python"
print(str1.startswith("P"))
print(str1.endswith("s"))
print(str1.isalpha())
print(str1.isdigit())
print(str1.isalnum())
