def double(a):
    return a*a
print(double(5))
#this is a function but we can also use this in a single line  anonumusly usch like 
double2=lambda x: x*2
cube=lambda x: x*x*x
square = lambda x: x*x
avg=lambda x,y,z:(x+y+z)/3
print(double2(4))
print(cube(3))
print(square(4))
print(avg(5,8,10))