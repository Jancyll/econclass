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
    ENDOWMENT = 20
    # MULTIPLIER = 1.8
    MULTIPLIER = 1.6

class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    total_contribution = models.CurrencyField()
    individual_share = models.CurrencyField()


class Player(BasePlayer):
    contribution = models.CurrencyField(
        min=0, max=C.ENDOWMENT, label="How much will you contribute to the group account?"
    )
    earnings = models.IntegerField()
    total_earnings = models.IntegerField()

#FUNCTIONS

def set_payoffs(group: Group):
    players = group.get_players()
    print('this is the list of players:', players)

    # contributions = [p.contribution for p in players] # it creates one list for iteration
    # print('this is the list of contributions:', contributions)
    # group.total_contribution = sum(contributions)

    group.total_contribution = 0
    for p in players:
        group.total_contribution += group.total_contribution + p.contribution

    group.individual_share = group.total_contribution * C.MULTIPLIER / C.PLAYERS_PER_GROUP

    for p in players:
        p.payoff = C.ENDOWMENT - p.contribution + group.individual_share

    # for p in players:
    #     p.remain = C.ENDOWMENT - p.contribution

# group randomly
def creating_session(subsession):
    subsession.group_randomly()
    print(subsession.get_group_matrix())

# PAGES
class MyPage(Page):
    form_model = 'player'
    form_fields = ['contribution']


class ResultsWaitPage(WaitPage):
    after_all_players_arrive = set_payoffs

# shuffling during the session
class ShuffleWaitPage(WaitPage):

    wait_for_all_groups = True

    @staticmethod
    def after_all_players_arrive(subsession):
        subsession.group_randomly()


class Results(Page):
    pass


page_sequence = [MyPage, ResultsWaitPage, Results]
