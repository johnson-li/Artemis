REGIONS = {
    'us-east-1': 'Virginia',
    'us-east-2': 'Ohio',
    'us-west-1': 'California',
    'us-west-2': 'Oregon',
    'ap-south-1': 'Mumbai',
    'ap-southeast-1': 'Singapore',
    'ap-southeast-2': 'Sydney',
    'ap-northeast-1': 'Tokyo',
    'ap-northeast-2': 'Seoul',
    'ca-central-1': 'Central',
    'eu-central-1': 'Frankfurt',
    'eu-west-1': 'Ireland',
    'eu-west-2': 'London',
    'eu-west-3': 'Paris',
    'sa-east-1': 'SaoPaulo',
}

REVERSE_REGIONS = {v.lower(): k for k, v in REGIONS.items()}

LOCATION = {
    'us-east-1': (37.8221044, -81.5420547),
    'us-east-2': (40.3436043, -84.9124343),
    'us-west-1': (37.184309, -123.7974511),
    'us-west-2': (44.1234999, -122.826347),
    'ap-south-1': (19.0821978, 72.7411001),
    'ap-southeast-1': (1.3139961, 103.7041634),
    'ap-southeast-2': (-33.847927, 150.6517873),
    'ap-northeast-1': (35.9610251, 139.311752),
    'ap-northeast-2': (37.5352816, 126.7439797),
    'ca-central-1': (44.9519362, -77.3228968),
    'eu-central-1': (50.1211277, 8.4964813),
    'eu-west-1': (53.3942362, -10.1982995),
    'eu-west-2': (51.5285582, -0.241681),
    'eu-west-3': (48.8588377, 2.2770203),
    'sa-east-1': (-23.6821604, -46.8754909),
}
