# A toy generator for learning only. Use the secrets module for anything security-related.
M, A, C = 16, 5, 3
state = 7  # the seed

def next_state():
    global state
    state = (A * state + C) % M
    return state

def roll():  # fair die, 1..6
    while True:
        x = next_state()
        if x < 12:
            return x % 6 + 1

counts = {face: 0 for face in range(1, 7)}
for _ in range(6000):
    counts[roll()] += 1
print(counts)
