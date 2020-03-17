
urls = {'NextSteps': 'https://next:steps@stage.nextsteps.ru/'}

TIMEOUT = 60
TIMEOUT_10 = 10
TIMEOUT_15 = 15
TIMEOUT_30 = 30
TIMEOUT_120 = 120


def get_url_data(website_name):
    return urls[website_name]
