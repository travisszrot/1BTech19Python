# 1. Sprawdzenie czy liczba jest pierwsza
# liczba pierwsza - liczba, która się dzieli tylko przez 1 i samą siebie
# 2,3,5,7,11,13,17,19,23 .. itd
# dzielniki właściwe - dzielniki liczby poza 1 i nią samą

# n = int(input())
# for i in range(2, n):
#     if n % i == 0:
#         print("Liczba nie jest pierwsza")
#         exit(0)
# print("Liczba jest pierwsza")

# 2. Generowanie liczb pierwszych


# n = int(input("do ilu mam szukać liczb pierwszych/n"))

# for i in range(2, n+1):
#   for j in range(2,i):
#     if i % j == 0:
#       flaga = False
#       break
# if flaga:
#   print(i, end= " ")


# p = int(input("do ilu mam szukać liczb pierwszych/n"))
# q = int(input("do ilu mam szukać liczb pierwszych/n"))

# for i in range(p, q+1):
#   for j in range(2,i):
#     if i % j == 0:
#       flaga = False
#       break
# if flaga:
#   print(i, end= " ")



p = int(input("do ilu mam szukać liczb pierwszych/n"))

while 1:
  flaga = True 
for j in range(2,int(i**0.5)+1):
  if i % j == 0:
    flaga = False
    break
    