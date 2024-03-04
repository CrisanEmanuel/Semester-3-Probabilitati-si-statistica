import random


def bile2(N=1000):
    # Define the balls in the urn
    urn = [1] * 10 + [2] * 3 + [3] * 5  # 1 for red, 2 for white, 3 for green

    # Initialize counts for events A, B, C for both with and without replacement
    A_without, B_without, C_without = 0, 0, 0
    A_with, B_with, C_with = 0, 0, 0

    # Simulation without replacement
    for _ in range(N):
        drawn_balls = random.sample(urn, 3)

        if drawn_balls == [2, 1, 3]:
            A_without += 1

        count = [drawn_balls.count(i) for i in range(1, 4)]

        if count[2] == 0:
            B_without += 1
        if count[2] == 1:
            C_without += 1

    # Simulation with replacement
    for _ in range(N):
        drawn_balls = random.choices(urn, k=3)

        if drawn_balls == [2, 1, 3]:
            A_with += 1

        count = [drawn_balls.count(i) for i in range(1, 4)]

        if count[2] == 0:
            B_with += 1
        if count[2] == 1:
            C_with += 1

    # Calculate probabilities
    prob_A_without = A_without / N
    prob_B_without = B_without / N
    prob_C_without = C_without / N

    prob_A_with = A_with / N
    prob_B_with = B_with / N
    prob_C_with = C_with / N

    return prob_A_without, prob_B_without, prob_C_without, prob_A_with, prob_B_with, prob_C_with
