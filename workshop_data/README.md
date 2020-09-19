# Data Collection

## Contents
* [Overview](#Overview)
* [Python Script](#Python-Script)
    * [Organizing Columns](#Organizing-Columns)
* [Credit](#Credit)

## Overview
We acquired user data in our deployed <b>Web Application</b> and it provided us with a <a href = "Results_Collected.xlsx">Results Collected</a> <b>Excel Spreadsheet</b>. However, this is hard to read and extract data from. To deal with this, I wrote a <a href = "spreadsheet_organizer.py">Spreadsheet Organizer</a> <b>Python</b> script, which imports the <b>Pandas Library</b> and restructures the useful information from the app results using <b>DataFrames</b>. This labelled data is organized in another <a href = "Relevant_Results.py">Relevant Results</a> <b>Excel Spreadsheet</b> in order to make it easier to display this information alongside our simulation results.

## Python Script 
The knowledge required to complete this organizer was acquired from a prior exploration of the <b>Scikit-Learn Library</b> as well as a corporate <b>XML</b> and <b>Excel</b> organizer I had wrote separately.</br>

### Organizing Columns
Without digressing, the most useful functionality of this script comes from the separation of the column data into individual <b>Series</b> as shown below. 
```python
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
```

These were concatenated into a new <b>DataFrame</b> after a few other optional modifications.
```python
    combined_dataframe = pd.concat([
    player_details_series, app_choice_series, 
    round_1_series, round_2_series, 
    round_3_series, round_4_series, 
    round_5_series], axis = 1)
```

In order to prepare the columns for our analysis in the AI Simulation, we renamed the <b>DataFrame</b> columns 
prior to saving this in the <b>Excel Spreadsheet</b>.
```python
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
```

## Credit
Credit should be provided to <b>Simon Frasier University</b> and <b>Professor Farouk Abdul-Salam</b> for providing
insight into the usage of these tools to create and deploy the app. This was completed as part of an 
<a href = "https://sites.google.com/view/farouk-abdul-salam/my-teaching-workshop/workshop?authuser=0">Online Workshop</a>.