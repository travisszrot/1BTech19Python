a = int(input())
b = int(input())
c = int(input())
d = int(input())

x, y = b, d
ilocz = x * y
while y > 0:
  x, y = y, x % y
nww = ilocz // x 

print(f"{a}/{b} + {c}/{d} = ?/{nww} + ?/{nww} = ?/{nww}")


