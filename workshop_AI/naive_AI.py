
# Import module random to generate pseudo-random numbers when player makes decision.
import random

# Generate 2 types of individuals initially with equal chance.
decision_options = ['Fixed', 'Random']
decision_probabilities = [0.5, 0.5]

number_of_rounds = 5
number_of_players = 3

def selection(decision_options, decision_probabilities) :
    # Generate a number in between 0 and 1.
    probability = random.uniform(0,1)
    cumulative_probability = 0.0

    for item, item_probability in zip (decision_options, decision_probabilities) :
        # Add each item probability to cumulative probability
        cumulative_probability += item_probability

        if (probability < cumulative_probability) : break 
    return item

def producing_types(decision_options, decision_probabilities, number_of_players) :
    copy = []
    
    while (len(copy) < number_of_players) :
        copy.append(selection(decision_options, decision_probabilities))
    return copy 