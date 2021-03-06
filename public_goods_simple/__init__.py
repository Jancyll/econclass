from otree.api import *



class C(BaseConstants):
    NAME_IN_URL = 'public_goods_simple'
    PLAYERS_PER_GROUP = 3
    NUM_ROUNDS = 1
    ENDOWMENT = cu(100)
    MULTIPLIER = 1.8


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    total_contribution = models.CurrencyField()
    individual_share = models.CurrencyField()


class Player(BasePlayer):
    contribution = models.CurrencyField(
        min=0, max=C.ENDOWMENT, label="How much will you contribute?"
    )


# FUNCTIONS
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


# PAGES
# choose model --> line 22; fields is decided under the model
class Contribute(Page):
    form_model = 'player'
    form_fields = ['contribution']


class ResultsWaitPage(WaitPage):
    after_all_players_arrive = set_payoffs

# no input needed, so just Pass
class Results(Page):
    pass

# show the sequence of the page
page_sequence = [Contribute, ResultsWaitPage, Results]
