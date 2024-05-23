for i in range(5):
    print(i)
else:
    print("there is no i")

# we can also use else in the while loop

i=0
while(i<8):
    print(i)
    i=i+1
else:
    print("there is no more i")

# if we break the loop before the else statement the else statement didn't work

i=0
while(i<8):
    print(i)
    i=i+1
    if (i==7):
        break
else:
    print("there is no more i")