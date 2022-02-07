from otree.api import *


doc = """
My simple survey
"""


class C(BaseConstants):
    NAME_IN_URL = 'my_simple_survey'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    name = models.StringField()
    age = models.IntegerField()

# PAGES


class MyPage(Page):
    form_model = 'player'
    form_fields = ['name', 'age']


class Results(Page):
    pass


page_sequence = [
    MyPage,
    Results
]
