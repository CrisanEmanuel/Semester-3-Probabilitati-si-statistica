import random


def bile3(N=1000):
    # Define the balls in the urn
    urn = [1] * 7 + [2] * 6 + [3] * 5  # 1 for white, 2 for green, 3 for red

    # Initialize counts for events A, B, C, D
    A, B, C, D = 0, 0, 0, 0

    # Simulation without replacement
    for _ in range(N):
        drawn_balls = random.sample(urn, 3)
        count = [drawn_balls.count(i) for i in range(1, 4)]

        # Check conditions for events A, B, C
        if count[1] == 3:  # All green
            A += 1
        if count[0] == 1 and count[1] == 1 and count[2] == 1:  # One of each color
            B += 1
        if count[0] <= 2:  # At most two white
            C += 1

        # Check condition for event D (at least one green given first is white)
        if drawn_balls[0] == 1 and (2 in drawn_balls[1:]):
            D += 1

    # Calculate probabilities
    prob_A = A / N
    prob_B = B / N
    prob_C = C / N
    prob_D = D / N

    return prob_A, prob_B, prob_C, prob_D
