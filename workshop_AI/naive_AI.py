# Import module random to generate pseudo-random numbers when player makes decision.
import random

# There are 2 possible types of individuals initially with equal chance of being generated.
    # The option probabilities should have a sum of 1.
type_options = ['Fixed', 'Random']
option_probabilities = [0.5, 0.5]

# The experiment consists of 3 players that each make 5 decisions.
number_of_rounds = 5 
number_of_players = 3

##########################################
########### Generate Players #############
##########################################

# This function selects one of the two possible types based on a
# generated number used to cycle between a 'Fixed' and 'Random' type.
def selectDecisionType(type_options, option_probabilities) :
    # Pair the type options with their respective probabilities in a zip object.
    options_and_probabilities = zip(type_options, option_probabilities)
    print('Type Options and Their Probabilities : ', list(options_and_probabilities))

    # Generate a number in between 0 and 1 using uniform distribution.
        # Since the option probabilities are between 0 and 1 as well,
        # this variable decides the player's decision type.
    type_decider = random.uniform(0,1)
    print('Generate Type Decider : ', type_decider)
    
    # Cycle through the options based on the generated type decider.
    cumulative_probability = 0.0
    for option, probability in zip(type_options, option_probabilities) :

        # Add the respective option probability to cumulative probability.
            # This momentarily alternates the current type option in the loop.
        cumulative_probability += probability

        print('Cumulative Probability : ', cumulative_probability)
        print('Current Option : ', option)

        # Break loop when the cumulative probability is greater than the type decider.
        if (type_decider < cumulative_probability) : break 
    return option

# Generate a single player with a decision type.
print('Player Decision Type : ', selectDecisionType(type_options, option_probabilities))

# This function generates the specified number of 
# players with one of the possible decision types.
def generatePlayers(type_options, option_probabilities, number_of_players) :
    # Initialize an empty list to store the players' decision types.
    players = []
    
    for player in range(number_of_players) :
        # Add a new player with a generated decision type.
        players.append(selectDecisionType(type_options, option_probabilities))
    return players

# Generate the specified number of players.
player_types = generatePlayers(type_options, option_probabilities, number_of_players)
print('Types of Players Generated : ', player_types) 

# This function counts the total number of 'Fixed' type players.
def countFixedPlayers(players) :
    total_fixed = 0
    for player in players :
        if (player == 'Fixed') :
            total_fixed += 1
    return total_fixed

# Count the number of 'Fixed' players generated.
number_fixed_players = countFixedPlayers(player_types)
print('Number of "Fixed" Type Players : ', number_fixed_players)

# This function counts the total number of 'Random' type players.
def countRandomPlayers(players) :
    total_random = 0
    for player in players :
        if (player == 'Random') :
            total_random += 1
    return total_random

# Count the number of 'Random' players generated.
number_random_players = countRandomPlayers(player_types)
print('Number of "Random" Type Players : ', number_random_players)


#####################################
########## Player Strategy ##########
#####################################

# This function provides the probability that each of the players
# with 'Fixed' decision types will follow one of the possible strategies.
def strategiesFixedPlayers(number_fixed_players) :
    # Initialize an empty list to store the probabilities for the 'Fixed' players.
    fixed_player_probabilities =  []
    for player in range(number_fixed_players) :
        strategy_probabilities = [('Fixed', 1), ('Random', 0)]
        fixed_player_probabilities.append(strategy_probabilities)
    return fixed_player_probabilities

# List the expectations of the strategies the 'Fixed' players will adhere to.
expectations_fixed_players = strategiesFixedPlayers(number_fixed_players)
print('Expectations of "Fixed" Player Strategies : ', expectations_fixed_players)

# This function provides the probability that each of the players
# with 'Random' decision types will follow one of the possible strategies.
def strategiesRandomPlayers(number_random_players) :
    # Initialize an empty list to store the probabilities for the 'Random' players.
    random_player_probabilities =  []
    for player in range(number_random_players) :
        strategy_probabilities = [('Fixed', 0), ('Random', 1)]
        random_player_probabilities.append(strategy_probabilities)
    return random_player_probabilities

# List the expectations of the strategies the 'Random' players will adhere to.
expectations_random_players = strategiesRandomPlayers(number_random_players)
print('Expectations of "Random" Player Strategies : ', expectations_random_players)

################################
########## Plays Made ##########
################################ 

# This function simulates a round in the decision making process.
def selectPlayType(expectations_strategies) :
    # Initialize an empty list to store the plays made.
    plays_made = []

    # Generate a number for each player in between 0 and 1 using uniform distribution.
        # Since the strategy probabilities are between 0 and 1 as well,
        # this variable decides which strategy will be adhered to by the player.
    strategy_decider = [random.uniform(0,1) for player in range(len(expectations_strategies))]
    print('Generate Strategy Deciders : ', strategy_decider)

    # Cycle through the strategies based on the generated strategy decider.
    cumulative_probability = 0.0
    for index in range(len(expectations_strategies)) :
        for strategy_and_probability in expectations_strategies[index] :
            if (index == 0) :
                cumulative_probability += strategy_and_probability[1]

                print('Cumulative Strategy : ', cumulative_probability)
                print('Current Strategy : ', strategy_and_probability[0])

                # Break loop when the cumulative_probability is greater than the strategy decider.
                if (strategy_decider[index] < cumulative_probability) : break    
            else :
                cumulative_probability = 0.0
                cumulative_probability += strategy_and_probability[1]

                print('Cumulative Strategy : ', cumulative_probability)
                print('Current Strategy : ', strategy_and_probability[0])

                # Break loop when the cumulative_probability is greater than the strategy decider.
                if (strategy_decider[index] < cumulative_probability) : break    
        plays_made.append(strategy_and_probability[0])
    return plays_made

# Initialize an empty list to store the expectations of the players' strategies.
expectations_strategies = []

# Extend the expectations list for all players to include the 
# separate expectations for the 'Fixed' and 'Random' players.
expectations_strategies.extend(expectations_fixed_players)
expectations_strategies.extend(expectations_random_players)

# List the expectations of the strategies both the 'Fixed' and 'Random' players will adhere to.
print('Expectations of Player Strategies : ', expectations_strategies)

# List the plays made by all the players based on the expectations of their strategies.
plays_made = selectPlayType(expectations_strategies)
print ('Plays Made By Players : ', plays_made)

#################################
###### Changing Strategies ######
#################################

# This function generates the probability of a 'Fixed' player making strategies.
def profit_fixed_player(fixed_players) :
    decision_probabilities = []

    random_income = [random.uniform(50, 150) for player in range(len(fixed_players))]
    profit_earned = [(100 - earning) for earning in random_income]

    probability_random = [(earning / (100 + earning)) for earning in random_income]
    probability_fixed = [(1 - i) for i in probability_random]  


    for i in range(len(fixed_players)) :
        if (profit_earned[i] > 0 and fixed_players[i][1] == 1) :
            decision_probabilities.append([('Fixed', 1), ('Random', 0)])
        else :
            decision_probabilities.append([('Fixed', probability_fixed[i]), ('Random', probability_random[i])])
    return decision_probabilities

# This function generates the probability of a 'Random' player making strategies.
def profit_random_player(random_players) :
    decision_probabilities = []

    random_income = [random.uniform(50, 150) for player in range(len(random_players))]
    profit_earned = [(earning - 100) for earning in random_income]

    probability_fixed = [(100 / (100 + earning)) for earning in random_income]  
    probability_random = [(1 - i) for i in probability_fixed]

    for i in range(len(random_players)) :
        if (profit_earned[i] > 0 and random_players[i][1] == 1) :
            decision_probabilities.append([('Fixed', 0), ('Random', 1)])
        else :
            decision_probabilities.append([('Fixed', probability_fixed[i]), ('Random', probability_random[i])])
    return decision_probabilities

def count_fixed_and_random_plays(players) :
    player_types = []
    plays_made = selectPlayType(players)

    for i in range(len(plays_made)) :
        if (plays_made[i][0] == 'Fixed') :
            player_types.append(1)
        elif (plays_made[i][0] == 'Random') :
            player_types.append(0)
    return plays_made, sum(player_types)