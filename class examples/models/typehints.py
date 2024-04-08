def greeting(name):
    return 'Hello ' + name



# is a function that takes a string as an argument and returns a string
# the second snippet is a function that takes a string as an argument and returns a string
# the difference is that the first snippet uses type hints to specify the type of the argument and the return value

def greeting(name: str) -> str:
    return 'Hello ' + name


s