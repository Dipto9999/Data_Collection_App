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
Collects User Information to Make Mathematical Decisions
"""

#####################################
# Define Constants with Values that Won't Change.
class Constants(BaseConstants):
    name_in_url = 'workshop_app'
    players_per_group = None
    num_rounds = 1
    round_1 = 1
    name_developer = "Muntakim Rahman"

#####################################
# No Subsession in Between Apps. Will be Unattended.
class Subsession(BaseSubsession):
    pass
#####################################
# Not a Group App. Concerns an Individual Making a Decision.
class Group(BaseGroup):
    pass

#####################################
# Input that Influences Decision Making.
class Player(BasePlayer):
    Name_Initials_Consent = models.StringField()
    # Not Required to Be Provided by Individual
    Email_Consent = models.StringField(blank = True)
    Contact_Consent = models.StringField()

