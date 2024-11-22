 #1. uzdevums

x1 = 5
x2 = 1.5
x3 = "hello world"
print(x1, x2, x3)

 #2. uzdevums
 
x = int(input("Ievadi veselu skaitli "))
y = int(input("Ievadi veselu skaitli "))
print(x+y)
print(x-y)
print(x*y)
print(x/y)

 #3. uzdevums
 
x = int(input("Ievadi veselu skaitli "))
if x > 0:
    print("x ir pozitīvs")
    
if x < 0:
    print("x ir negatīvs")
    
if x == 0:
    print("x ir nulle")
    
 #4. uzdevums
 
x = int(input("Ievadi veselu skaitli "))
y = int(input("Ievadi veselu skaitli "))

result = 4 * x ** (y + 3) + 15 *y
print (result)

result = (5 * y ** x - 144 * x + 2) / ((x + y) ** 2)
print (result)

result = (2 + x - 2 * x * y) / (y / (x + y))
print (result)

 #5. uzdevums
 
atzime = int(input("Ievadi atzimi "))
if 8<atzime<10:
    print("A")
elif 6<atzime<9:
    print("B")
elif 4<atzime<7:
    print("C")
elif 2<atzime<5:
    print("D")
elif 0<atzime<3:
    print("E")
else: 
    print("F")
    
    