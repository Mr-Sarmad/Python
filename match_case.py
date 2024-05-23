x=int(input("enter your value"))
match x:
    # if x=0
    case 0:
        print("x is zero")
    case 4:
        print("x is equal to four")
    case _:
        print("none of the above case is true ")