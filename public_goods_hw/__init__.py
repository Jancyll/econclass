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
    PLAYERS_PER_GROUP = 3
    NUM_ROUNDS = 3
    # ENDOWMENT = cu(100)
    ENDOWMENT = 20
    # MULTIPLIER = 1.8
    MULTIPLIER = 1.6


class Subsession(BaseSubsession):
    sum_contribution = models.IntegerField(
        initial=0
    )
    mean_contribution = models.FloatField()


class Group(BaseGroup):
    total_contribution = models.IntegerField()
    individual_share = models.FloatField()


class Player(BasePlayer):
    # unconditional contribution
    unconditional_contribution = models.IntegerField(
        min=0, max=C.ENDOWMENT, label='Your unconditional contribution to the group account',
    )
    # conditional contribution
    c_contribution_0 = models.IntegerField(
        min=0, max=C.ENDOWMENT, label='0',
    )
    c_contribution_1 = models.IntegerField(
        min=0, max=C.ENDOWMENT, label='1',
    )
    c_contribution_2 = models.IntegerField(
        min=0, max=C.ENDOWMENT, label='2',
    )
    c_contribution_3 = models.IntegerField(
        min=0, max=C.ENDOWMENT, label='3',
    )
    c_contribution_4 = models.IntegerField(
        min=0, max=C.ENDOWMENT, label='4',
    )
    c_contribution_5 = models.IntegerField(
        min=0, max=C.ENDOWMENT, label='5',
    )
    # conditional_contribution_6 = models.IntegerField(
    #     min=0, max=C.ENDOWMENT, label='6',
    # )
    age = models.IntegerField(label='What is your age?', min=13, max=125)
    gender = models.StringField(
        choices=[['Male', 'Male'], ['Female', 'Female']],
        label='What is your gender?',
        widget=widgets.RadioSelect,
    )
    contribution = models.IntegerField(
        min=0, max=C.ENDOWMENT, label="How much will you contribute to the group account?"
    )
    earnings = models.IntegerField()
    total_earnings = models.IntegerField()

#FUNCTIONS

def set_payoffs(subsession: Subsession):
    for group in subsession.get_groups():

        players = group.get_players()
        print('this is the list of players:', players)

        contributions = [p.contribution for p in players] # it creates one list for iteration
        print('this is the list of contributions:', contributions)
        group.total_contribution = sum(contributions)
        print('this is the group contributions:', group.total_contribution)

        # group.total_contribution = 0
        # for p in players:
        #     group.total_contribution += group.total_contribution + p.contribution

        group.individual_share = group.total_contribution * C.MULTIPLIER / C.PLAYERS_PER_GROUP

        for p in players:
            p.payoff = C.ENDOWMENT - p.contribution + group.individual_share

    for g in subsession.get_groups():
        subsession.sum_contribution += g.total_contribution


# group randomly
def creating_session(subsession):
    subsession.group_randomly()
    print(subsession.get_group_matrix())

# PAGES
class MyPage(Page):
    form_model = 'player'
    form_fields = ['contribution']

    def vars_for_template(player):
        v = -1
        print(player.subsession.round_number)
        if player.subsession.round_number > 1:
            s = player.subsession.in_round(player.subsession.round_number-1)
            v = s.sum_contribution

        return dict(
            sum_contribution = v
        )

class Contribution_1(Page):
    form_model = 'player'
    form_fields = ['unconditional_contribution']

class Contribution_2(Page):
    form_model = 'player'
    form_fields = ['c_contribution_0', 'c_contribution_1', 'c_contribution_2', 'c_contribution_3', 'c_contribution_4', 'c_contribution_5']


class Demographics(Page):
    form_model = 'player'
    form_fields = ['age', 'gender']

class ResultsWaitPage(WaitPage):
    wait_for_all_groups = True
    after_all_players_arrive = set_payoffs

# shuffling during the session
class ShuffleWaitPage(WaitPage):

    wait_for_all_groups = True

    @staticmethod
    def after_all_players_arrive(subsession):
        subsession.group_randomly()


class Results(Page):
    pass

class Introduction(Page):
    pass


page_sequence = [Introduction, Contribution_1, Contribution_2, MyPage, ResultsWaitPage, Results]
