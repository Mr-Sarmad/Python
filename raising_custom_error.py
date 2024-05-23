# we can raise custom error 
a=input("give the input ")
if(a!="quit"):
    raise quitError("given input shuld be quit")
else:
    print("quit")