import os
import sys
from datetime import timedelta

DEFAULT_TOURNAMENTS_PERIOD = timedelta(weeks = 2)
DEFAULT_TOURNAMENTS_FROM_NOW = timedelta(weeks = 2)

DEFAULT_MATCHES_PERIOD = timedelta(weeks = 4)
DEFAULT_MATCHES_FROM_NOW = timedelta(weeks = 20)

DEFAULT_RESULTS_PERIOD = timedelta(weeks = 1)
DEFAULT_RESULTS_UNTIL_NOW = timedelta(weeks = 1)

class MailChimpConfig:
    def __init__(self):
        if os.path.isfile('./APIKEY') == False:
            print "Please enter your API Key into the APIKEY file as mentioned in README.md"
            sys.exit()

        f = open('./APIKEY', 'r+')
        apikey = f.read().strip()
        f.close()

        parts = apikey.split('-')
        if len(parts) != 2:
            print "This doesn't look like an API Key: " + apikey
            print "The API Key should have both a key and a server name, separated by a dash, like this: abcdefg8abcdefg6abcdefg4-us1"
            sys.exit()

        self.apikey = apikey
        self.shard = parts[1]
        self.api_root = "https://" + self.shard + ".api.mailchimp.com/3.0/"
