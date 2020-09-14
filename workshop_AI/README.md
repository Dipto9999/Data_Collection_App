# AI Simulation

## Contents
* [Overview](#Overview)
    * [Assumptions](#Assumptions)
* [Script Details](#Script-Details)
* [Credit](#Credit)

## Overview
We used <b>Python</b> to simulate results to the questionnaire in the <b>Web Application</b>.  
The <a href = "naive_AI.py">naive_AI</a> <b>Python</b> script makes predictions of user data. 
It was written with the establishment of several assumptions regarding user behavior, which are discussed below. The script imports the 
<b>Matplotlib Library</b> to generate data visualizations of the simulation results as well as the actual data collected from the deployed app.  

### Assumptions
There are originally players with 2 Decision Types which are either "Fixed" or "Random". If the Strategy corresponding to their Decision Type provides the players a profit, they continue to follow the Strategy adhering to their Decision Type in the questionnaire. However, if they make a loss from following the default Strategy, they have a chance of temporarily altering their Strategy for the next round in the questionnaire. The original Decision Type of the player doesn't change regardless of the play outcome (i.e. profit/loss).

## Script Details
The <a href = "naive_AI.py">naive_AI</a> <b>Python</b> script produces simulation results through calling several <i>custom functions</i> in a <i>main function</i> to separate the simulation results of interest to our purposes. 

These include :
<ul>
    <li>Total Number of "Fixed" Plays in Each Round</li>
    <ul>
        <li>Number of "Fixed" Plays in Each Round by "Fixed" Players</li>
        <li>Number of "Fixed" Plays in Each Round by "Random" Players</li>
    </ul>
</ul>

## Credit
Credit should be provided to <b>Simon Frasier University</b> and <b>Professor Farouk Abdul-Salam</b> for providing
insight into the usage of these tools to create and deploy the app. This was completed as part of an 
<a href = "https://sites.google.com/view/farouk-abdul-salam/my-teaching-workshop/workshop?authuser=0">Online Workshop</a>.