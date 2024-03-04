import random


def bile1(nr_sim=1000):
    # Define the balls in the urn
    balls = ['g'] * 4 + ['n'] * 5 + ['w'] * 2 + ['a'] * 3

    # Initialize counts for events A, B, C for both with and without replacement
    A_with, B_with, C_with = 0, 0, 0
    A_without, B_without, C_without = 0, 0, 0

    # Simulation with replacement
    for _ in range(nr_sim):
        # Sample 4 balls with replacement
        drawn_balls = random.choices(balls, k=4)
        count = {'g': drawn_balls.count('g'), 'n': drawn_balls.count('n'),
                 'w': drawn_balls.count('w'), 'a': drawn_balls.count('a')}

        # Check conditions for events A, B, C
        if count['w'] <= 1:
            A_with += 1
        if count['g'] == 0:
            B_with += 1
        if count['n'] >= 2:
            C_with += 1

    # Simulation without replacement
    for _ in range(nr_sim):
        # Sample 4 balls without replacement
        drawn_balls = random.sample(balls, 4)
        count = {'g': drawn_balls.count('g'), 'n': drawn_balls.count('n'),
                 'w': drawn_balls.count('w'), 'a': drawn_balls.count('a')}

        # Check conditions for events A, B, C
        if count['w'] <= 1:
            A_without += 1
        if count['g'] == 0:
            B_without += 1
        if count['n'] >= 2:
            C_without += 1

    # Calculate probabilities
    prob_A_with = A_with / nr_sim
    prob_B_with = B_with / nr_sim
    prob_C_with = C_with / nr_sim

    prob_A_without = A_without / nr_sim
    prob_B_without = B_without / nr_sim
    prob_C_without = C_without / nr_sim

    return prob_A_with, prob_B_with, prob_C_with, prob_A_without, prob_B_without, prob_C_without
