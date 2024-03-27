# scope = the region that a variable is recognized
#         a variable is only available from inside the region it is created
#         a global and locally scoped versions of a variable can be created

name = "guy" # global scope (available inside and outside functions)

def display_name():
    name = "your mom" # local scope (available ony inside the function)
    print(name)

display_name()
print(name)


# L = Local
# E = Enclosing
# G = Global
# B = Built in





































