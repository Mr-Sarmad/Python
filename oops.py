class person:
    Name="Sarmad"
    age=20
    Study="BSc"
    def info(self):
        print(f"My name is {self.Name},and my age is: {self.age}.I am a {self.study} student")
a=person()
b=person()
c=person()

a.Name="Ali"
a.age=21
a.study="F.A"

b.Name="Sagar"
b.age=20
b.study="FSc"

c.Name="Rahsid"
c.age=19
c.study="FSc"

a.info()
c.info()
b.info()
