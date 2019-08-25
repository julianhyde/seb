#
#
# We want to print:
# 
#    a      c       e
#  ---- + ---- =  ----
#    b      d       f
#
# For example, given (3, 4, 1, 10), we should print
#
#    3      1      17
#  ---- + ---- =  ----
#    4     10      20
#

a = int(input("Top 1? "))
# print(a)
b = int(input("Bottom 1? "))
# print(b)
c = int(input("Top 2? "))
# print(c)
d = int(input("Bottom 2? "))
# print(d)
e = (c * b + a * d)
f = (b * d)
print("")
print(f"{a:4}   {c:4}   {e:4}")
print(" ---- + ---- = ----")
print(f"{b:4}   {d:4}   {f:4}")
print("")
