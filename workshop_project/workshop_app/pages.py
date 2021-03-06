#########################################################################################################################################
#########################################################################################################################################
################################################# Keep Track of How Pages are Accessed. #################################################
#########################################################################################################################################
#########################################################################################################################################


from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
# Import module random to generate pseudo-random numbers when player makes decision.
import random

#######################
###### First Page #####
#######################

class Introduction(Page) :
    form_model = 'player'
    # This list contains variables from class Player in pages.py.
    form_fields = ['Name_Initials_Consent', 'Age_Consent', 'Email_Consent', 'Contact_Consent'] 

###########################
##### App Instruction #####
###########################

class Instruction(Page) :
    form_model = 'player'
    form_fields = ['App_Choice', 'Education', 'Concern']

##################################
######## Quadratic Inputs ########
##################################

class Input_Quadratic(Page) :
    form_model = 'player'
    form_fields = ['A_Coefficient', 'B_Coefficient', 'C_Coefficient']

    # Page is displayed if the app was chosen to be quadratic.
        # All functions defined in a class require a self parameter to specify 
        # that they are invoked on the particular object in question. 
    def is_displayed(self) :
        return self.player.App_Choice == Constants.quadratic

    # Function advertises a job for economics students looking for work and 
    # face masks for individuals worried about their health.
    def vars_for_template(self) :
        # Advertise job fair for economics students worried about finding a job.
        if ((self.player.Concern == Constants.job) and (self.player.Education == Constants.economics)) :
            return {'Advert' : 'Please Sign Up For The Upcoming Job Fair.'}
        # Advertise face masks for individuals worried about their health.
        else :
            return {'Advert' : 'We Have Face Masks Available For Purchase.'}

#################################
####### Quadratic Results #######
#################################

class Results_Quadratic(Page) :
    ## Note that since we don't expect the player to provide us with any information,
    ## there is no reason to provide a form model and form fields.

    # Page is displayed if the app was chosen to be quadratic.
    def is_displayed(self) :
        return self.player.App_Choice == Constants.quadratic

    # Function returns the quadratic coefficients as well as the roots of the quadratic equation to precision of 2 decimal places.
    def vars_for_template(self) :
        # If the quadratic formula is given by A*(x^2) + B*(x) + C, the roots are calculated as : 
            # ((-B + ((B^2 - 4*A*C)^(0.5)))/(2*A))
            # ((-B - ((B^2 - 4*A*C)^(0.5)))/(2*A))
        positive_result = (-(self.player.B_Coefficient) + ((self.player.B_Coefficient ** 2) - 4 * (self.player.A_Coefficient) * (self.player.C_Coefficient)) ** (0.5)) / (2*(self.player.A_Coefficient))
        negative_result = (-(self.player.B_Coefficient) - ((self.player.B_Coefficient ** 2) - 4 * (self.player.A_Coefficient) * (self.player.C_Coefficient)) ** (0.5)) / (2*(self.player.A_Coefficient))
        
        return {
            'A_Coefficient' : round(self.player.A_Coefficient, 2),
            'B_Coefficient' : round(self.player.B_Coefficient, 2),
            'C_Coefficient' : round(self.player.C_Coefficient, 2),
            # In case roots are complex, the real and imaginary parts must be rounded separately.
            'Final_Result_Positive' : (round(positive_result.real, 2) + round(positive_result.imag, 2) * 1j),
            'Final_Result_Negative' : (round(negative_result.real, 2) + round(negative_result.imag, 2) * 1j)
        }

###################################
######## Investment Inputs ########
###################################

class Input_Investment(Page) :
    form_model = 'player'
    form_fields = ['Principal_Amount', 'Interest_Rate', 'Maturity_Period']

    # Page is displayed if the app was chosen to be investment.
    def is_displayed(self) :
        return self.player.App_Choice == Constants.investment

    # Function advertises a job for economics students looking for work and 
    # face masks for individuals worried about their health.
    def vars_for_template(self) :
        # Advertise job fair for economics students worried about finding a job.
        if ((self.player.Concern == Constants.job) and (self.player.Education == Constants.economics)) :
            return {'Advert' : 'Please Sign Up For The Upcoming Job Fair.'}
        # Advertise face masks for individuals worried about their health.
        else :
            return {'Advert' : 'We Have Face Masks Available For Purchase.'}

##################################
####### Investment Results #######
##################################

class Results_Investment(Page) :
    # Page is displayed if the app was chosen to be investment.
    def is_displayed(self) :
        return self.player.App_Choice == Constants.investment

    # Function returns the investment details as well as the final returns of investment to 2 decimal places.
    def vars_for_template(self) :
        # Final returns are calculated as ((Principal Amount) * ( ( 1 + (Interest Rate) ) ^ (Maturity Period) )).
        final_returns = self.player.Principal_Amount * ((1 + self.player.Interest_Rate) ** (self.player.Maturity_Period))

        return {
            'Principal_Amount' : round(self.player.Principal_Amount, 2),
            'Interest_Rate' : round(self.player.Interest_Rate, 2),
            'Maturity_Period' : round(self.player.Maturity_Period, 2),
            'Final_Returns' : round(final_returns, 2)
        }

######################################
###### Taking Player Decision 1 ######
######################################

class Questionnaire_COVID_1(Page) :
    form_model = 'player'
    form_fields = ['Decision_1']

class Results_Questionnaire_COVID_1(Page) :
    def vars_for_template(self) :
        # Generate a random number between 50 and 150 to a precision of 2 decimal points.
        generated_value = round(random.uniform(50, 150), 2)
        difference = abs(generated_value - 100)

        # Ensure that the total earnings are accurately 
        # updated when the player refreshes the current page.
        if (self.player.Number_Earnings == 0) :
            self.player.Previous_Earnings = self.player.Total_Earnings
            self.player.Number_Earnings = self.player.Number_Earnings + 1      

        # Case where player chooses fixed amount and loses out on chance for generated value.
        if ((self.player.Decision_1 == Constants.fixed_amount) and (generated_value > 100)) :
            self.player.Total_Earnings = self.player.Previous_Earnings + 100
            return {
                'Inform' : 'You Have Chosen A Fixed Amount Of $100.',
                'Statement_1' : 'Your drawed amount of',
                'Random_Number' : '$' + str(generated_value),
                'Statement_2' : 'would have been', 
                'Comparison' : 'greater than',
                'Statement_3' : 'the constant amount of $100 by',
                'Difference' : '$' + str(round(difference, 2)),
                'Total_Income' : '$' + str(round(self.player.Total_Earnings,2))
            }
        # Case where player chooses fixed amount and wins on chance for generated value.
        elif ((self.player.Decision_1 == Constants.fixed_amount) and (generated_value < 100)) :
            self.player.Total_Earnings = self.player.Previous_Earnings + 100
            return {
                'Inform' : 'You Have Chosen A Fixed Amount Of $100.',
                'Statement_1' : 'Your drawed amount of',
                'Random_Number' : '$' + str(generated_value),
                'Statement_2' : 'would have been', 
                'Comparison' : 'less than',
                'Statement_3' : 'the constant amount of $100 by',
                'Difference' : '$' + str(round(difference, 2)),
                'Total_Income' : '$' + str(round(self.player.Total_Earnings,2))
            }
        # Case where player chooses fixed amount and the generated value would have been $100.
        elif ((self.player.Decision_1 == Constants.fixed_amount) and (generated_value == 100)) :
            self.player.Total_Earnings = self.player.Previous_Earnings + 100
            return {
                'Inform' : 'You Have Chosen A Fixed Amount Of $100.',
                'Statement_1' : 'Your drawed amount of',
                'Random_Number' : '$' + str(generated_value),
                'Statement_2' : 'would have been', 
                'Comparison' : 'equal to',
                'Statement_3' : 'the constant amount of $100',
                'Difference' : '',
                'Total_Income' : '$' + str(round(self.player.Total_Earnings,2))
            }    
        # Case where player chooses generated value and wins on chance.
        elif ((self.player.Decision_1 == Constants.random_amount) and (generated_value > 100)) :
            self.player.Total_Earnings = self.player.Previous_Earnings + generated_value
            return {
                'Inform' : 'You Have Chosen A Random Amount Instead Of The Constant Amount Of $100.',
                'Statement_1' : 'Your drawed amount of',
                'Random_Number' : '$' + str(generated_value),
                'Statement_2' : 'is', 
                'Comparison' : 'greater than',
                'Statement_3' : 'the constant amount of $100 by',
                'Difference' : '$' + str(round(difference, 2)),
                'Total_Income' : '$' + str(round(self.player.Total_Earnings,2))
            }
        # Case where player chooses generated value and makes loss on chance.
        elif ((self.player.Decision_1 == Constants.random_amount) and (generated_value < 100)) :
            self.player.Total_Earnings = self.player.Previous_Earnings + generated_value
            return {
                'Inform' : 'You Have Chosen A Random Amount Instead Of The Constant Amount Of $100.',
                'Statement_1' : 'Your drawed amount of',
                'Random_Number' : '$' + str(generated_value),
                'Statement_2' : 'is', 
                'Comparison' : 'less than',
                'Statement_3' : 'the constant amount of $100 by',
                'Difference' : '$' + str(round(difference, 2)),
                'Total_Income' : '$' + str(round(self.player.Total_Earnings,2))
            }
        # Case where player chooses generated value and it yields $100.
        elif ((self.player.Decision_1 == Constants.random_amount) and (generated_value == 100)) :
            self.player.Total_Earnings = self.player.Previous_Earnings + 100
            return {
                'Inform' : 'You Have Chosen A Random Amount Instead Of The Constant Amount Of $100.',
                'Statement_1' : 'Your drawed amount of',
                'Random_Number' : '$' + str(generated_value),
                'Statement_2' : 'is', 
                'Comparison' : 'equal to',
                'Statement_3' : 'the constant amount of $100',
                'Difference' : '',
                'Total_Income' : '$' + str(round(self.player.Total_Earnings,2))
            }    

######################################
###### Taking Player Decision 2 ######
######################################

class Questionnaire_COVID_2(Page) :
    form_model = 'player'
    form_fields = ['Decision_2']

class Results_Questionnaire_COVID_2(Page) :
    def vars_for_template(self) :
        # Generate a random number between 50 and 150 to a precision of 2 decimal points.
        generated_value = round(random.uniform(50, 150), 2)
        difference = abs(generated_value - 100)
    
        # Ensure that the total earnings are accurately 
        # updated when the player refreshes the current page.
        if (self.player.Number_Earnings == 1) :
            self.player.Previous_Earnings = self.player.Total_Earnings
            self.player.Number_Earnings = self.player.Number_Earnings + 1      

        # Case where player chooses fixed amount and loses out on chance for generated value.
        if ((self.player.Decision_2 == Constants.fixed_amount) and (generated_value > 100)) :
            self.player.Total_Earnings = self.player.Previous_Earnings + 100
            return {
                'Inform' : 'You Have Chosen A Fixed Amount Of $100.',
                'Statement_1' : 'Your drawed amount of',
                'Random_Number' : '$' + str(generated_value),
                'Statement_2' : 'would have been', 
                'Comparison' : 'greater than',
                'Statement_3' : 'the constant amount of $100 by',
                'Difference' : '$' + str(round(difference, 2)),
                'Total_Income' : '$' + str(round(self.player.Total_Earnings,2))
            }
        # Case where player chooses fixed amount and wins on chance for generated value.
        elif ((self.player.Decision_2 == Constants.fixed_amount) and (generated_value < 100)) :
            self.player.Total_Earnings = self.player.Previous_Earnings + 100
            return {
                'Inform' : 'You Have Chosen A Fixed Amount Of $100.',
                'Statement_1' : 'Your drawed amount of',
                'Random_Number' : '$' + str(generated_value),
                'Statement_2' : 'would have been', 
                'Comparison' : 'less than',
                'Statement_3' : 'the constant amount of $100 by',
                'Difference' : '$' + str(round(difference, 2)),
                'Total_Income' : '$' + str(round(self.player.Total_Earnings,2))
            }
        # Case where player chooses fixed amount and the generated value would have been $100.
        elif ((self.player.Decision_2 == Constants.fixed_amount) and (generated_value == 100)) :
            self.player.Total_Earnings = self.player.Previous_Earnings + 100
            return {
                'Inform' : 'You Have Chosen A Fixed Amount Of $100.',
                'Statement_1' : 'Your drawed amount of',
                'Random_Number' : '$' + str(generated_value),
                'Statement_2' : 'would have been', 
                'Comparison' : 'equal to',
                'Statement_3' : 'the constant amount of $100',
                'Difference' : '',
                'Total_Income' : '$' + str(round(self.player.Total_Earnings,2))
            }    
        # Case where player chooses generated value and wins on chance.
        elif ((self.player.Decision_2 == Constants.random_amount) and (generated_value > 100)) :
            self.player.Total_Earnings = self.player.Previous_Earnings + generated_value
            return {
                'Inform' : 'You Have Chosen A Random Amount Instead Of The Constant Amount Of $100.',
                'Statement_1' : 'Your drawed amount of',
                'Random_Number' : '$' + str(generated_value),
                'Statement_2' : 'is', 
                'Comparison' : 'greater than',
                'Statement_3' : 'the constant amount of $100 by',
                'Difference' : '$' + str(round(difference, 2)),
                'Total_Income' : '$' + str(round(self.player.Total_Earnings,2))
            }
        # Case where player chooses generated value and makes loss on chance.
        elif ((self.player.Decision_2 == Constants.random_amount) and (generated_value < 100)) :
            self.player.Total_Earnings = self.player.Previous_Earnings + generated_value
            return {
                'Inform' : 'You Have Chosen A Random Amount Instead Of The Constant Amount Of $100.',
                'Statement_1' : 'Your drawed amount of',
                'Random_Number' : '$' + str(generated_value),
                'Statement_2' : 'is', 
                'Comparison' : 'less than',
                'Statement_3' : 'the constant amount of $100 by',
                'Difference' : '$' + str(round(difference, 2)),
                'Total_Income' : '$' + str(round(self.player.Total_Earnings,2))
            }
        # Case where player chooses generated value and it yields $100.
        elif ((self.player.Decision_2 == Constants.random_amount) and (generated_value == 100)) :
            self.player.Total_Earnings = self.player.Previous_Earnings + 100
            return {
                'Inform' : 'You Have Chosen A Random Amount Instead Of The Constant Amount Of $100.',
                'Statement_1' : 'Your drawed amount of',
                'Random_Number' : '$' + str(generated_value),
                'Statement_2' : 'is', 
                'Comparison' : 'equal to',
                'Statement_3' : 'the constant amount of $100',
                'Difference' : '',
                'Total_Income' : '$' + str(round(self.player.Total_Earnings,2))
            }    


######################################
###### Taking Player Decision 3 ######
######################################

class Questionnaire_COVID_3(Page) :
    form_model = 'player'
    form_fields = ['Decision_3']

class Results_Questionnaire_COVID_3(Page) :
    def vars_for_template(self) :
        # Generate a random number between 50 and 150 to a precision of 2 decimal points.
        generated_value = round(random.uniform(50, 150), 2)
        difference = abs(generated_value - 100)

        # Ensure that the total earnings are accurately 
        # updated when the player refreshes the current page.
        if (self.player.Number_Earnings == 2) :
            self.player.Previous_Earnings = self.player.Total_Earnings
            self.player.Number_Earnings = self.player.Number_Earnings + 1      

        # Case where player chooses fixed amount and loses out on chance for generated value.
        if ((self.player.Decision_3 == Constants.fixed_amount) and (generated_value > 100)) :
            self.player.Total_Earnings = self.player.Previous_Earnings + 100
            return {
                'Inform' : 'You Have Chosen A Fixed Amount Of $100.',
                'Statement_1' : 'Your drawed amount of',
                'Random_Number' : '$' + str(generated_value),
                'Statement_2' : 'would have been', 
                'Comparison' : 'greater than',
                'Statement_3' : 'the constant amount of $100 by',
                'Difference' : '$' + str(round(difference, 2)),
                'Total_Income' : '$' + str(round(self.player.Total_Earnings,2))
            }
        # Case where player chooses fixed amount and wins on chance for generated value.
        elif ((self.player.Decision_3 == Constants.fixed_amount) and (generated_value < 100)) :
            self.player.Total_Earnings = self.player.Previous_Earnings + 100
            return {
                'Inform' : 'You Have Chosen A Fixed Amount Of $100.',
                'Statement_1' : 'Your drawed amount of',
                'Random_Number' : '$' + str(generated_value),
                'Statement_2' : 'would have been', 
                'Comparison' : 'less than',
                'Statement_3' : 'the constant amount of $100 by',
                'Difference' : '$' + str(round(difference, 2)),
                'Total_Income' : '$' + str(round(self.player.Total_Earnings,2))
            }
        # Case where player chooses fixed amount and the generated value would have been $100.
        elif ((self.player.Decision_3 == Constants.fixed_amount) and (generated_value == 100)) :
            self.player.Total_Earnings = self.player.Previous_Earnings + 100
            return {
                'Inform' : 'You Have Chosen A Fixed Amount Of $100.',
                'Statement_1' : 'Your drawed amount of',
                'Random_Number' : '$' + str(generated_value),
                'Statement_2' : 'would have been', 
                'Comparison' : 'equal to',
                'Statement_3' : 'the constant amount of $100',
                'Difference' : '',
                'Total_Income' : '$' + str(round(self.player.Total_Earnings,2))
            }    
        # Case where player chooses generated value and wins on chance.
        elif ((self.player.Decision_3 == Constants.random_amount) and (generated_value > 100)) :
            self.player.Total_Earnings = self.player.Previous_Earnings + generated_value
            return {
                'Inform' : 'You Have Chosen A Random Amount Instead Of The Constant Amount Of $100.',
                'Statement_1' : 'Your drawed amount of',
                'Random_Number' : '$' + str(generated_value),
                'Statement_2' : 'is', 
                'Comparison' : 'greater than',
                'Statement_3' : 'the constant amount of $100 by',
                'Difference' : '$' + str(round(difference, 2)),
                'Total_Income' : '$' + str(round(self.player.Total_Earnings,2))
            }
        # Case where player chooses generated value and makes loss on chance.
        elif ((self.player.Decision_3 == Constants.random_amount) and (generated_value < 100)) :
            self.player.Total_Earnings = self.player.Previous_Earnings + generated_value
            return {
                'Inform' : 'You Have Chosen A Random Amount Instead Of The Constant Amount Of $100.',
                'Statement_1' : 'Your drawed amount of',
                'Random_Number' : '$' + str(generated_value),
                'Statement_2' : 'is', 
                'Comparison' : 'less than',
                'Statement_3' : 'the constant amount of $100 by',
                'Difference' : '$' + str(round(difference, 2)),
                'Total_Income' : '$' + str(round(self.player.Total_Earnings,2))
            }
        # Case where player chooses generated value and it yields $100.
        elif ((self.player.Decision_3 == Constants.random_amount) and (generated_value == 100)) :
            self.player.Total_Earnings = self.player.Previous_Earnings + 100
            return {
                'Inform' : 'You Have Chosen A Random Amount Instead Of The Constant Amount Of $100.',
                'Statement_1' : 'Your drawed amount of',
                'Random_Number' : '$' + str(generated_value),
                'Statement_2' : 'is', 
                'Comparison' : 'equal to',
                'Statement_3' : 'the constant amount of $100',
                'Difference' : '',
                'Total_Income' : '$' + str(round(self.player.Total_Earnings,2))
            }    

######################################
###### Taking Player Decision 4 ######
######################################

class Questionnaire_COVID_4(Page) :
    form_model = 'player'
    form_fields = ['Decision_4']

class Results_Questionnaire_COVID_4(Page) :
    def vars_for_template(self) :
        # Generate a random number between 50 and 150 to a precision of 2 decimal points.
        generated_value = round(random.uniform(50, 150), 2)
        difference = abs(generated_value - 100)

        # Ensure that the total earnings are accurately 
        # updated when the player refreshes the current page.
        if (self.player.Number_Earnings == 3) :
            self.player.Previous_Earnings = self.player.Total_Earnings
            self.player.Number_Earnings = self.player.Number_Earnings + 1   

        # Case where player chooses fixed amount and loses out on chance for generated value.
        if ((self.player.Decision_4 == Constants.fixed_amount) and (generated_value > 100)) :
            self.player.Total_Earnings = self.player.Previous_Earnings + 100
            return {
                'Inform' : 'You Have Chosen A Fixed Amount Of $100.',
                'Statement_1' : 'Your drawed amount of',
                'Random_Number' : '$' + str(generated_value),
                'Statement_2' : 'would have been', 
                'Comparison' : 'greater than',
                'Statement_3' : 'the constant amount of $100 by',
                'Difference' : '$' + str(round(difference, 2)),
                'Total_Income' : '$' + str(round(self.player.Total_Earnings,2))
            }
        # Case where player chooses fixed amount and wins on chance for generated value.
        elif ((self.player.Decision_4 == Constants.fixed_amount) and (generated_value < 100)) :
            self.player.Total_Earnings = self.player.Previous_Earnings + 100
            return {
                'Inform' : 'You Have Chosen A Fixed Amount Of $100.',
                'Statement_1' : 'Your drawed amount of',
                'Random_Number' : '$' + str(generated_value),
                'Statement_2' : 'would have been', 
                'Comparison' : 'less than',
                'Statement_3' : 'the constant amount of $100 by',
                'Difference' : '$' + str(round(difference, 2)),
                'Total_Income' : '$' + str(round(self.player.Total_Earnings,2))
            }
        # Case where player chooses fixed amount and the generated value would have been $100.
        elif ((self.player.Decision_4 == Constants.fixed_amount) and (generated_value == 100)) :
            self.player.Total_Earnings = self.player.Previous_Earnings + 100
            return {
                'Inform' : 'You Have Chosen A Fixed Amount Of $100.',
                'Statement_1' : 'Your drawed amount of',
                'Random_Number' : '$' + str(generated_value),
                'Statement_2' : 'would have been', 
                'Comparison' : 'equal to',
                'Statement_3' : 'the constant amount of $100',
                'Difference' : '',
                'Total_Income' : '$' + str(round(self.player.Total_Earnings,2))
            }    
        # Case where player chooses generated value and wins on chance.
        elif ((self.player.Decision_4 == Constants.random_amount) and (generated_value > 100)) :
            self.player.Total_Earnings = self.player.Previous_Earnings + generated_value
            return {
                'Inform' : 'You Have Chosen A Random Amount Instead Of The Constant Amount Of $100.',
                'Statement_1' : 'Your drawed amount of',
                'Random_Number' : '$' + str(generated_value),
                'Statement_2' : 'is', 
                'Comparison' : 'greater than',
                'Statement_3' : 'the constant amount of $100 by',
                'Difference' : '$' + str(round(difference, 2)),
                'Total_Income' : '$' + str(round(self.player.Total_Earnings,2))
            }
        # Case where player chooses generated value and makes loss on chance.
        elif ((self.player.Decision_4 == Constants.random_amount) and (generated_value < 100)) :
            self.player.Total_Earnings = self.player.Previous_Earnings + generated_value
            return {
                'Inform' : 'You Have Chosen A Random Amount Instead Of The Constant Amount Of $100.',
                'Statement_1' : 'Your drawed amount of',
                'Random_Number' : '$' + str(generated_value),
                'Statement_2' : 'is', 
                'Comparison' : 'less than',
                'Statement_3' : 'the constant amount of $100 by',
                'Difference' : '$' + str(round(difference, 2)),
                'Total_Income' : '$' + str(round(self.player.Total_Earnings,2))
            }
        # Case where player chooses generated value and it yields $100.
        elif ((self.player.Decision_4 == Constants.random_amount) and (generated_value == 100)) :
            self.player.Total_Earnings = self.player.Previous_Earnings + 100
            return {
                'Inform' : 'You Have Chosen A Random Amount Instead Of The Constant Amount Of $100.',
                'Statement_1' : 'Your drawed amount of',
                'Random_Number' : '$' + str(generated_value),
                'Statement_2' : 'is', 
                'Comparison' : 'equal to',
                'Statement_3' : 'the constant amount of $100',
                'Difference' : '',
                'Total_Income' : '$' + str(round(self.player.Total_Earnings,2))
            }    

######################################
###### Taking Player Decision 5 ######
######################################

class Questionnaire_COVID_5(Page) :
    form_model = 'player'
    form_fields = ['Decision_5']

class Results_Questionnaire_COVID_5(Page) :
    def vars_for_template(self) :
        # Generate a random number between 50 and 150 to a precision of 2 decimal points.
        generated_value = round(random.uniform(50, 150), 2)
        difference = abs(generated_value - 100)

        # This variable is intended to account for the difference 
        # between the total earnings and accumulative fixed earnings of 500.
        total_difference = 0

        # Ensure that the total earnings are accurately 
        # updated when the player refreshes the current page.
        if (self.player.Number_Earnings == 4) :
            self.player.Previous_Earnings = self.player.Total_Earnings
            self.player.Number_Earnings = self.player.Number_Earnings + 1   

        # The total earnings must be updated prior to evaluating the final value.
        if (self.player.Decision_5 == Constants.fixed_amount) :
            # Case where player chooses fixed amount. 
            self.player.Total_Earnings = self.player.Previous_Earnings + 100
            total_difference = abs(self.player.Total_Earnings - 500)
            # Case where player loses out on chance for generated value but wins on their total earnings.
            if ((generated_value > 100) and (self.player.Total_Earnings > 500)) :
                return {
                    'Inform' : 'You Have Chosen A Fixed Amount Of $100.',
                    'Statement_A1' : 'Your drawed amount of',
                    'Random_Number' : '$' + str(generated_value),
                    'Statement_A2' : 'would have been', 
                    'Comparison' : 'greater than',
                    'Statement_A3' : 'the constant amount of $100 by',
                    'Difference' : '$' + str(round(difference, 2)),
                    'Statement_B1' : 'Your total earnings of',
                    'Total_Income' : '$' + str(round(self.player.Total_Earnings,2)),
                    'Statement_B2' : 'are',
                    'Total_Comparison' : 'greater than',
                    'Statement_B3' : 'the accumulative constant earnings of $500 by',
                    'Total_Difference' : '$' + str(round(total_difference, 2))
                }
            # Case where player loses out on chance for generated value and also loses on their total earnings.
            elif ((generated_value > 100) and (self.player.Total_Earnings < 500)) :
                return {
                    'Inform' : 'You Have Chosen A Fixed Amount Of $100.',
                    'Statement_A1' : 'Your drawed amount of',
                    'Random_Number' : '$' + str(generated_value),
                    'Statement_A2' : 'would have been', 
                    'Comparison' : 'greater than',
                    'Statement_A3' : 'the constant amount of $100 by',
                    'Difference' : '$' + str(round(difference, 2)),
                    'Statement_B1' : 'Your total earnings of',
                    'Total_Income' : '$' + str(round(self.player.Total_Earnings,2)),
                    'Statement_B2' : 'are',
                    'Total_Comparison' : 'less than',
                    'Statement_B3' : 'the accumulative constant earnings of $500 by',
                    'Total_Difference' : '$' + str(round(total_difference, 2))
                }
            # Case where player loses out on chance for generated value and the total earnings are $500.
            elif ((generated_value > 100) and (self.player.Total_Earnings == 500)) :
                return {
                    'Inform' : 'You Have Chosen A Fixed Amount Of $100.',
                    'Statement_A1' : 'Your drawed amount of',
                    'Random_Number' : '$' + str(generated_value),
                    'Statement_A2' : 'would have been', 
                    'Comparison' : 'greater than',
                    'Statement_A3' : 'the constant amount of $100 by',
                    'Difference' : '$' + str(round(difference, 2)),
                    'Statement_B1' : 'Your total earnings of',
                    'Total_Income' : '$' + str(round(self.player.Total_Earnings,2)),
                    'Statement_B2' : 'are',
                    'Total_Comparison' : 'equal to',
                    'Statement_B3' : 'the accumulative constant earnings of $500',
                    'Total_Difference' : ''
                }
            # Case where player wins on chance for generated value and also wins on their total earnings.
            elif ((generated_value < 100) and (self.player.Total_Earnings > 500)) :
                return {
                    'Inform' : 'You Have Chosen A Fixed Amount Of $100.',
                    'Statement_A1' : 'Your drawed amount of',
                    'Random_Number' : '$' + str(generated_value),
                    'Statement_A2' : 'would have been', 
                    'Comparison' : 'less than',
                    'Statement_A3' : 'the constant amount of $100 by',
                    'Difference' : '$' + str(round(difference, 2)),
                    'Statement_B1' : 'Your total earnings of',
                    'Total_Income' : '$' + str(round(self.player.Total_Earnings,2)),
                    'Statement_B2' : 'are',
                    'Total_Comparison' : 'greater than',
                    'Statement_B3' : 'the accumulative constant earnings of $500 by',
                    'Total_Difference' : '$' + str(round(total_difference, 2))
                }
            # Case where player wins on chance for generated value but loses on their total earnings.
            elif ((generated_value < 100) and (self.player.Total_Earnings < 500)) :
                return {
                    'Inform' : 'You Have Chosen A Fixed Amount Of $100.',
                    'Statement_A1' : 'Your drawed amount of',
                    'Random_Number' : '$' + str(generated_value),
                    'Statement_A2' : 'would have been', 
                    'Comparison' : 'less than',
                    'Statement_A3' : 'the constant amount of $100 by',
                    'Difference' : '$' + str(round(difference, 2)),
                    'Statement_B1' : 'Your total earnings of',
                    'Total_Income' : '$' + str(round(self.player.Total_Earnings,2)),
                    'Statement_B2' : 'are',
                    'Total_Comparison' : 'less than',
                    'Statement_B3' : 'the accumulative constant earnings of $500 by',
                    'Total_Difference' : '$' + str(round(total_difference, 2))
                }
            # Case where player wins on chance for generated value and the total earnings are $500.
            elif ((generated_value < 100) and (self.player.Total_Earnings == 500)) :
                return {
                    'Inform' : 'You Have Chosen A Fixed Amount Of $100.',
                    'Statement_A1' : 'Your drawed amount of',
                    'Random_Number' : '$' + str(generated_value),
                    'Statement_A2' : 'would have been', 
                    'Comparison' : 'less than',
                    'Statement_A3' : 'the constant amount of $100 by',
                    'Difference' : '$' + str(round(difference, 2)),
                    'Statement_B1' : 'Your total earnings of',
                    'Total_Income' : '$' + str(round(self.player.Total_Earnings,2)),
                    'Statement_B2' : 'are',
                    'Total_Comparison' : 'equal to',
                    'Statement_B3' : 'the accumulative constant earnings of $500',
                    'Total_Difference' : ''
                }
            # Case where the generated value would have been $100 but the player wins on their total earnings.
            elif ((generated_value == 100) and (self.player.Total_Earnings > 500)) :
                return {
                    'Inform' : 'You Have Chosen A Fixed Amount Of $100.',
                    'Statement_A1' : 'Your drawed amount of',
                    'Random_Number' : '$' + str(generated_value),
                    'Statement_A2' : 'would have been', 
                    'Comparison' : 'equal to',
                    'Statement_A3' : 'the constant amount of $100',
                    'Difference' : '',
                    'Statement_B1' : 'Your total earnings of',
                    'Total_Income' : '$' + str(round(self.player.Total_Earnings,2)),
                    'Statement_B2' : 'are',
                    'Total_Comparison' : 'greater than',
                    'Statement_B3' : 'the accumulative constant earnings of $500 by',
                    'Total_Difference' : '$' + str(round(total_difference, 2))
                }
            # Case where the generated value would have been $100 but the player loses on their total earnings.
            elif ((generated_value == 100) and (self.player.Total_Earnings < 500)) :
                return {
                    'Inform' : 'You Have Chosen A Fixed Amount Of $100.',
                    'Statement_A1' : 'Your drawed amount of',
                    'Random_Number' : '$' + str(generated_value),
                    'Statement_A2' : 'would have been', 
                    'Comparison' : 'equal to',
                    'Statement_A3' : 'the constant amount of $100',
                    'Difference' : '',
                    'Statement_B1' : 'Your total earnings of',
                    'Total_Income' : '$' + str(round(self.player.Total_Earnings,2)),
                    'Statement_B2' : 'are',
                    'Total_Comparison' : 'less than',
                    'Statement_B3' : 'the accumulative constant earnings of $500 by',
                    'Total_Difference' : '$' + str(round(total_difference, 2))
                }
            # Case where the generated value would have been $100 and the total earnings are $500.
            elif ((generated_value == 100) and (self.player.Total_Earnings == 500)) :
                return {
                    'Inform' : 'You Have Chosen A Fixed Amount Of $100.',
                    'Statement_A1' : 'Your drawed amount of',
                    'Random_Number' : '$' + str(generated_value),
                    'Statement_A2' : 'would have been', 
                    'Comparison' : 'equal to',
                    'Statement_A3' : 'the constant amount of $100',
                    'Difference' : '',
                    'Statement_B1' : 'Your total earnings of',
                    'Total_Income' : '$' + str(round(self.player.Total_Earnings,2)),
                    'Statement_B2' : 'are',
                    'Total_Comparison' : 'equal to',
                    'Statement_B3' : 'the accumulative constant earnings of $500',
                    'Total_Difference' : ''
                }
        elif (self.player.Decision_5 == Constants.random_amount) :
            # Case where player chooses generated value.
            self.player.Total_Earnings = self.player.Previous_Earnings + generated_value
            total_difference = abs(self.player.Total_Earnings - 500)
            # Case where player wins on chance for generated value and also wins on their total earnings.
            if ((generated_value > 100) and (self.player.Total_Earnings > 500)) :
                return {
                    'Inform' : 'You Have Chosen A Random Amount Instead Of The Constant Amount Of $100.',
                    'Statement_A1' : 'Your drawed amount of',
                    'Random_Number' : '$' + str(generated_value),
                    'Statement_A2' : 'is', 
                    'Comparison' : 'greater than',
                    'Statement_A3' : 'the constant amount of $100 by',
                    'Difference' : '$' + str(round(difference, 2)),
                    'Statement_B1' : 'Your total earnings of',
                    'Total_Income' : '$' + str(round(self.player.Total_Earnings,2)),
                    'Statement_B2' : 'are',
                    'Total_Comparison' : 'greater than',
                    'Statement_B3' : 'the accumulative constant earnings of $500 by',
                    'Total_Difference' : '$' + str(round(total_difference, 2))
                }
            # Case where player wins on chance for generated value but loses on their total earnings.
            elif ((generated_value > 100) and (self.player.Total_Earnings < 500)) :
                return {
                    'Inform' : 'You Have Chosen A Random Amount Instead Of The Constant Amount Of $100.',
                    'Statement_A1' : 'Your drawed amount of',
                    'Random_Number' : '$' + str(generated_value),
                    'Statement_A2' : 'is', 
                    'Comparison' : 'greater than',
                    'Statement_A3' : 'the constant amount of $100 by',
                    'Difference' : '$' + str(round(difference, 2)),
                    'Statement_B1' : 'Your total earnings of',
                    'Total_Income' : '$' + str(round(self.player.Total_Earnings,2)),
                    'Statement_B2' : 'are',
                    'Total_Comparison' : 'less than',
                    'Statement_B3' : 'the accumulative constant earnings of $500 by',
                    'Total_Difference' : '$' + str(round(total_difference, 2))
                }
            # Case where player wins on chance for generated value and the total earnings are $500.
            elif ((generated_value > 100) and (self.player.Total_Earnings == 500)) :
                return {
                    'Inform' : 'You Have Chosen A Random Amount Instead Of The Constant Amount Of $100.',
                    'Statement_A1' : 'Your drawed amount of',
                    'Random_Number' : '$' + str(generated_value),
                    'Statement_A2' : 'is', 
                    'Comparison' : 'greater than',
                    'Statement_A3' : 'the constant amount of $100 by',
                    'Difference' : '$' + str(round(difference, 2)),
                    'Statement_B1' : 'Your total earnings of',
                    'Total_Income' : '$' + str(round(self.player.Total_Earnings,2)),
                    'Statement_B2' : 'are',
                    'Total_Comparison' : 'equal to',
                    'Statement_B3' : 'the accumulative constant earnings of $500',
                    'Total_Difference' : ''
                }
            # Case where player loses on chance for generated value but wins on their total earnings.
            elif ((generated_value < 100) and (self.player.Total_Earnings > 500)) :
                return {
                    'Inform' : 'You Have Chosen A Random Amount Instead Of The Constant Amount Of $100.',
                    'Statement_A1' : 'Your drawed amount of',
                    'Random_Number' : '$' + str(generated_value),
                    'Statement_A2' : 'is', 
                    'Comparison' : 'less than',
                    'Statement_A3' : 'the constant amount of $100 by',
                    'Difference' : '$' + str(round(difference, 2)),
                    'Statement_B1' : 'Your total earnings of',
                    'Total_Income' : '$' + str(round(self.player.Total_Earnings,2)),
                    'Statement_B2' : 'are',
                    'Total_Comparison' : 'greater than',
                    'Statement_B3' : 'the accumulative constant earnings of $500 by',
                    'Total_Difference' : '$' + str(round(total_difference, 2))
                }
            # Case where player loses on chance for generated value but loses on their total earnings.
            elif ((generated_value < 100) and (self.player.Total_Earnings < 500)) :
                return {
                    'Inform' : 'You Have Chosen A Random Amount Instead Of The Constant Amount Of $100.',
                    'Statement_A1' : 'Your drawed amount of',
                    'Random_Number' : '$' + str(generated_value),
                    'Statement_A2' : 'is', 
                    'Comparison' : 'less than',
                    'Statement_A3' : 'the constant amount of $100 by',
                    'Difference' : '$' + str(round(difference, 2)),
                    'Statement_B1' : 'Your total earnings of',
                    'Total_Income' : '$' + str(round(self.player.Total_Earnings,2)),
                    'Statement_B2' : 'are',
                    'Total_Comparison' : 'less than',
                    'Statement_B3' : 'the accumulative constant earnings of $500 by',
                    'Total_Difference' : '$' + str(round(total_difference, 2))
                }
            # Case where player loses on chance for generated value and the total earnings are $500.
            elif ((generated_value < 100) and (self.player.Total_Earnings == 500)) :
                return {
                    'Inform' : 'You Have Chosen A Random Amount Instead Of The Constant Amount Of $100.',
                    'Statement_A1' : 'Your drawed amount of',
                    'Random_Number' : '$' + str(generated_value),
                    'Statement_A2' : 'is', 
                    'Comparison' : 'less than',
                    'Statement_A3' : 'the constant amount of $100 by',
                    'Difference' : '$' + str(round(difference, 2)),
                    'Statement_B1' : 'Your total earnings of',
                    'Total_Income' : '$' + str(round(self.player.Total_Earnings,2)),
                    'Statement_B2' : 'are',
                    'Total_Comparison' : 'equal to',
                    'Statement_B3' : 'the accumulative constant earnings of $500',
                    'Total_Difference' : ''
                }
            # Case where the generated value is $100 but the player wins on their total earnings.
            elif ((generated_value == 100) and (self.player.Total_Earnings > 500)) :
                return {
                    'Inform' : 'You Have Chosen A Random Amount Instead Of The Constant Amount Of $100.',
                    'Statement_1.1' : 'Your drawed amount of',
                    'Random_Number' : '$' + str(generated_value),
                    'Statement_1.2' : 'is',  
                    'Comparison' : 'equal to',
                    'Statement_1.3' : 'the constant amount of $100',
                    'Difference' : '',
                    'Statement_2.1' : 'Your total earnings of',
                    'Total_Income' : '$' + str(round(self.player.Total_Earnings,2)),
                    'Statement_2.2' : 'are',
                    'Total_Comparison' : 'greater than',
                    'Statement_2.3' : 'the accumulative constant earnings of $500 by',
                    'Total_Difference' : '$' + str(round(total_difference, 2))
                }
            # Case where the generated value is $100 but the player loses on their total earnings.
            elif ((generated_value == 100) and (self.player.Total_Earnings < 500)) :
                return {
                    'Inform' : 'You Have Chosen A Random Amount Instead Of The Constant Amount Of $100.',
                    'Statement_1.1' : 'Your drawed amount of',
                    'Random_Number' : '$' + str(generated_value),
                    'Statement_1.2' : 'is', 
                    'Comparison' : 'equal to',
                    'Statement_1.3' : 'the constant amount of $100',
                    'Difference' : '',
                    'Statement_2.1' : 'Your total earnings of',
                    'Total_Income' : '$' + str(round(self.player.Total_Earnings,2)),
                    'Statement_2.2' : 'are',
                    'Total_Comparison' : 'less than',
                    'Statement_2.3' : 'the accumulative constant earnings of $500 by',
                    'Total_Difference' : '$' + str(round(total_difference, 2))
                }
            # Case where the generated value is $100 and the total earnings are $500.
            elif ((generated_value == 100) and (self.player.Total_Earnings == 500)) :
                return {
                    'Inform' : 'You Have Chosen A Random Amount Instead Of The Constant Amount Of $100.',
                    'Statement_1.1' : 'Your drawed amount of',
                    'Random_Number' : '$' + str(generated_value),
                    'Statement_1.2' : 'is', 
                    'Comparison' : 'equal to',
                    'Statement_1.3' : 'the constant amount of $100',
                    'Difference' : '',
                    'Statement_2.1' : 'Your total earnings of',
                    'Total_Income' : '$' + str(round(self.player.Total_Earnings,2)),
                    'Statement_2.2' : 'are',
                    'Total_Comparison' : 'equal to',
                    'Statement_2.3' : 'the accumulative constant earnings of $500',
                    'Total_Difference' : ''
                }

class Appreciation(Page) :
    form_model = 'player'

# This list contains .html filenames which are accessed in the expected sequence. 
page_sequence = [
    Introduction, 
    Instruction,
    Input_Quadratic,
    Input_Investment,
    Results_Quadratic,
    Results_Investment,
    Questionnaire_COVID_1,
    Results_Questionnaire_COVID_1,
    Questionnaire_COVID_2,
    Results_Questionnaire_COVID_2,
    Questionnaire_COVID_3,
    Results_Questionnaire_COVID_3,
    Questionnaire_COVID_4,
    Results_Questionnaire_COVID_4,
    Questionnaire_COVID_5,
    Results_Questionnaire_COVID_5,
    Appreciation
]
