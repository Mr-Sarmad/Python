def greet(fx):
    def mfx(*args,**kwargs):
        print("good Morning")
        fx(*args,**kwargs)
        print("Thank you")
    return mfx
@greet
def hello():
    print("HEllo World")

@greet
def add(a,b):
    print(a+b)

hello()
add(5,3)