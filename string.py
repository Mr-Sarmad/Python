name="Sarmad"
firend='Abdur Rehman'
print("hello",name)
print('My firned name is',firend)

apple=''' my name is sarmad
and i am 19 years old 
i live in okara 
adn i am studing bioinformatics '''
print(apple)
# jb multiple lines pr stirng use krni h tw triple sting use kry g  

f='Hi,"he wants apple".'
print(f)
# jb double qote ko print krna h tw single qote use kry g
for character in apple:
    print(character)
# is sy hm sary character ko show krava skty hn

print(name[2])
# this is indexing like array hm issy string value ka cahracter acces kr skty hn

print(len(apple))
# string ki length k pata krny k liye is length fucntion k use kry ga 
for i in apple:
    print (i)
print(apple[0:9])
# apni mrzi ki string mn sy part k use krny k liye isy use kry ga 

a="Sarmad"
# stings are immutable
print(a.lower())
# string ko lower letter krny k liye k lower() function k use krty han 
print(a.upper())
# string ko upper letter mn use krny k liye upper() function k use krty h 
b="!!!! kia hal h !!!!"
print(b.rstrip("!"))
# string k right side strip krny k liye rstrip() function use htA H 
print(a.replace("Sarmad","Harry"))
# replace function string mn already value k chnge krny k liye use hta 
print(b.split())
# string function string mn space bar k remove krny k liye use hta h 
c="i am a boy"
print(c.capitalize())
# captalize function fisrt letter captalize krny k liye use hta 
print(len(c))
print(c.center(50))
# center function jese c++ mn setw use krty th y b wase hi use hta h 
print(c.count("a"))
d="Welcome to my code !!!!"
print(d.endswith("!"))
# enswith function is liye use hta k pata kr sky k given string hmry put kiye g character sy hi end h rhy h 
print(d.endswith("to",4,10))
# hm isy given size sy b kr skty hn
print(d.find("to"))
# find function hm koi b chz string mn b use krny k liye krty hn 
print(d.isalnum())
# alnum funtion is liye use hta h k given string mn numerical values hi use h rhy h jis mn A-Z ,a-z,0-9
print(d.isalpha())
# isalpha is liye use hta h k given sting mn A-Z or a-z just use h rhy 
print(d.isprintable())
# isprintable function is liye use hta h k string mn given all character printable h y nai
print(d.isspace())
# issapce use hta h k given string mn sapce use hoi k nai
print(d.istitle())
# title function is use to check kia given string k title captalize h y nai 
print(d.startswith("w"))
print(d.swapcase())
# swapcase function j words capital h uny lower case or j lower case hn unhy upper case mn convert krny k liye use hta 
print(d.title())
# titile function sab word k fisrt character k capital krny k liyw use hta