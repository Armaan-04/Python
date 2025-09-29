with open('C:/Users/KIIT0001/Desktop/Python/Basics/FileHandling/data.txt' , 'a') as file:
    content = input("Enter data to append: ")
    file.write(content)
    print("Appended successfully.")
    
    
