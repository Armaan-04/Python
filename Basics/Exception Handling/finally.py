try:
    file = open('/Users/KIIT0001/Desktop/Python/Basics/Exception Handling/errors.txt')
    content = file.read()
    print(content)

except FileNotFoundError:
    print("File not found")

finally: 
        file.close()
print("File operation completed.")
    