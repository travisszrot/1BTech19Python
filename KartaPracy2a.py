# # # # #ZAD 1

# # # # a,b = int(input()),int(input())
# # # # if (a + b) % 2 ==0:
# # # #   print("TAK")
# # # # else:
# # # #   print("NIE")

# # # # # # ZAD 2

# # # # a = int(input())
# # # # g = int(input())
# # # # if (a+g%2)==(a*g):
# # # #   print("TAK")
# # # # else:
# # # #   print("NIE")

# # # # ZAD 3
# # # k, l, m = int(input()), (input()), (input())
# # # if k == l:
# # #   print("NIE")
# # # elif l == m:
# # #   print("NIE")
# # # elif m == k:
# # #   print("NIE")
# # # else:
# # #   print("TAK")

# # #ZAD 4

# # a,b,c,d = int(input()),int(input()),int(input()),int(input())
# # if a<b and a<c and a<d:
# #   print("najniejszą liczbą jest (a)", a) 
# # if b<a and b<c and b<d:
# #   print("najniejszą liczbą jest (b)", b) 
# # if c<a and c<b and c<a:
# #   print("najniejszą liczbą jest (c)", c) 
# # if d<a and d<b and d<c:
# #   print("najniejszą liczbą jest (d)", d) 

# # #ZAD 5

# a,b,c = int(input()),int(input()),int(input())

# if a+b>c and b+c>a and a+c>b:
#   print ("liczby spełniają nierówność trójkąta")
# else:
#   print ("liczby nie spełniają nierównośći trójkąta")

# #ZAD 6

a,b,c = int(input()),int(input()),int(input())
if a**2 < b**2 + c**2:
  print("ostrokątny")
elif a**2 + b**2 == c**2:
  print("prostokątny")
elif a**2 > b**2 + c**2:
  print("rozwartokątny")


  


