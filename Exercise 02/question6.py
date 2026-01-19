import random
#3-digit code (0-9)
a = random.randint(0 ,9)
b = random.randint(0, 9)
c = random.randint(0, 9)

#4-digit code (1-6)
d = random.randint(1 ,6)
e = random.randint(1, 6)
f = random.randint(1, 6)
g = random.randint(1, 6)

print(f"3-Digit Combination Lock Code: {a}{b}{c}")
print(f"4-Digit Combination Lock Code: {d}{e}{f}{g}")

