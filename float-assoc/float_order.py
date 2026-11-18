"""Adding the same floats in a different order gives a different answer."""
import random
import sys
from decimal import Decimal, getcontext

print("python", sys.version.split()[0])
print("(0.1 + 1e20) - 1e20 =", (0.1 + 1e20) - 1e20)
print("0.1 + (1e20 - 1e20) =", 0.1 + (1e20 - 1e20))

# Toy float: 3 significant decimal digits, rounded after every add
getcontext().prec = 3
a, b, c = Decimal(1230), Decimal("4.5"), Decimal("4.5")
print("toy 1230 + 4.5 =", a + b)
print("toy (1230 + 4.5) + 4.5 =", (a + b) + c)
print("toy 4.5 + 4.5 =", b + c)
print("toy 1230 + (4.5 + 4.5) =", a + (b + c))

# The article's shuffle experiment: 8 numbers that sum to exactly 0
vals = [1e-10, 1e-5, 1e-2, 1]
vals = vals + [-v for v in vals]
results = []
random.seed(42)
for _ in range(10000):
    random.shuffle(vals)
    total = 0.0
    for v in vals:  # plain left-to-right adds (sum() compensates on Python 3.12+)
        total += v
    results.append(total)
uniq = sorted(set(results))
print("unique sums:", len(uniq))
print("min", uniq[0], "max", uniq[-1])
print("exactly 0.0:", results.count(0.0), "of", len(results))
