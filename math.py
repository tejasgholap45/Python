import random
import math

def estimate_pi(n):
    #n = int(input("kiti sample draw karu?"))
    m = 0

    for _ in range(n):
        # Generate random point in the unit square
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)

        # Check if point is inside the unit circle
        distance = math.sqrt(x**2 + y**2)
        if distance <= 1:
            m = m + 1

    # The ratio of points inside the circle to total points should be π/4
    return 4 * m / n

# Example usage
n = 10000000 # More samples = more accurate estimate
pi_estimate = estimate_pi(n)
pi_estimate
