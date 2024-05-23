# class person():
#     def __int__(self):
#         print("I am a person")
    
#     def info(self):
#         print(f"{self.name} is a {self.occ}")

# a=person()

class persn:
    def __int__(self,n,oc):
        print("i AM a person")
        self.nam=n
        self.oc=oc
    def inf(self):
        print(f"{self.nam} is a {self.oc}")

c=persn("Sarmad","Developer")
d=persn("Ali","Friend")
c.inf()
d.inf()
