"""
Define a simple Markov Model with three weather states: Sunny, Cloudy, and Rainy.
Create a transition matrix for the weather states, specifying the probabilities of
transitioning from one state to another (e.g., from Sunny to Cloudy, or from Cloudy to
Rainy). Simulate the weather for the next 10 days, starting with a Sunny day, using the
Markov Model. Calculate the probability of having at least 3 rainy days over the 10-day
period.
"""

import numpy as np

states = ["Sunny", "Rainy", "Cloudy"]

transition_matrix = np.array([
    [ 0.6, 0.3, 0.1 ],
    [ 0.3, 0.4, 0.3 ],
    [ 0.2, 0.3, 0.5 ]
])

def simulate_markhov_process(num_of_steps, intial_state):
    current_state = intial_state
    state_sequence = [current_state]

    for i in range(num_of_steps):
        if current_state == "Sunny":
            next_state = np.random.choice(states, p=transition_matrix[0])
        elif current_state == "Rainy":
            next_state = np.random.choice(states, p=transition_matrix[1])
        else:
            next_state = np.random.choice(states, p=transition_matrix[2])
    
        state_sequence.append(next_state)
        current_state = next_state
    
    return state_sequence


num_of_sims = 10000
num_of_steps = 10
intial_state = "Sunny"

num_of_rainydays_greaterthan_three = 0

for i in range(num_of_sims):
    seq = simulate_markhov_process(num_of_steps, intial_state)
    rainy_days = seq.count("Rainy")

    if rainy_days >= 3:
        num_of_rainydays_greaterthan_three+=1       

print("probability of having at least 3 rainy days over the 10-day period:", num_of_rainydays_greaterthan_three/num_of_sims)
#print("->".join(state_seq))

