import io
import re

# Loops: read until empty
f = io.StringIO("x" * 2500)
while (chunk := f.read(1024)):
    print("read", len(chunk))

# Conditions: test a result, then use it
s = "release v42"
if (m := re.search(r"v(\d+)", s)):
    print(m.group(1))

# Comprehensions: compute once, filter + keep
def f(x):
    return x * 2 - 3

data = [0, 1, 2, 3, 4]
print([y for x in data if (y := f(x)) > 0])
