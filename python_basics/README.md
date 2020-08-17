# Python Basics

## Contents
* [Overview](#Overview)
* [Credit](#Credit)

## Overview
Prior to developing the <b>Web App</b>, the following scripts were written to 
explore the language and its features <i>(i.e. Integers, Strings, Booleans, Custom Functions)</i>. 

The <a href = "further_exploration.py">further_exploration</a> file is of interest due to the creation of a 
simple Investment Function with the use of <i>If Statements</i>.

```python
    def investment(principal, interest, year) :
        total_profit = principal * (1 + interest) ** year
        net_profit = total_profit - principal

        if interest <= 0.5 :
            statement = "Less Interest"
        elif (interest <= 1 ) :
            statement = "More Interest"
        elif interest > 1 :
            statement = "Be Cautious! This is a Ponzi Scheme."

        return total_profit, net_profit, statement
```

## Credit
Credit should be provided to <b>Simon Frasier University</b> and <b>Professor Farouk Abdul-Salam</b> for providing
insight into the usage of these tools to create and deploy the app. This was completed as part of an 
<a href = "https://sites.google.com/view/farouk-abdul-salam/my-teaching-workshop/workshop?authuser=0">Online Workshop</a>.
