squares = []
differences = []
x = 0
for value in range(1,11):
	previous = x
	x = value ** 2
	squares.append(x)
	differences.append(x - previous)
print(squares)
print(differences)
