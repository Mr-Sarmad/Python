s={2,2,4,6,6,8}
print(s,type(s))
s2={5,9,2,1,5,6,4,8}
print(s.union(s2))#union function
print(s.issubset(s2))#subset function
(s.update(s2))
print(s)#update method of string 
cities={"Lahore","Karachi","Islamabad"}
cities2={"Islamabad","Peshawar","Dipalpur"}
cities.difference_update(cities2)
print(cities)
cities.intersection(cities2)
print(cities)
cities.symmetric_difference(cities2)
print(cities)
cities.add("Faisalabad")
print(cities) 
cities.remove("Karachi")
print(cities)
cities.pop()
print(cities)