roll_no=[223610,223633,223616,223645,223642]
for index,roll in enumerate(roll_no):
    print(index,roll)
# we use enumerate function for get the value of index as the loops run
# we can also start our loop from our given index
c=int(input("enter the value of index in between 0 to 4: "))
if(c>=0 and c<=4 ):
    a=c
else:
    a=0
for  index,roll in enumerate(roll_no,start=a):
    print(index,roll)
