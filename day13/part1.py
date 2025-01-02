from sympy import symbols, Eq, solve
import re

with open('input2.txt') as f:
    lines = f.read().splitlines()

pat = re.compile(r'\D+')
tokens = 0

for i in range(0, len(lines), 4):
    tmp = []
    for j in range(3):
        tmp.append([int(re.sub(pat, '', line)) for line in lines[i + j].split(",")])

    a, b = symbols('a, b')
    eq1 = Eq(a * tmp[0][0] + b * tmp[1][0], tmp[2][0])
    eq2 = Eq(a * tmp[0][1] + b * tmp[1][1], tmp[2][1])
    sol = solve((eq1, eq2), (a, b))

    if all(float(val).is_integer() and 0 <= val <= 100 for val in sol.values()):
        tokens += 3 * sol[a] + sol[b]

print(tokens)
