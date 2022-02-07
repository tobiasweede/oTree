from otree.api import *


doc = """
My public goods
"""


class C(BaseConstants):
    NAME_IN_URL = 'my_public_goods'
    NUM_ROUNDS = 1
    PLAYERS_PER_GROUP = 3
    ENDOWMENT = cu(1000)
    MULTIPLIER = 2


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    total_contribution = models.CurrencyField()
    individual_share = models.CurrencyField()


class Player(BasePlayer):
    contribution = models.CurrencyField(
        min=0,
        max=C.ENDOWMENT,
        label='How much will you contribute?'
    )
    
def set_payoffs(group: Group):
    players = group.get_players()
    contributions = [p.contribution for p in players]
    group.total_contribution = sum(contributions)
    group.individual_share = group.total_contribution * C.MULTIPLIER / C.PLAYERS_PER_GROUP
    for player in players:
        player.payoff = C.ENDOWMENT - player.contribution + group.individual_share


# PAGES
class Contribute(Page):
    form_model = 'player'
    form_fields = ['contribution']


class ResultsWaitPage(WaitPage):
    after_all_players_arrive = 'set_payoffs'


class Results(Page):
    pass


page_sequence = [Contribute, ResultsWaitPage, Results]
