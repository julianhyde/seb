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

def add_fractions(a, b, c, d):
    (e, f) = (c * b + a * d, b * d)
    # print(f"e={e},f={f}")
    g = gcd(e, f)
    return (int(e / g), int(f / g))

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


def check(success):
    if not success:
        raise Exception('failed!')

check(9 == gcd(0, 9))
check(1 == gcd(0, 0))
check(1 == gcd(0, 1))
check(7 == gcd(0, 7))
check(2 == gcd(10, 8))
check(1 == gcd(1, 1))
check(4 == gcd(4, 4))
check(10 == gcd(30, 70))
check(1 == gcd(7, 4))
check(4 == gcd(8, 4))
check(1 == gcd(10, 21))

check((5, 4) == add_fractions(1, 2, 3, 4))
check((2, 1) == add_fractions(1, 1, 1, 1))
check((7, 12) == add_fractions(1, 3, 1, 4))
check((17, 20) == add_fractions(3, 4, 1, 10))
check((1, 1) == add_fractions(2, 3, 1, 3))
check((0, 1) == add_fractions(2, 3, -2, 3))
check((0, 1) == add_fractions(2, 3, -4, 6))


a = int(input("Top 1? "))
# print(a)
b = int(input("Bottom 1? "))
# print(b)
c = int(input("Top 2? "))
# print(c)
d = int(input("Bottom 2? "))
# print(d)
(e, f) = add_fractions(a, b, c, d)

print("")
print(f"{a:4}   {c:4}   {e:4}")
print(" ---- + ---- = ----")
print(f"{b:4}   {d:4}   {f:4}")
print("")
