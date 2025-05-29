# very_bad_example_script.py

print("Starting script...")  # Rule R001 violation (print)

def BadNameFunction():
    print("This function name is bad!")  # R001 print usage
    for i in range(5):
        print(i)
    # Missing docstring (R006)

def anotherBadFunc():
    # Missing docstring (R006)
    print("Another bad function here!")  # R001
    pass

def tooLongFunction():
    '''This docstring is too short'''
    for i in range(100):
        print(i)  # R001
    for j in range(50):
        print(j)  # R001
    for k in range(60):
        print(k)  # R001

# No if __name__ == '__main__' guard - R002
BadNameFunction()
anotherBadFunc()
tooLongFunction()