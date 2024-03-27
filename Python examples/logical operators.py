# logical operators (and,or,not) = used to check if two or more conditional statements are True
# and, both conditions must be True to produce True
# or, at least one condition must be True to produce True
# not, flips True condition to False




temp = int(input("What is the temp outside?: "))

if temp >= 0 and temp <= 30:
    print("the temp is good outside")
elif temp < 0 or temp > 30:
    print("the temp is bad today!")
elif not(temp >= 0 and temp <= 30):
    print("this condition is was True")
    





































