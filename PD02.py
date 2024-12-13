
#2. uzdevums

n = int(input("Ievadi skaitli n: "))
summa = 0
for i in range(1, n + 1):
  summa += i
  print(f" {summa}")

#3. uzdevums
h = int(input("Ievadi skaitli h: "))
reizinājums = 1
for i in range(1, n + 1):
  reizinājums *= i
print(f" {reizinājums}")

#4. uzdevums
a = int(input("Ievadi skaitli a: "))
for i in range(a, -1, -1):
  print(i)

#5. uzdevums

l = int(input("Ievadi trijstūra augstumu l: "))
for i in range(l):
  print(" " * i + "*" * (2 * (h - i) - 1))

#6. uzdevums

import random
dators = random.randint(1, 10)

while True:
  speletajs = int(input("Ievadi skaitli: "))
  if speletajs < dators:
    print("Lielāks")
  elif speletajs > dators:
    print("Mazāks")
  else:
    print("Uzminēts!")
    break