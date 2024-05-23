a=input("enter your number")
try:
    for i in range(1,11):
        print(f"{int(a)} * {i} ={int(a)*i} ")
except Exception as e:
    print(e)
print("some other imp lines")
print("code ends")
# so like these we can handle error in the codes by using exeption