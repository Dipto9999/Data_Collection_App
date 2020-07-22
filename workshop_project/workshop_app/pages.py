# Keep Track of How Pages are Accessed.

from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

# First Page
class Introduction(Page):
    form_model = 'player'
    # List Contains variables from class Player in pages.py
    form_fields = ['Name_Initials_Consent', 'Email_Consent', 'Contact_Consent'] 


class ResultsWaitPage(WaitPage):
    pass


class Results(Page):
    pass

# List Contains .html filename Which is Accessed. 
page_sequence = [Introduction]
