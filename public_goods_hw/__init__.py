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
    NUM_ROUNDS = 1
    # ENDOWMENT = cu(100)
    ENDOWMENT = 20
    # MULTIPLIER = 1.8
    MULTIPLIER = 1.6


class Subsession(BaseSubsession):
    sum_contribution = models.IntegerField(initial=0)
    s1_sum_contribution = models.IntegerField(initial=0)
    s2_run1_sum_contribution = models.IntegerField(initial=0)
    mean_contribution = models.FloatField()
    s1_mean_contribution = models.FloatField()
    s2_run1_mean_contribution = models.FloatField()
    s2r2_sum_contribution = models.IntegerField(initial=0)
    s2r2_mean_contribution = models.FloatField()


class Group(BaseGroup):
    total_contribution = models.IntegerField()
    individual_share = models.FloatField()
    s1_total_contribution = models.IntegerField()
    s1_individual_share = models.FloatField()
    s2_run1_total_contribution = models.IntegerField()
    s2_run1_individual_share = models.FloatField()
    s2r2_total_contribution = models.IntegerField()
    s2r2_individual_share = models.FloatField()
    s2r3_total_contribution = models.IntegerField()
    s2r3_individual_share = models.FloatField()


class Player(BasePlayer):
    # unconditional contribution
    unconditional_contribution = models.IntegerField(
        min=0, max=C.ENDOWMENT, label='Your unconditional contribution to the project',
    )
    # conditional contribution
    c_contribution_0 = models.IntegerField(min=0, max=C.ENDOWMENT, label='0')
    c_contribution_1 = models.IntegerField(min=0, max=C.ENDOWMENT, label='1')
    c_contribution_2 = models.IntegerField(min=0, max=C.ENDOWMENT, label='2')
    c_contribution_3 = models.IntegerField(min=0, max=C.ENDOWMENT, label='3')
    c_contribution_4 = models.IntegerField(min=0, max=C.ENDOWMENT, label='4')
    c_contribution_5 = models.IntegerField(min=0, max=C.ENDOWMENT, label='5')
    c_contribution_6 = models.IntegerField(min=0, max=C.ENDOWMENT, label='6')
    c_contribution_7 = models.IntegerField(min=0, max=C.ENDOWMENT, label='7')
    c_contribution_8 = models.IntegerField(min=0, max=C.ENDOWMENT, label='8')
    c_contribution_9 = models.IntegerField(min=0, max=C.ENDOWMENT, label='9')
    c_contribution_10 = models.IntegerField(min=0, max=C.ENDOWMENT, label='10')
    c_contribution_11 = models.IntegerField(min=0, max=C.ENDOWMENT, label='11')
    c_contribution_12 = models.IntegerField(min=0, max=C.ENDOWMENT, label='12')
    c_contribution_13 = models.IntegerField(min=0, max=C.ENDOWMENT, label='13')
    c_contribution_14 = models.IntegerField(min=0, max=C.ENDOWMENT, label='14')
    c_contribution_15 = models.IntegerField(min=0, max=C.ENDOWMENT, label='15')
    c_contribution_16 = models.IntegerField(min=0, max=C.ENDOWMENT, label='16')
    c_contribution_17 = models.IntegerField(min=0, max=C.ENDOWMENT, label='17')
    c_contribution_18 = models.IntegerField(min=0, max=C.ENDOWMENT, label='18')
    c_contribution_19 = models.IntegerField(min=0, max=C.ENDOWMENT, label='19')
    c_contribution_20 = models.IntegerField(min=0, max=C.ENDOWMENT, label='20')

    # conditional_contribution_6 = models.IntegerField(
    #     min=0, max=C.ENDOWMENT, label='6',
    # )
    # control question
    control_1 = models.IntegerField(
        min=0,
        label='What is your income if you contribute 0 tokens?',
    )
    control_2 = models.IntegerField(
        min=0,
        label='What is your income if you contribute 20 tokens?',
    )
    control_3 = models.IntegerField(
        min=0,
        label='What is your income if you contribute 0 tokens?',
    )
    control_4 = models.IntegerField(
        min=0,
        label='What is your income if the total contribution to the project (including yours) is 12 tokens?',
    )
    control_5 = models.IntegerField(
        min=0,
        label='What is your income if the total contribution to the project (including yours) is 48 tokens?',
    )
    control_6 = models.IntegerField(
        min=0,
        label='What is your income if you contribute 20 tokens?',
    )
    age = models.IntegerField(label='What is your age?', min=13, max=125)
    gender = models.StringField(
        choices=[['Male', 'Male'], ['Female', 'Female']],
        label='What is your gender?',
        widget=widgets.RadioSelect,
    )
    # session 2 contribution
    s2_contribution_3 = models.IntegerField(
        min=0, max=C.ENDOWMENT, label="How much will you contribute to the project?"
    )
    s2r2_contribution = models.IntegerField(
        min=0, max=C.ENDOWMENT, label="How much will you contribute to the project?"
    )
    s2r3_contribution = models.IntegerField(
        min=0, max=C.ENDOWMENT, label="How much will you contribute to the project?"
    )
    contribution = models.IntegerField(
        min=0, max=C.ENDOWMENT, label="How much will you contribute to the group account?"
    )
    earnings = models.IntegerField()
    total_earnings = models.IntegerField()
    s1_payoff = models.CurrencyField()
    s2_run1_payoff = models.CurrencyField()
    s2r2_payoff = models.CurrencyField()
    s2r3_payoff = models.CurrencyField()
    # status = models.IntegerField()

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

# FUNCTIONS

def session1_payoffs(subsession: Subsession):
    for group in subsession.get_groups():

        players = group.get_players()
        print('this is the list of players:', players)

        contributions = [p.unconditional_contribution for p in players] # it creates one list for iteration
        print('this is the list of contributions:', contributions)
        group.s1_total_contribution = sum(contributions)
        print('this is the group contributions:', group.s1_total_contribution)

        # group.s1_total_contribution = 0
        # for p in players:
        #     group.s1_total_contribution += group.s1_total_contribution + p.unconditional_contribution

        group.s1_individual_share = group.s1_total_contribution * C.MULTIPLIER / C.PLAYERS_PER_GROUP

        for p in players:
            p.payoff = C.ENDOWMENT - p.unconditional_contribution + group.s1_individual_share
            p.s1_payoff = p.payoff

    for g in subsession.get_groups():
        subsession.s1_sum_contribution += g.s1_total_contribution
        subsession.s1_mean_contribution = subsession.s1_sum_contribution/8
    # for g in subsession.get_groups():
    #     subsession.sum_contribution += g.total_contribution

# def session1_payoffs(group: Group):
#     players = group.get_players()
#     print('this is the list of players:', players)
#
#     # contributions = [p.contribution for p in players] # it creates one list for iteration
#     # print('this is the list of contributions:', contributions)
#     # group.total_contribution = sum(contributions)
#
#     group.s1_total_contribution = 0
#     for p in players:
#         group.s1_total_contribution += group.s1_total_contribution + p.unconditional_contribution
#
#
#     group.s1_individual_share = group.s1_total_contribution * C.MULTIPLIER / C.PLAYERS_PER_GROUP
#
#     for p in players:
#         p.s1_payoff = C.ENDOWMENT - p.unconditional_contribution + group.s1_individual_share


def session2_run1_payoffs(subsession: Subsession):
    for group in subsession.get_groups():

        players = group.get_players()
        print('this is the list of players:', players)

        contributions = [p.s2_contribution_3 for p in players] # it creates one list for iteration
        print('this is the list of contributions:', contributions)
        group.s2_run1_total_contribution = sum(contributions)
        print('this is the group contributions:', group.s2_run1_total_contribution)

        # group.s2_run1_total_contribution = 0
        # for p in players:
        #     group.s2_run1_total_contribution += group.s2_run1_total_contribution + p.s2_contribution_3

        group.s2_run1_individual_share = group.s2_run1_total_contribution * C.MULTIPLIER / C.PLAYERS_PER_GROUP

        for p in players:
            p.payoff = C.ENDOWMENT - p.s2_contribution_3 + group.s2_run1_individual_share
            p.s2_run1_payoff = p.payoff

    for g in subsession.get_groups():
        subsession.s2_run1_sum_contribution += g.s2_run1_total_contribution
        subsession.s2_run1_mean_contribution = subsession.s2_run1_sum_contribution/8

def s2rs_payoffs(subsession: Subsession):
    for group in subsession.get_groups():

        players = group.get_players()
        print('this is the list of players:', players)

        contributions = [p.s2r2_contribution for p in players] # it creates one list for iteration
        print('this is the list of contributions:', contributions)
        group.s2r2_total_contribution = sum(contributions)
        print('this is the group contributions:', group.s2r2_total_contribution)

        # group.s2r2_total_contribution = 0
        # for p in players:
        #     group.s2r2_total_contribution += group.s2r2_total_contribution + p.s2r2_contribution

        group.s2r2_individual_share = group.s2r2_total_contribution * C.MULTIPLIER / C.PLAYERS_PER_GROUP

        for p in players:
            p.payoff = C.ENDOWMENT - p.s2r2_contribution + group.s2r2_individual_share
            p.s2r2_payoff = p.payoff

    # for g in subsession.get_groups():
    #     subsession.s2r2_sum_contribution += g.s2r2_individual_share
    #     subsession.s2r2_mean_contribution = subsession.s2r2_sum_contribution/8

def s2r3_payoffs(subsession: Subsession):
    for group in subsession.get_groups():

        players = group.get_players()
        print('this is the list of players:', players)

        contributions = [p.s2r3_contribution for p in players] # it creates one list for iteration
        print('this is the list of contributions:', contributions)
        group.s2r3_total_contribution = sum(contributions)
        print('this is the group contributions:', group.s2r3_total_contribution)

        # group.s2r3_total_contribution = 0
        # for p in players:
        #     group.s2r3_total_contribution += group.s2r3_total_contribution + p.s2r2_contribution

        group.s2r3_individual_share = group.s2r3_total_contribution * C.MULTIPLIER / C.PLAYERS_PER_GROUP

        for p in players:
            p.payoff = C.ENDOWMENT - p.s2r2_contribution + group.s2r3_individual_share
            p.s2r3_payoff = p.payoff

# group randomly
def creating_session(subsession):
    subsession.group_randomly()
    print(subsession.get_group_matrix())

# session 1 random payoff

# PAGES
# class MyPage(Page):
#     form_model = 'player'
#     form_fields = ['contribution']
#
#     def vars_for_template(player):
#         v = -1
#         print(player.subsession.round_number)
#         if player.subsession.round_number > 1:
#             s = player.subsession.in_round(player.subsession.round_number-1)
#             v = s.sum_contribution
#
#         return dict(
#             sum_contribution = v
#         )


class treatment1(Page):
    pass
    # form_model = 'player'
    # form_fields = ['unconditional_contribution']

    # def vars_for_template(player):
    #     v = 0
    #     print(player.subsession.round_number)
    #     if player.subsession.round_number > 1:
    #         s = player.subsession.in_round(player.subsession.round_number)
    #         print('this is ' + s)
    #         v = s.s1_mean_contribution
    #
    #     return dict(
    #         s1_mean_contribution = v
    #     )

class Control_question(Page):
    form_model = 'player'
    form_fields = ['control_1', 'control_2', 'control_3', 'control_4', 'control_5', 'control_6']

class Contribution_1(Page):
    form_model = 'player'
    form_fields = ['unconditional_contribution']

class Contribution_2(Page):
    form_model = 'player'
    form_fields = ['c_contribution_0', 'c_contribution_1', 'c_contribution_2', 'c_contribution_3', 'c_contribution_4', 'c_contribution_5',
                   'c_contribution_6', 'c_contribution_7', 'c_contribution_8', 'c_contribution_9', 'c_contribution_10', 'c_contribution_11',
                   'c_contribution_12', 'c_contribution_13', 'c_contribution_14', 'c_contribution_15', 'c_contribution_16', 'c_contribution_17',
                   'c_contribution_18', 'c_contribution_19', 'c_contribution_20']


class Contribution_3(Page):
    form_model = 'player'
    form_fields = ['s2_contribution_3']

class Contribution_4(Page):
    form_model = 'player'
    form_fields = ['s2r2_contribution']

class Contribution_5(Page):
    form_model = 'player'
    form_fields = ['s2r3_contribution']


# class Demographics(Page):
#     form_model = 'player'
#     form_fields = ['age', 'gender']

# class Results1(Page):
#     form_model = 'player'
#     def vars_for_template(player: Player):
#         import random
#         chosen_player = random.choice(player.id_in_group)

class s1_ResultsWaitPage(WaitPage):
    wait_for_all_groups = True
    after_all_players_arrive = session1_payoffs

class s2_run1_ResultsWaitPage(WaitPage):
    wait_for_all_groups = True
    after_all_players_arrive = session2_run1_payoffs

class s2r2_ResultsWaitPage(WaitPage):
    wait_for_all_groups = True
    after_all_players_arrive = s2rs_payoffs

class s2r3_ResultsWaitPage(WaitPage):
    wait_for_all_groups = True
    after_all_players_arrive = s2r3_payoffs

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

class Introduction1(Page):
    pass

class Instruction2(Page):
    pass

class Results1(Page):
    pass

class Results2(Page):
    pass

class Results_s2rs(Page):
    pass

class Results_s2r3(Page):
    pass

class paymentinfo(Page):
    @staticmethod
    def vars_for_template(player: Player):
        return dict(total_earnings=(player.s1_payoff + player.s2_run1_payoff + player.s2r2_payoff + player.s2r3_payoff) * 0.15,
                    earnings= player.s2_run1_payoff + player.s2r2_payoff + player.s2r3_payoff)

class treatment2(Page):
    pass

class treatment3(Page):
    pass

page_sequence = [Introduction, Control_question, Introduction1, Contribution_1, Contribution_2, s1_ResultsWaitPage, Results1,
                 Instruction2,
                 treatment1, Contribution_3, s2_run1_ResultsWaitPage, Results2,
                 treatment2, Contribution_4, s2r2_ResultsWaitPage, Results_s2rs,
                 treatment3, Contribution_5, s2r3_ResultsWaitPage, Results_s2r3,
                 paymentinfo]
