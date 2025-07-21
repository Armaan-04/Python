def decorator(func):
    def wrapper():
        print("This is happening before the function is called.")
        func()
        print("This is happening after the function is called.")
    return wrapper

@decorator
def hello():
    print("Hello")
hello()