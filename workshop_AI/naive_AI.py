# Import module random to generate pseudo-random numbers when player makes decision.
import random
# Import data visualization library.
import matplotlib.pyplot as plt 

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

    ## The following line is commented out -> used for debugging custom function.
    ## print('Type Options and Their Probabilities : ', list(options_and_probabilities))

    # Generate a number in between 0 and 1 using uniform distribution.
        # Since the option probabilities are between 0 and 1 as well,
        # this variable decides the player's decision type.
    type_decider = random.uniform(0, 1)

    ## The following line is commented out -> used for debugging custom function.
    ## print('Generate Type Decider : ', type_decider)
    
    # Cycle through the options based on the generated type decider.
    cumulative_probability = 0.0
    for option, probability in zip(type_options, option_probabilities) :

        # Add the respective option probability to cumulative probability.
            # This momentarily alternates the current type option in the loop.
        cumulative_probability += probability

        ## The following lines are commented out -> used for debugging custom function.
        ## print('Cumulative Probability : ', cumulative_probability)
        ## print('Current Option : ', option)

        # Break loop when the cumulative probability is greater than the type decider.
        if (type_decider < cumulative_probability) : break 
    return option

## The following line is commented out -> used for debugging custom function.
## print('Player Decision Type : ', selectDecisionType(type_options, option_probabilities))

# This function generates the specified number of players with one of the possible decision types.
def generatePlayers(type_options, option_probabilities, number_of_players) :
    # Initialize an empty list to store the players' decision types.
    players = []
    
    for player in range(number_of_players) :
        # Add a new player with a generated decision type.
        players.append(selectDecisionType(type_options, option_probabilities))
    return players

## The following lines are commented out -> used for debugging custom function.
## player_types = generatePlayers(type_options, option_probabilities, number_of_players)
## print('Types of Players Generated : ', player_types) 

# This function counts the total number of 'Fixed' type players.
def countFixedPlayers(players) :
    total_fixed = 0
    for player in players :
        if (player == 'Fixed') :
            total_fixed += 1
    return total_fixed

## The following lines are commented out -> used for debugging custom function.
## number_fixed_players = countFixedPlayers(player_types)
## print('Number of "Fixed" Type Players : ', number_fixed_players)

# This function counts the total number of 'Random' type players.
def countRandomPlayers(players) :
    total_random = 0
    for player in players :
        if (player == 'Random') :
            total_random += 1
    return total_random

## The following lines are commented out -> used for debugging custom function.
## number_random_players = countRandomPlayers(player_types)
## print('Number of "Random" Type Players : ', number_random_players)

#####################################
########## Player Strategy ##########
#####################################

# This function provides the probability that each of the players
# with 'Fixed' decision types will follow one of the possible strategies.
def strategiesFixedPlayers(number_fixed_players) :
    # Initialize an empty list to store the probabilities for the 'Fixed' players.
    fixed_player_probabilities =  []
    for player in range(number_fixed_players) :
        strategy_probabilities = [ ('Fixed', 1), ('Random', 0) ]
        fixed_player_probabilities.append(strategy_probabilities)
    return fixed_player_probabilities

## The following lines are commented out -> used for debugging custom function.
## expectations_fixed_players = strategiesFixedPlayers(number_fixed_players)
## print('Expectations of "Fixed" Player Strategies : ', expectations_fixed_players)

# This function provides the probability that each of the players
# with 'Random' decision types will follow one of the possible strategies.
def strategiesRandomPlayers(number_random_players) :
    # Initialize an empty list to store the probabilities for the 'Random' players.
    random_player_probabilities =  []
    for player in range(number_random_players) :
        strategy_probabilities = [ ('Fixed', 0), ('Random', 1) ]
        random_player_probabilities.append(strategy_probabilities)
    return random_player_probabilities

## The following lines are commented out -> used for debugging custom function.
## expectations_random_players = strategiesRandomPlayers(number_random_players)
## print('Expectations of "Random" Player Strategies : ', expectations_random_players)

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
    strategy_deciders = [ random.uniform(0, 1) for player in range(len(expectations_strategies)) ]
    print('Generate Strategy Deciders : ', strategy_deciders)

    # Cycle through the strategies based on the generated strategy decider.
    cumulative_probability = 0.0
    for index in range(len(expectations_strategies)) :

        print('Current Decider : ', strategy_deciders[index])

        for strategy_and_probability in expectations_strategies[index] :
            if (index == 0) :
                cumulative_probability += strategy_and_probability[1]

                print('Cumulative Strategy : ', cumulative_probability)
                print('Current Strategy : ', strategy_and_probability[0])

                # Break loop when the cumulative_probability is greater than the strategy decider.
                if (strategy_deciders[index] < cumulative_probability) : break    
            else :
                cumulative_probability = 0.0
                cumulative_probability += strategy_and_probability[1]

                print('Cumulative Strategy : ', cumulative_probability)
                print('Current Strategy : ', strategy_and_probability[0])

                # Break loop when the cumulative_probability is greater than the strategy decider.
                if (strategy_deciders[index] < cumulative_probability) : break    
        plays_made.append(strategy_and_probability[0])
    return plays_made

## The following lines are commented out -> used for debugging custom function.
## expectations_strategies = []
## expectations_strategies.extend(expectations_fixed_players)
## expectations_strategies.extend(expectations_random_players)
## print('Expectations of Player Strategies : ', expectations_strategies)
## plays_made = selectPlayType(expectations_strategies)
## print ('Plays Made By Players : ', plays_made)

#################################
###### Changing Strategies ######
#################################

# This function generates the probability of a 'Fixed' player following the possible strategies.
def profit_fixed_player(fixed_players) :
    decision_probabilities = []

    random_income = [ random.uniform(50, 150) for player in range(len(fixed_players)) ]
    profit_earned = [ (100 - earning) for earning in random_income ]

    ## The following lines are commented out -> used for debugging custom function.
    print('"Fixed" Players : ', fixed_players)
    print('Generated Income for "Fixed" Players : ', random_income)
    print('Profit from "Fixed" Strategy : ', profit_earned)

    probability_random = []
    probability_fixed = []
    # These probability variables have the original expectations of (Fixed : Random) 
    # as (1 : 0), unless there is a loss from following the 'Fixed' strategy.
    for earning in range(len(random_income)) :
        if (profit_earned[earning] > 0) :
            probability_random.append(0)
            probability_fixed.append(1)
        else :
            probability_random.append(earning / (100 + earning))
            probability_fixed.append(1 - probability_random[earning])

    for player in range(len(fixed_players)) :
        decision_probabilities.append([('Fixed', probability_fixed[player]), ('Random', probability_random[player])])
    return decision_probabilities

# This function generates the probability of a 'Random' player following the possible strategies.
def profit_random_player(random_players) :
    decision_probabilities = []

    random_income = [ random.uniform(50, 150) for player in range(len(random_players)) ]
    profit_earned = [ (earning - 100) for earning in random_income ]

    ## The following lines are commented out -> used for debugging custom function.
    print('"Random" Players : ', random_players)
    print('Generated Income for "Random" Players : ', random_income)
    print('Profit from "Random" Strategy : ', profit_earned)

    probability_fixed = []
    probability_random = []
    # These probability variables have the original expectations of (Fixed : Random) 
    # as (0 : 1), unless there is a loss from following the 'Random' strategy.
    for earning in range(len(random_income)) :
        if (profit_earned[earning] > 0) :
            probability_fixed.append(0)
            probability_random.append(1)
        else :
            probability_fixed.append(100 / (100 + earning))
            probability_random.append(1 - probability_fixed[earning])

    for player in range(len(random_players)) :
        decision_probabilities.append([('Fixed', probability_fixed[player]), ('Random', probability_random[player])])
    return decision_probabilities

def count_fixed_and_random_plays(players) :
    number_of_fixed_plays = 0
    plays_made = selectPlayType(players)

    ## The following lines are commented out -> used for debugging custom function.
    print("Plays Simulated : ", plays_made)

    for play in range(len(plays_made)) :
        if (plays_made[play] == 'Fixed') :
            number_of_fixed_plays += 1
    return plays_made, number_of_fixed_plays

###########################
###### Main Function ######
###########################

def simulation_questionnaire (type_options, option_probabilities, number_of_players, number_of_rounds) :
    # Generate the specified number of players.
    player_types = generatePlayers(type_options, option_probabilities, number_of_players)
    print('Types of Players Generated : ', player_types)     

    # Count the number of 'Fixed' players generated.
    number_fixed_players = countFixedPlayers(player_types)
    print('Number of "Fixed" Type Players : ', number_fixed_players)  

    # Count the number of 'Random' players generated.
    number_random_players = countRandomPlayers(player_types)
    print('Number of "Random" Type Players : ', number_random_players)

    # List the expectations of the strategies the 'Fixed' players will adhere to.
    expectations_fixed_players = strategiesFixedPlayers(number_fixed_players)
    print('Expectations of "Fixed" Player Strategies : ', expectations_fixed_players)
    
    # List the expectations of the strategies the 'Random' players will adhere to.
    expectations_random_players = strategiesRandomPlayers(number_random_players)
    print('Expectations of "Random" Player Strategies : ', expectations_random_players)

    # The following empty lists will include the results
    # from each simulated round of the questionnaire. 
    results_number_of_fixed_plays = []
    results_number_of_fixed_plays_by_fixed_players = []
    results_number_of_fixed_plays_by_random_players = []
    results_updated_expectations_fixed_players = []
    results_updated_expectations_random_players = []

    for round in range(number_of_rounds) :
        print('Round # : ', round + 1)

        # Update the expectations of the strategies the players will adhere to based on the previous results.
        if (round > 0) :
            expectations_fixed_players = results_updated_expectations_fixed_players[len(results_updated_expectations_fixed_players) - 1]
            expectations_random_players = results_updated_expectations_random_players[len(results_updated_expectations_random_players) - 1]

        # Store the plays made by the different types of players.
        plays_made_fixed_players, number_of_fixed_plays_by_fixed_players = count_fixed_and_random_plays(expectations_fixed_players)
        plays_made_random_players, number_of_fixed_plays_by_random_players = count_fixed_and_random_plays(expectations_random_players)

        print('Plays Made by "Fixed" Players : ', plays_made_fixed_players)
        print('Number of "Fixed" Plays Made by "Fixed" Players : ', number_of_fixed_plays_by_fixed_players)

        print('Plays Made by "Random" Players : ', plays_made_random_players)
        print('Number of "Fixed" Plays Made by "Random" Players : ', number_of_fixed_plays_by_random_players)

        # Calculate the total number of 'Fixed' plays in the round.
        number_of_fixed_plays = number_of_fixed_plays_by_fixed_players + number_of_fixed_plays_by_random_players

        print('Total Number of "Fixed" Plays : ', number_of_fixed_plays)
        
        # Based on the results from this round, update the expectations for the different types of players.
        updated_expectations_fixed_players = profit_fixed_player(plays_made_fixed_players)
        updated_expectations_random_players = profit_random_player(plays_made_random_players)

        print('Updated "Fixed" Player Expectations : ',  updated_expectations_fixed_players)
        print('Updated "Random" Player Expectations : ',  updated_expectations_random_players)

        # Update the lists containing the results from the particular round of the simulation.
        results_number_of_fixed_plays.append(number_of_fixed_plays)
        results_number_of_fixed_plays_by_fixed_players.append(number_of_fixed_plays_by_fixed_players)
        results_number_of_fixed_plays_by_random_players.append(number_of_fixed_plays_by_random_players)
        results_updated_expectations_fixed_players.append(updated_expectations_fixed_players)
        results_updated_expectations_random_players.append(updated_expectations_random_players)

    return results_number_of_fixed_plays, results_number_of_fixed_plays_by_fixed_players, results_number_of_fixed_plays_by_random_players

results_number_of_fixed_plays, results_number_of_fixed_plays_by_fixed_players, results_number_of_fixed_plays_by_random_players = simulation_questionnaire (type_options, option_probabilities, number_of_players, number_of_rounds)

print()
print ("******SIMULATION RESULTS******")
print()

print('Number of "Fixed" Plays in Each Round : ', results_number_of_fixed_plays)
print('Number of "Fixed" Plays by "Fixed" Players in Each Round : ', results_number_of_fixed_plays_by_fixed_players)
print('Number of "Fixed" Plays by "Random" Players in Each Round : ', results_number_of_fixed_plays_by_random_players)

###########################
###### Graph Results ######
###########################

rounds = []
for round in range(number_of_rounds) :
    rounds.append(round + 1)

print("Rounds : ", rounds)

plt.plot(rounds, results_number_of_fixed_plays, label = 'Number of "Fixed" Decisions in Simulated Questionnaire')
plt.xlabel('Round #')
plt.ylabel('Number of "Fixed" Plays')

plt.plot(rounds, results_number_of_fixed_plays_by_fixed_players, label = 'Number of "Fixed" Decisions by "Fixed" Players in Simulated Questionnaire')
plt.xlabel('Round #')
plt.ylabel('Number of "Fixed" Plays by "Fixed" Players')

plt.plot(rounds, results_number_of_fixed_plays_by_random_players, label = 'Number of "Fixed" Decisions by "Random" Players in Simulated Questionnaire')
plt.xlabel('Round #')
plt.ylabel('Number of "Fixed" Plays by "Random" Players')

plt.title('Simulated Questionnaire Results')
plt.legend()
plt.show()
