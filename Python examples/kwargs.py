# **kwargs = parameter that will pack all arguments into a dictionary
#            useful so that a function can accept a varying amount of keyword arguments
#            ** is the important part / dictionary is renamed 

def hello(**kwargs):
    #print("hello "+kwargs["first"]+" "+kwargs["last"])
    print("hello",end=" ")
    for key,value in kwargs.items():
        print(value,end=" ")

hello(title="mr.",first="dick",middle="face",last="mcgee")










































