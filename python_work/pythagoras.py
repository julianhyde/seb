# A program to generate pythagorean triples.
# Each triple has the form (a, b, c) where a^2 + b^2 = c^2
# and a, b, c are positive integers.

def gcd(e, f):
    if e == 0:
        if f == 0:
            return 1 # special case: gcd(0, 0) is 1
        else:
            return f # special case: gcd(0, x) is x
    elif e < 0:
        return gcd(-e, f)
    elif f < 0:
        return gcd(e, -f)
    elif e == f:
        return e
    elif e < f:
        return gcd(e, f - e)
    else:
        return gcd(e - f, f)


print(f"   a    b    c")
print(f"==== ==== ====")
for c in range(5, 1000):
    for b in range(4, c):
        for a in range(3, b):
            if a*a + b*b >= c*c:
                if a*a + b*b == c*c and gcd(a, b) == 1:
                    print(f"{a:4} {b:4} {c:4}")
                break
        	
