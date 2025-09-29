with open('/Users/KIIT0001/Desktop/Python/Basics/FileHandling/data.txt' , 'w') as file:
    content = input('Enter content to write: ')
    file.write(content)
    print('Saved.')