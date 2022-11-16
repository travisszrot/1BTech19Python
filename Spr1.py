#zad 1

a = int(input())
b = int(input())
c = int(input())

if a != b - 2 and a!=c-2 and b!=c-2 and a != b + 2 and a!=c+2 and b!=c+2 and a != b - 1 and a!=c-1 and b!=c-1 and a != b + 1 and a!=c+1 and b!=c+1 and a != b - 2 and a!=c-2 and b!=c-2 and a != b + 2:
  print("Zły kod")

else:
#   print("Dobry kod")


#zad 2

n= 1
x= 2
for i in range(1,100000,x+1):
  print (x%n)
 



