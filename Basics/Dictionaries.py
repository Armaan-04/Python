dict = {"Name" : "Armaan" , "Age" : 21 , "Marks" : 60.33 , 100 : "abc"}
print(dict)

#tuples , lists or dictionaries can be stored in a dictionary
#keys and names must be unique

dict2 = {"marks" : [12,44,32,67]}
print(dict2)

#INSERTION
dict3 = {"Fruits" : ["Banana" , "Apple", "Orange"]}
print(dict3)
dict3["Price"] = 100
print(dict3)

#UPDATE
dict4 = {"name":"python" , "version":3.9}
dict4["version"] = 4.0
print(dict4)

#DELETION
dict5 = {"name":"python" , "version":3.9}
del dict5['version']
print(dict5)

#GET METHOD
profile = {"name":"Armaan" , "age":21 , "salary":18000.00}
age = profile.get("age")
print(age)

#RETRIEVING ALL KEYS
keys = profile.keys()
print(list(keys))

#RETRIEVING ALL VALUES
values = profile.values()
print(list(values))

#ITEMS METHOD
all_items = profile.items()
print(list(all_items))

#POP METHOD
popped = profile.pop("age")
print(profile)

#POP ITEM -> removes the last item in the dictionary
popped_item = profile.popitem()
print(popped_item)
print(profile)

#CLEAR
cleared = profile.clear()
print(profile)

#DICTIONARY COMPREHENSION
dict6 = {x : x*x for x in range (1,6)}
print(dict6)

#NESTED DICTIONARY
dict7 = {"python": {"name":"python" , "use_case":["ai,ml,webdev,ds"]}
         ,"java": {"name":"java" , "use_case":["app dev"]}}
print(dict7) 

#LOOPS
for k in dict5.values():
    print(k)
