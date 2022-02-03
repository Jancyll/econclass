from otree.api import *


doc = """
A public good game:
1. Group size is larger than 1.
2. Several rounds (i.e., more than 2). 
3. Change the MPCR partway through the rounds.
4. Subjects’ aggregate earnings are always displayed on the screen.
5. Display any other information you deem appropriate.
"""


class C(BaseConstants):
    NAME_IN_URL = 'public_goods_hw'
    PLAYERS_PER_GROUP = 4
    NUM_ROUNDS = 3
    # ENDOWMENT = cu(100)
    ENDOWMENT = 100
    # MULTIPLIER = 1.8
    MPCR1 = 0.4
    MPCR2 = 0.6

class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    earnings = models.IntegerField()
    total_earnings = models.IntegerField()

#FUNCTIONS

def creating_session(subsession):
    print("in creating session")


# PAGES
class MyPage(Page):
    pass


class ResultsWaitPage(WaitPage):
    pass


class Results(Page):
    pass


page_sequence = [MyPage, ResultsWaitPage, Results]
