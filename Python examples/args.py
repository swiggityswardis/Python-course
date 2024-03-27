# *args = parameter that will pack all arguments into a tuple
#         useful so that a function can accept a varying amount of arguments
#         *stuff is the same as *args / *anyword

def add(*stuff):
    sum = 0
    stuff = list(stuff)
    for i in stuff:
        sum += i
    return sum

print(add(1,3,4,5,6,22,1109,74))

































