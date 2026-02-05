import random

N = int(input("How many random points to generate? "))

inside = 0

for i in range(N):
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)

    if x*x + y*y < 1:
        inside += 1

pi_approx = 4 * inside / N

print("Approximation of pi:", pi_approx)