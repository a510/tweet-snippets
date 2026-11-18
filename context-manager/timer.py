from contextlib import contextmanager
import time

@contextmanager
def timer(name):
    print("start", name)
    t0 = time.time()
    try:
        yield
    finally:
        took = round(time.time() - t0, 1)
        print(name, "took", took, "s")

with timer("search"):
    time.sleep(0.2)
    print("found 3 results")

# This block raises on purpose: the finally still prints, then the error carries on.
with timer("fetch"):
    time.sleep(0.1)
    raise ValueError("network down")
