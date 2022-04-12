from os import environ


SESSION_CONFIGS = [
    dict(
        name='guess_two_thirds',
        display_name="Guess 2/3 of the Average",
        app_sequence=['guess_two_thirds', 'payment_info'],
        num_demo_participants=3,
    ),
    dict(
        name='survey', app_sequence=['survey', 'payment_info'], num_demo_participants=1
    ),
    dict(
        name='Public_Goods_Game_Demo',
        display_name="Public goods game with norms",
        app_sequence=['public_goods_hw'],
        num_demo_participants=3,
    ),
    dict(
        name='Public_Goods_Game',
        display_name="This is a simple public goods game in otree",
        app_sequence=['public_goods_simple'],
        num_demo_participants=3,
    ),
    dict(
        name='Survey',
        display_name="Survey demo",
        app_sequence=['survey'],
        num_demo_participants=1,
    ),
    dict(
        name='bargaining',
        display_name="bargaining demo",
        app_sequence=['bargaining'],
        num_demo_participants=2,
    ),
    dict(
        name='bertrand',
        display_name="bertrand demo",
        app_sequence=['bertrand'],
        num_demo_participants=2,
    ),
    dict(
        name='common_value_auction',
        display_name="common_value_auction",
        app_sequence=['common_value_auction'],
        num_demo_participants=2,
    ),
    dict(
        name='cournot',
        display_name="cournot",
        app_sequence=['cournot'],
        num_demo_participants=2,
    ),
    dict(
        name='dictator',
        display_name="dictator",
        app_sequence=['dictator'],
        num_demo_participants=2,
    ),
    dict(
        name='matching_pennies',
        display_name="matching_pennies",
        app_sequence=['matching_pennies'],
        num_demo_participants=2,
    ),
    dict(
        name='payment_info',
        display_name="payment_info",
        app_sequence=['payment_info'],
        num_demo_participants=2,
    ),
    dict(
        name='prisoner',
        display_name="prisoner",
        app_sequence=['prisoner'],
        num_demo_participants=2,
    ),
    dict(
        name='traveler_dilemma',
        display_name="traveler_dilemma",
        app_sequence=['traveler_dilemma'],
        num_demo_participants=2,
    ),
    dict(
        name='trust',
        display_name="trust",
        app_sequence=['trust'],
        num_demo_participants=2,
    ),
    dict(
        name='volunteer_dilemma',
        display_name="volunteer_dilemma",
        app_sequence=['volunteer_dilemma'],
        num_demo_participants=2,
    ),
]

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1.00, participation_fee=0.00, doc=""
)

PARTICIPANT_FIELDS = []
SESSION_FIELDS = []

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'en'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'USD'
USE_POINTS = True
POINTS_CUSTOM_NAME = 'tokens'

ROOMS = [
    dict(
        name='econ101',
        display_name='Econ 101 class',
        participant_label_file='_rooms/econ101.txt',
    ),
    dict(name='live_demo', display_name='Room for live demo (no participant labels)'),
]

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """
Here are some oTree games.
"""


SECRET_KEY = '1496624479172'

INSTALLED_APPS = ['otree']
