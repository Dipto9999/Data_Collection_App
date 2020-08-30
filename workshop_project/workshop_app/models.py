from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as c,
    currency_range,
)

author = 'Muntakim Rahman'

doc = """
This app collects player information to make mathematical calculations.
"""


###################################################################
###################################################################
######### Define Constants with Values that Won't Change. #########
###################################################################
###################################################################


class Constants(BaseConstants) :
    #####################################
    ######## General Information ########
    #####################################

    name_in_url = 'workshop_app'
    players_per_group = None
    # This constant refers to the number of trials conducted.
    num_rounds = 1
    name_developer = "Muntakim Rahman"

    ###################################
    ############ App Choice ###########
    ###################################

    quadratic = 0
    investment = 1

    #####################################
    ############# Education #############
    #####################################

    economics = 0
    other = 1

    #####################################
    ############## Concern ##############
    #####################################

    job = 0
    health = 1

    ######################################
    ############# Decisions ##############
    ######################################

    fixed_amount = 0
    random_amount = 1


###########################################################################
###########################################################################
########### No Subsession in Between Apps. Will be Unattended. ############
###########################################################################
###########################################################################


class Subsession(BaseSubsession) :
    pass


###########################################################################
###########################################################################
####### Not a Group App. Concerns an Individual Making a Decision. ########
###########################################################################
###########################################################################


class Group(BaseGroup) :
    pass


####################################################
####################################################
###### Input that Influences Decision Making. ######
####################################################
####################################################


class Player(BasePlayer) :

    ################################
    ######## Player Consent ########
    ################################

    # StringField type is specified for text strings.
    Name_Initials_Consent = models.StringField()
    # Individual must have age between 10 and 100.
    Age_Consent = models.PositiveIntegerField(min = 10, max = 100)
    # Individual isn't required to provide the following consent fields.
    Email_Consent = models.StringField(blank = True)
    Contact_Consent = models.FloatField(blank = True)
        
    #####################################
    ########## Instructions #############
    #####################################

    # FloatField type is specified for real numbers.
    App_Choice = models.FloatField(
        choices = [
            [Constants.quadratic, 'Quadratic'],
            [Constants.investment, 'Investment'],
        ],
        verbose_name = 'Choice of App? ',
        widget = widgets.RadioSelect)
    Education = models.FloatField(
        choices = [
            [Constants.economics, 'Economics'],
            [Constants.other, 'Other'],
        ],
        verbose_name = 'Educational Background? ',
        widget = widgets.RadioSelect)
    Concern = models.FloatField(
        choices = [
            [Constants.job, 'Job'],
            [Constants.health, 'Health'],
        ],
        verbose_name = 'Current Major Concern? ',
        widget = widgets.RadioSelect)

    ######################################
    ####### Quadratic Coefficients #######
    ######################################

    A_Coefficient = models.FloatField()
    B_Coefficient = models.FloatField()
    C_Coefficient = models.FloatField()

    ##################################
    ####### Investment Details #######
    ##################################

    Principal_Amount = models.FloatField()
    # Interest Rate must be between 0 and 1 (i.e. decimal format).
    Interest_Rate = models.FloatField(min = 0, max = 1)
    Maturity_Period = models.FloatField()
    
    ############################
    ######## Decisions #########
    ############################

    # CharField indicates that this may have one of the following 
    # values indicated in the choices list for individuals to 
    # express what they want (Similar to True/False Input). 
    Decision_1 = models.FloatField(
        choices = [
            [Constants.random_amount, 'Random Amount'], 
            [Constants.fixed_amount, 'Fixed Amount']
        ],
        verbose_name = 'Decision 1? ',
        widget = widgets.RadioSelect)

    # Similarly, store a value for the player's second decision.
    Decision_2 = models.FloatField(
        choices = [
            [Constants.random_amount, 'Random Amount'], 
            [Constants.fixed_amount, 'Fixed Amount']
        ],
        verbose_name = 'Decision 2? ',
        widget = widgets.RadioSelect)

    # Similarly, store a value for the player's third decision.
    Decision_3 = models.FloatField(
        choices = [
            [Constants.random_amount, 'Random Amount'], 
            [Constants.fixed_amount, 'Fixed Amount']
        ],
        verbose_name = 'Decision 3? ',
        widget = widgets.RadioSelect)

    # Similarly, store a value for the player's fourth decision.
    Decision_4 = models.FloatField(
        choices = [
            [Constants.random_amount, 'Random Amount'], 
            [Constants.fixed_amount, 'Fixed Amount']
        ],
        verbose_name = 'Decision 4? ',
        widget = widgets.RadioSelect)

    # Similarly, store a value for the player's fifth decision.
    Decision_5 = models.FloatField(
        choices = [
            [Constants.random_amount, 'Random Amount'], 
            [Constants.fixed_amount, 'Fixed Amount']
        ],
        verbose_name = 'Decision 5? ',
        widget = widgets.RadioSelect)      

    # Store a value for the player's total earnings.
    # These will be updated on each questionnaire page 
    # based on the chosen method of income.
    Total_Earnings = models.FloatField(initial = 0)

    # Store a value for the player's previous earnings to the current page. 
    # This accounts for the player refreshing the page.
    Previous_Earnings = models.FloatField(initial = 0)

    # Store a counter for the number of times the 
    # player's total earnings were changed.
    # This is used to account for the player refreshing the page.
    Number_Earnings = models.IntegerField(initial = 0)