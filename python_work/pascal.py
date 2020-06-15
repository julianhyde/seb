# A program to print Pascal's triangle.

a = [0, 1, 0]
# a = [0, 1, 1, 0]
# a = [0, 1, 2, 1, 0]
for n in range(1, 20):
   # print line, e.g. '1', '1 1', '1 2 1', '1 3 3 1'
      print(f"{n} {a}")
      old_a = a
      a = []
      a.append(0)
      for i in range(1, len(old_a)):
         a.append(old_a[i - 1] + old_a[i])
      a.append(0)

# End
  