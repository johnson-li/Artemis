from os.path import expanduser

HOME = expanduser("~")
PROJECT_ID = 'our-foundry-254505'
PROJECT_EMAIL = '392419806272-compute@developer.gserviceaccount.com'
SERVICE_ACCOUNT_FILE = "%s/keys/our-foundry-254505-72a6860f5a7c.json" % HOME
ZONES = ['us-east1-c', 'us-east4-c', 'us-central1-c', 'us-west1-c', 'us-west2-c', 'us-west3-c',
         'europe-west1-c', 'europe-west2-c', 'europe-west3-c', 'europe-west4-c', 'europe-west6-c', 'europe-north1-c',
         'asia-east1-c',  'asia-east2-c', 'asia-southeast1-c', 'asia-northeast1-c', 'asia-northeast2-c', 'asia-northeast3-c', 'asia-south1-c', 'australia-southeast1-c',
         'southamerica-east1-c', 'northamerica-northeast1-c']
ZONES = ['us-east1-c', 'us-east4-c', 'us-central1-c', 'us-west3-c',
         'europe-west1-c', 'europe-west4-c', 'europe-north1-c',
         'asia-east1-c', 'asia-southeast1-c', 'asia-northeast1-c', 'asia-northeast3-c', 'asia-south1-c', 'australia-southeast1-c',
         'southamerica-east1-c', 'northamerica-northeast1-c']
SSH_PUBLIC_KEY = "johnsonli1993:ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAACAQDVcYOl/Q/TkpxdA4GYbVda8flEQ3EDTaNoBMzYHQ/owPYXP/vaAT3DL3Lxgs12eslNA9px8wqNckmdUdc0NsUyh8Od1ke2S+FCkC/b2tK75aZ3PQsGJb0z+hdYu1/kFby5WKllTQRgNkvkOhTOWu+ybFeiCrylShMXXrkdC6aBQ8w7qWyaGlr1CBs+cKxAd2zyuYn3E5KiyhJPFZr+hN8EH6Q0wtAwTec8ViosY7pEcdIkBl1RUvwiZdaCv5fnGoax62dzQO7jCTVdBAH3jQifBsMLaLffGKqGjF926DLFwhEpUEKL4B/I3LNehAbV+xDnIkFchucgjNkmXamv5yl7W5PVgdyl3W7SoxKfVut0/0eKUKjRplZrhKVCRNLKqnHA9C3yF8QAYRwhlAOwFarEAi5zJNJV+JniFpNkXCsXdJxuZukHPDVJlY8LVyopxbvjSGTowlwgIoCtJPWbW15nioo0Sm1exVJff50eG6L8oTbFTCIar2YcXz07skqmW1nqE53bEBgqageSsjOcBouS8f7X3xOC66qQB1Oyyi9+gUJF4O6NpLlhFvyJMER3Yl4v89LyqAUi27FGbcn+zzCKELV5zjHTmJ+18EOPYv8h7IIJ4nR31QCD4F1eW1TRt4fXn8oEW/H9H+ItcDKQwSn39ZyK/q1t8hYDV1rzavv59w== johnsonli1993@gmail.com"
DEFAULT_USER_NAME = 'johnsonli1993'
USER_NAME = 'johnson'

DOMAIN_NAME = 'serviceid.xuebing.li'
ANYCAST_IP = '11.11.11.11'

DATABASE_NAME = 'serviceid_db'
TABLE_NAME_MEASUREMENTS = 'measurements'
TABLE_NAME_DEPLOYMENT = 'deployment'
TABLE_NAME_INTRA = 'intra'
