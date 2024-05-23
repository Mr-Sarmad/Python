# # conditional operators
# # > greater than 
# # < less than 
# # == equal to 
# # <= less than equal to 
# # >= greater than equal to 
# # =! not equal to 
# a=int(input("what is your age: "))
# print(a>18)
# print(a<18)
# print(a==18)
# print(a!=18)
# print(a<=18)
# print(a>=18)
# if(a>18):
#     print("you can drive")
# else:
#     print("you cannot drive")
# num=int(input("enter your number: "))
# if(num<0):
#     print("the num is negative")
# elif(num>0):
#     if(num<=10):
#         print("the num is in between 1 to ")
#     elif(num<=20):
#         print("the num is in between 11-20")
#     else:
#         print("the num is greater than 20")
# else:
#     print("the num is zero")
import time
timestamp=int(time.strftime("%H"))
print(timestamp)
if(timestamp<=5 and timestamp>=11):
    print("Good morning sir")
    if(timestamp==10):
        print("its tea break sir")
    elif(timestamp==11):
        print("its end of tea break sir ")
    else:
        print("How are you sir ")
elif(timestamp<=11 and timestamp>=16 ):
    print("good afternoon  sir ")
    if(timestamp==13):
        print("its lunch break sir")
    elif(timestamp==14):
        print("its end of lunch break sir")
else:
    print("good evening sir")
    
