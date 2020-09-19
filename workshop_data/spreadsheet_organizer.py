######################################
########## Import Libraries ##########
######################################

# Deal with Tabular Data using Pandas Library.
import pandas as pd

################################################
######## Acquire Data from Excel File ##########
################################################

raw_dataframe = pd.read_excel('Results_Collected.xlsx')

# Check to ensure the app data isn't collected from bots.
for i in range(len(raw_dataframe.index)) :
    if (raw_dataframe['participant._is_bot'][i] == 1) :
        print('Error! Data is Acquired from Bots.')
        exit()

# Create a series to isolate relevant column information from 
# Excel Spreadsheet for comparing the app data with the AI 
# simulation results. Create a series to contain column information.
name_series = raw_dataframe['workshop_app.1.player.Name_Initials_Consent']
age_series = raw_dataframe['workshop_app.1.player.Age_Consent']

app_choice_series = raw_dataframe['workshop_app.1.player.App_Choice']

# It is known beforehand that the players will complete 5 rounds of the questionnaire.
# A look inside a sample excel file confirms the knowledge of this information.
round_1_series = raw_dataframe['workshop_app.1.player.Decision_1']
round_2_series = raw_dataframe['workshop_app.1.player.Decision_2']
round_3_series = raw_dataframe['workshop_app.1.player.Decision_3']
round_4_series = raw_dataframe['workshop_app.1.player.Decision_4']
round_5_series = raw_dataframe['workshop_app.1.player.Decision_5']

######################################
######## Modify Data Labels ##########
######################################

# Combine the player details in a single list.
player_details_column = []
for i in range(len(name_series)) :
    player_details = str(name_series[i]) + ' - ' + str(age_series[i])
    player_details_column.append(player_details)
print(player_details_column)

# Convert the player details list into a series.
player_details_series = pd.DataFrame(player_details_column)

# Combine the series into a new dataframe.
combined_dataframe = pd.concat([
    player_details_series, app_choice_series, 
    round_1_series, round_2_series, 
    round_3_series, round_4_series, 
    round_5_series], axis = 1)
# Rename the columns in the dataframe for readability.
combined_dataframe.rename(columns = {
    0 : 'Player Details',
    'workshop_app.1.player.App_Choice' : 'App Choice',
    'workshop_app.1.player.Decision_1' : 'Round 1', 
    'workshop_app.1.player.Decision_2' : 'Round 2', 
    'workshop_app.1.player.Decision_3' : 'Round 3', 
    'workshop_app.1.player.Decision_4' : 'Round 4', 
    'workshop_app.1.player.Decision_5' : 'Round 5', 
    }, inplace = True)

# View final dataframe before inputting to a formatted Excel Spreadsheet.
print(combined_dataframe)

##########################################################
############## Writing to Excel Spreadsheet ##############
##########################################################

# Use Pandas library function ExcelWriter to input the DataFrame. 
writer = pd.ExcelWriter('Relevant_Results.xlsx', engine = 'xlsxwriter')

# Write content to new Excel Spreadsheet.
combined_dataframe.to_excel(writer,
             sheet_name = 'questionnaire_results')  
             
# Ensure the Excel file isn't open at the time of saving.
writer.save()
writer.close()
