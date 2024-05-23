try:
    l=[1,2,3,6,5,4,7]
    i=int(input("enter your value"))
    print(l[i])
except:
    print("index error")
# we use try except like this but in case of a function
def list():
    try:
        l=[1,2,5,6,7,8]
        i=int(input("enter your num"))
        print(l[i])
        return 1
    except:
        print("index error")
        return 0
    finally:
        print("i am always excute")

a=list()
print(a)
# so we use finally if we want to excute all the code in function after the return statement