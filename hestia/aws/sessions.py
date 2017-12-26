import boto3


class Sessions:
    def __init__(self) -> None:
        self.us_east_1 = boto3.session.Session(region_name='us-east-1')
        self.us_east_2 = boto3.session.Session(region_name='us-east-2')
        self.us_west_1 = boto3.session.Session(region_name='us-west-1')
        self.us_west_2 = boto3.session.Session(region_name='us-west-2')
        self.ap_south_1 = boto3.session.Session(region_name='ap-south-1')
        self.ap_southeast_1 = boto3.session.Session(region_name='ap-southeast-1')
        self.ap_southeast_2 = boto3.session.Session(region_name='ap-southeast-2')
        self.ap_northeast_1 = boto3.session.Session(region_name='ap-northeast-1')
        self.ap_northeast_2 = boto3.session.Session(region_name='ap-northeast-2')
        self.ca_central_1 = boto3.session.Session(region_name='ca-central-1')
        self.eu_central_1 = boto3.session.Session(region_name='eu-central-1')
        self.eu_west_1 = boto3.session.Session(region_name='eu-west-1')
        self.eu_west_2 = boto3.session.Session(region_name='eu-west-2')
        self.eu_west_3 = boto3.session.Session(region_name='eu-west-3')
        self.sa_east_1 = boto3.session.Session(region_name='sa-east-1')

    def all(self):
        parameters = [value for value in self.__dict__.values()]
        return list(filter(lambda x: isinstance(x, boto3.session.Session), parameters))
