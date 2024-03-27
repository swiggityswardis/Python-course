# if statement = a block of code that will execute if it's condition is true
#                for boolean True, indented code will run
#                for boolean False, indented code will not run
#                else, will run if False over all if and/or elif conditions
# == is comparison
# =  is assignment

age = int(input("How old are you?: "))

if age == 100:
    print("You are a century old!")
elif age >= 18:
    print("You are an adult!")
elif age < 0:
    print("You haven't been born yet!")
else:
    print("You are a child!")


































