#############################################################
########## Import Libraries and Define Assumptions ##########
#############################################################

# Import Module Random to Generate Decision Types and Strategies.
import random
# Import Library for Data Visualization of Simulation Results and App Data.
import matplotlib.pyplot as plt 
# Import Library for Working with Numerical Arrays.
import numpy as np
# Deal with Tabular Data using Pandas Library.
import pandas as pd

# There are 2 possible Decision Types of players with equal chance of being generated.
    # The option probabilities should have a sum of 1.
type_options = ['Fixed', 'Random']
option_probabilities = [0.5, 0.5]

# The experiment consists of 3 players that each make 5 decisions.
number_of_rounds = 5 
number_of_players = 3

###################################
######### Acquire App Data ########
###################################

# Import the user data from the deployed app.
app_dataframe = pd.read_excel('../workshop_data/Relevant_Results.xlsx')
print('User Data Collected: \n', app_dataframe)

# Organize user data from Excel Spreadsheet into individual series.
user_details_series = app_dataframe['Player Details']
user_app_choice_series = app_dataframe['App Choice']
user_round_1_series = app_dataframe['Round 1']
user_round_1_series = app_dataframe['Round 2']
user_round_1_series = app_dataframe['Round 3']
user_round_1_series = app_dataframe['Round 4']
user_round_1_series = app_dataframe['Round 5']

# Initialize empty lists to input relevant data for graphics at end of script.
number_of_fixed_strategies_all_users = []
number_of_fixed_strategies_quadratic = []
number_of_fixed_strategies_investment = []

# Learn about the user data in terms of their 'Fixed' Strategies and app choice.
for round in range(number_of_rounds) :
    fixed_strategies_all_users_in_round = 0
    fixed_strategies_quadratic_in_round = 0
    fixed_strategies_investment_in_round = 0
    for user in range(len(app_dataframe.index)) :
        
        # Note the numerical values corresponding to the app choice and 'Fixed' or 'Random' Strategies 
        # correspond to what is defined in the app models.py script. These may differ from the numerical 
        # values used for our calculations in the AI simulation later on in this script.

        # Case in which user decides to earn a fixed amount (constant defined in models.py).
        if (app_dataframe['Round ' + str(round + 1)][user] == 0) :
                fixed_strategies_all_users_in_round += 1
                # Case in which user had decided to test quadratic app (constant defined in models.py).
                if (app_dataframe['App Choice'][user] == 0) :
                    fixed_strategies_quadratic_in_round += 1
                # Case in which user had decided to test investment app (constant defined in models.py).
                elif (app_dataframe['App Choice'][user] == 1) :
                    fixed_strategies_investment_in_round += 1
    # Append data involving 'Fixed' Strategies from each round to the list for the App Data. 
    number_of_fixed_strategies_all_users.append(fixed_strategies_all_users_in_round)
    number_of_fixed_strategies_quadratic.append(fixed_strategies_quadratic_in_round)
    number_of_fixed_strategies_investment.append(fixed_strategies_investment_in_round)

print("\n******APP DATA******\n")

print('"Fixed" Strategies Followed By All Users : ', number_of_fixed_strategies_all_users)
print('"Fixed" Strategies Followed By Quadratic App Users : ', number_of_fixed_strategies_quadratic)
print('"Fixed" Strategies Followed By Investment App Users : ', number_of_fixed_strategies_investment)

#################################################
########### Generate Decision Types #############
#################################################

# This function selects one of the two possible Decision Types based on a
# generated number used to cycle between a 'Fixed' and 'Random' type.
def selectDecisionType(type_options, option_probabilities) :
    
    ## The following line are commented out -> used for debugging custom function.
    ## options_and_probabilities = zip(type_options, option_probabilities)
    ## print('Decision Type Options and Their Probabilities : ', list(options_and_probabilities))

    # Generate a number in between 0 and 1 using uniform distribution.
        # Since the option probabilities are between 0 and 1 as well,
        # this variable decides the player's Decision Type.
    type_decider = random.uniform(0, 1)

    ## The following line is commented out -> used for debugging custom function.
    ## print('Generate Decision Type Decider : ', type_decider)
    
    # Cycle through the options based on the generated Decision Type decider.
    cumulative_probability = 0.0
    for option, probability in zip(type_options, option_probabilities) :

        # Add the respective option probability to cumulative probability.
            # This momentarily alternates the current option in the loop.
        cumulative_probability += probability

        ## The following lines are commented out -> used for debugging custom function.
        ## print('Cumulative Probability : ', cumulative_probability)
        ## print('Current Option : ', option)

        # Break loop when the cumulative probability is greater than the type decider.
        if (type_decider < cumulative_probability) : break 
    return option

## The following line is commented out -> used for debugging custom function.
## print('Player Decision Type : ', selectDecisionType(type_options, option_probabilities))

# This function generates the specified number of players with either of the possible Decision Types.
def generatePlayers(type_options, option_probabilities, number_of_players) :
    # Initialize an empty list to store the players' decision types.
    players = []
    
    for player in range(number_of_players) :
        # Add a new player with a generated decision type.
        players.append(selectDecisionType(type_options, option_probabilities))
    return players

## The following lines are commented out -> used for debugging custom function.
## decision_types = generatePlayers(type_options, option_probabilities, number_of_players)
## print('Decision Types of Players Generated : ', decision_types) 

# This function counts the total number of 'Fixed' Decision Type players.
def countFixedPlayers(players) :
    total_fixed = 0
    for player in players :
        if (player == 'Fixed') :
            total_fixed += 1
    return total_fixed

## The following lines are commented out -> used for debugging custom function.
## number_fixed_players = countFixedPlayers(decision_types)
## print('Number of "Fixed" Decision Type Players : ', number_fixed_players)

# This function counts the total number of 'Random' Decision Type players.
def countRandomPlayers(players) :
    total_random = 0
    for player in players :
        if (player == 'Random') :
            total_random += 1
    return total_random

## The following lines are commented out -> used for debugging custom function.
## number_random_players = countRandomPlayers(decision_types)
## print('Number of "Random" Decision Type Players : ', number_random_players)

########################################
########## Default Strategies ##########
########################################

# This function provides the probability that each of the players
# with 'Fixed' Decision Types will follow one of the possible Strategies.
def strategiesFixedPlayers(number_fixed_players) :
    # Initialize an empty list to store the Strategy probabilities for the 'Fixed' Decision Type players.
    fixed_player_probabilities =  []
    for player in range(number_fixed_players) :
        strategy_probabilities = [ ('Fixed', 1), ('Random', 0) ]
        fixed_player_probabilities.append(strategy_probabilities)
    return fixed_player_probabilities

## The following lines are commented out -> used for debugging custom function.
## strategy_expectations_fixed_players = strategiesFixedPlayers(number_fixed_players)
## print('Strategy Expectations of "Fixed" Decision Type Players : ', strategy_expectations_fixed_players)

# This function provides the probability that each of the players
# with 'Random' Decision Types will follow one of the possible Strategies.
def strategiesRandomPlayers(number_random_players) :
    # Initialize an empty list to store the Strategy probabilities for the 'Random' Decision Type players.
    random_player_probabilities =  []
    for player in range(number_random_players) :
        strategy_probabilities = [ ('Fixed', 0), ('Random', 1) ]
        random_player_probabilities.append(strategy_probabilities)
    return random_player_probabilities

## The following lines are commented out -> used for debugging custom function.
## strategy_expectations_random_players = strategiesRandomPlayers(number_random_players)
## print('Strategy Expectations of "Random" Decision Type Players : ', strategy_expectations_random_players)

#########################################
########## Strategies Followed ##########
######################################### 

# This function simulates a round in the questionnaire.
def strategiesFollowed(expectations_strategies) :
    # Initialize an empty list to store the Strategies adhered to by the players.
    strategies_followed = []

    # Generate a number for each player in between 0 and 1 using uniform distribution.
        # Since the Strategy probabilities are between 0 and 1 as well,
        # this variable decides which Strategy will be adhered to by the player.
    strategy_deciders = [ random.uniform(0, 1) for player in range(len(expectations_strategies)) ]

    ## The following line is commented out -> used for debugging custom function.
    ## print('Generate Strategy Deciders : ', strategy_deciders)

    # Cycle through the Strategies based on the generated Strategy deciders.
    cumulative_probability = 0.0
    for index in range(len(expectations_strategies)) :

        ## The following line is commented out -> used for debugging custom function.
        ## print('Current Strategy Decider : ', strategy_deciders[index])

        for strategy_and_probability in expectations_strategies[index] :
            if (index != 0) :
                cumulative_probability = 0.0
            cumulative_probability += strategy_and_probability[1]

            ## The following lines are commented out -> used for debugging custom function.
            ## print('Cumulative Probability : ', cumulative_probability)
            ## print('Current Strategy : ', strategy_and_probability[0])

            # Break loop when the cumulative_probability is greater than the Strategy decider.
            if (strategy_deciders[index] < cumulative_probability) : break      
        strategies_followed.append(strategy_and_probability[0])
    return strategies_followed

## The following lines are commented out -> used for debugging custom function.
## expectations_strategies = []
## expectations_strategies.extend(strategy_expectations_fixed_players)
## expectations_strategies.extend(strategy_expectations_random_players)
## print('Expectations of Player Strategies : ', expectations_strategies)
## strategies_followed = strategiesFollowed(expectations_strategies)
## print ('Strategies Followed by Players : ', strategies_followed)

##################################
###### Switching Strategies ######
##################################

# This function generates the probability of a 'Fixed' Decision Type player following the possible Strategies.
def profitFixedPlayer(fixed_players) :
    strategy_probabilities = []

    random_income = [ random.uniform(50, 150) for player in range(len(fixed_players)) ]
    profit_earned = [ (100 - earning) for earning in random_income ]

    ## The following lines are commented out -> used for debugging custom function.
    ## print('"Fixed" Decision Type Players : ', fixed_players)
    ## print('Generated Income for "Fixed" Decision Type Players : ', random_income)
    ## print('Profit from "Fixed" Strategy : ', profit_earned)

    random_probability = []
    fixed_probability = []
    # These probability variables have the original expectations of (Fixed : Random) 
    # as (1 : 0), unless there is a Loss from following the 'Fixed' Strategy.
    for earning in range(len(random_income)) :
        if (profit_earned[earning] > 0) :
            random_probability.append(0)
            fixed_probability.append(1)
        else :
            random_probability.append(earning / (100 + earning))
            fixed_probability.append(1 - random_probability[earning])

    for player in range(len(fixed_players)) :
        strategy_probabilities.append([('Fixed', fixed_probability[player]), ('Random', random_probability[player])])
    return strategy_probabilities

# This function generates the probability of a 'Random' Decision Type player following the possible Strategies.
def profitRandomPlayer(random_players) :
    strategy_probabilities = []

    random_income = [ random.uniform(50, 150) for player in range(len(random_players)) ]
    profit_earned = [ (earning - 100) for earning in random_income ]

    ## The following lines are commented out -> used for debugging custom function.
    ## print('"Random" Decision Type Players : ', random_players)
    ## print('Generated Income for "Random" Decision Type Players : ', random_income)
    ## print('Profit from "Random" Strategy : ', profit_earned)

    fixed_probability = []
    random_probability = []
    # These probability variables have the original expectations of (Fixed : Random) 
    # as (0 : 1), unless there is a Loss from following the 'Random' Strategy.
    for earning in range(len(random_income)) :
        if (profit_earned[earning] > 0) :
            fixed_probability.append(0)
            random_probability.append(1)
        else :
            fixed_probability.append(100 / (100 + earning))
            random_probability.append(1 - fixed_probability[earning])

    for player in range(len(random_players)) :
        strategy_probabilities.append([('Fixed', fixed_probability[player]), ('Random', random_probability[player])])
    return strategy_probabilities

def countFixedAndRandomStrategiesFollowed(players) :
    number_of_fixed_strategies_followed = 0
    strategies_followed = strategiesFollowed(players)

    ## The following line is commented out -> used for debugging custom function.
    ## print("Strategies Followed : ", strategies_followed)

    for strategy in range(len(strategies_followed)) :
        if (strategies_followed[strategy] == 'Fixed') :
            number_of_fixed_strategies_followed += 1
    return strategies_followed, number_of_fixed_strategies_followed

########################################
###### Main Function (Simulation) ######
########################################

def simulationAI (type_options, option_probabilities, number_of_players, number_of_rounds) :
    # Generate the specified number of players.
    decision_types = generatePlayers(type_options, option_probabilities, number_of_players)

    ## The following line is commented out -> used for debugging custom function.
    ## print('Decision Types of Players Generated : ', decision_types)     

    # Count the number of 'Fixed' Decision Type players generated.
    number_fixed_players = countFixedPlayers(decision_types)

    ## The following line is commented out -> used for debugging custom function.
    ## print('Number of "Fixed" Decision Type Players : ', number_fixed_players)  

    # Count the number of 'Random' Decision Type players generated.
    number_random_players = countRandomPlayers(decision_types)

    ## The following line is commented out -> used for debugging custom function.
    ## print('Number of "Random" Decision Type Players : ', number_random_players)

    # List the expectations of the Strategies the 'Fixed' Decision Type players will follow.
    strategy_expectations_fixed_players = strategiesFixedPlayers(number_fixed_players)
    
    ## The following line is commented out -> used for debugging custom function.    
    ## print('Strategy Expectations of "Fixed" Decision Type Players : ', strategy_expectations_fixed_players)
    
    # List the expectations of the Strategies the 'Random' Decision Type players will follow.
    strategy_expectations_random_players = strategiesRandomPlayers(number_random_players)

    ## The following line is commented out -> used for debugging custom function.
    ## print('Strategy Expectations of "Random" Decision Type Players : ', strategy_expectations_random_players)

    # The following empty lists will include the results
    # from each simulated round of the questionnaire. 
    results_number_of_fixed_strategies_followed = []
    results_number_of_fixed_strategies_followed_by_fixed_players = []
    results_number_of_fixed_strategies_followed_by_random_players = []
    results_updated_strategy_expectations_fixed_players = []
    results_updated_strategy_expectations_random_players = []

    for round in range(number_of_rounds) :
        print('Round # : ', round + 1)

        # Update the expectations of the Strategies the players will adhere to based on the previous Play Outcome.
        if (round > 0) :
            strategy_expectations_fixed_players = results_updated_strategy_expectations_fixed_players[len(results_updated_strategy_expectations_fixed_players) - 1]
            strategy_expectations_random_players = results_updated_strategy_expectations_random_players[len(results_updated_strategy_expectations_random_players) - 1]

        # Store the Strategies followed by the players of the different Decision Types.
        strategies_followed_fixed_players, number_of_fixed_strategies_followed_by_fixed_players = countFixedAndRandomStrategiesFollowed(strategy_expectations_fixed_players)
        strategies_followed_random_players, number_of_fixed_strategies_followed_by_random_players = countFixedAndRandomStrategiesFollowed(strategy_expectations_random_players)

        ## The following lines are commented out -> used for debugging custom function.
        ## print('Strategies Followed by "Fixed" Decision Type Players : ', strategies_followed_fixed_players)
        ## print('Number of "Fixed" Strategies Followed by "Fixed" Decision Type Players : ', number_of_fixed_strategies_followed_by_fixed_players)
        ## print('Strategies Followed by "Random" Decision Type Players : ', strategies_followed_random_players)
        ## print('Number of "Fixed" Strategies Followed by "Rando" Decision Type Players : ', number_of_fixed_strategies_followed_by_random_players)

        # Calculate the total number of 'Fixed' plays in the round.
        number_of_fixed_strategies_followed = number_of_fixed_strategies_followed_by_fixed_players + number_of_fixed_strategies_followed_by_random_players

        ## The following line is commented out -> used for debugging custom function.
        ## print('Total Number of "Fixed" Strategies Followed : ', number_of_fixed_strategies_followed)
        
        # Based on the Play Outcomes from this round, update the Strategy expectations for the different Decision Type players.
        updated_strategy_expectations_fixed_players = profitFixedPlayer(strategies_followed_fixed_players)
        updated_strategy_expectations_random_players = profitRandomPlayer(strategies_followed_random_players)

        ## The following lines are commented out -> used for debugging custom function.
        ## print('Updated Strategy Expectations of "Fixed" Decision Type Players : ',  updated_strategy_expectations_fixed_players)
        ## print('Updated Strategy Expectations of "Random" Decision Type Players : ',  updated_strategy_expectations_random_players)

        # Update the lists containing the results from the particular round of the simulation.
        results_number_of_fixed_strategies_followed.append(number_of_fixed_strategies_followed)
        results_number_of_fixed_strategies_followed_by_fixed_players.append(number_of_fixed_strategies_followed_by_fixed_players)
        results_number_of_fixed_strategies_followed_by_random_players.append(number_of_fixed_strategies_followed_by_random_players)
        results_updated_strategy_expectations_fixed_players.append(updated_strategy_expectations_fixed_players)
        results_updated_strategy_expectations_random_players.append(updated_strategy_expectations_random_players)

    return results_number_of_fixed_strategies_followed, results_number_of_fixed_strategies_followed_by_fixed_players, results_number_of_fixed_strategies_followed_by_random_players

results_number_of_fixed_strategies_followed, results_number_of_fixed_strategies_followed_by_fixed_players, results_number_of_fixed_strategies_followed_by_random_players = simulationAI (type_options, option_probabilities, number_of_players, number_of_rounds)

print("\n******SIMULATION RESULTS******\n")

print('Number of "Fixed" Strategies Followed in Each Round : ', results_number_of_fixed_strategies_followed)
print('Number of "Fixed" Strategies Followed by "Fixed" Decision Type Players in Each Round : ', results_number_of_fixed_strategies_followed_by_fixed_players)
print('Number of "Fixed" Strategies Followed by "Random" Decision Type Players in Each Round : ', results_number_of_fixed_strategies_followed_by_random_players)

###########################
###### Graph Results ######
###########################

index = np.arange(number_of_rounds)
rounds = [str(index[i] + 1) for i in range(len(index))]

## The following line is commented out -> used for debugging list.    
## print(rounds)

# Create a subplot for the Simulation Results.
plt.subplot(2, 1, 1)

# Create a barplot with the different Simulation Results identified by a legend.
simulation_graph = plt.bar(index + 0.00, results_number_of_fixed_strategies_followed, color = "blue", width = 0.25, label = 'All Players in Simulation')
simulation_graph += plt.bar(index + 0.25, results_number_of_fixed_strategies_followed_by_fixed_players, color = "red", width = 0.25, label = '"Fixed" Decision Type Players in Simulation')
simulation_graph += plt.bar(index + 0.50, results_number_of_fixed_strategies_followed_by_random_players, color = "green", width = 0.25, label = '"Random" Decision Type Players in Simulation')

# Specify the tick markings, ensuring only integers are displayed on y-axis.
integer_markings = range(0, number_of_players + 1)
plt.xticks(index, rounds)
plt.yticks(integer_markings)

plt.title('Simulation Results and App Data')

# Place legend to the right of the plot.
plt.legend(fontsize = 7.5, loc = 'upper right', borderaxespad = 0.)

# Create a subplot for App Data.
plt.subplot(2, 1, 2)

# Create a barplot with the App Data identified by a legend.
user_data = plt.bar(index + 0.00, number_of_fixed_strategies_all_users, color = "black", width = 0.25, label = 'All App Users')
user_data += plt.bar(index + 0.25, number_of_fixed_strategies_investment, color = "orange", width = 0.25, label = 'Investment App Users')
user_data += plt.bar(index + 0.50, number_of_fixed_strategies_quadratic, color = "purple", width = 0.25, label = 'Quadratic App Users')

# Specify the x-axis label.
plt.xlabel('Round #')

y_label = ''
# Shift the y label to account for both subplots.
for i in range(number_of_players + 1) :
    for j in range(number_of_players + 1) :
        for k in range(int(0.75 * (number_of_players + 1))) :
            y_label += ' '
y_label += 'Number of "Fixed" Strategies Followed'

# Specify the y-axis label.
plt.ylabel(y_label)

# Specify the tick markings, ensuring only integers are displayed on y-axis.
integer_markings = range(0, number_of_players + 1)
plt.xticks(index, rounds)
plt.yticks(integer_markings)

# Place legend to the right of the plot.
plt.legend(fontsize = 7.5, loc = 'upper right', borderaxespad = 0.)

# Thank the users for their involvement in this experiment.
print("\n******TO APP USERS******\n")
for user in range(len(user_details_series.index)) : 
    message = 'Thank You ' + user_details_series[user] + '.'
    print(message)
print('End of Experiment')

plt.show()


