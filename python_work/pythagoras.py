# A program to generate pythagorean triples.
# Each triple has the form (a, b, c) where a^2 + b^2 = c^2
# and a, b, c are positive integers.

for c in range(3, 25):
    for b in range(3, 25):
        for a in range(3, 25):
            if b >= c or a >= b :
                continue
            if a*a + b*b ==c*c:
                print(f"a={a} b={b} c={c}")
        	
