# -*- coding: utf-8 -*
from bs4 import BeautifulSoup
from datetime import datetime
import re
import requests

from config import DEFAULT_MATCHES_PERIOD, DEFAULT_MATCHES_FROM_NOW, DEFAULT_RESULTS_PERIOD, DEFAULT_RESULTS_UNTIL_NOW
from constants import TEAMS


class MatchesScraper:

    def __init__(self):
        self.matches = {}

    def get_local_matches(self, period = DEFAULT_MATCHES_PERIOD, from_now = DEFAULT_MATCHES_FROM_NOW):
        local_matches = {}
        start_date = datetime.today() + from_now
        end_date = start_date + period
        for team_key in self.matches.keys():
            local_matches[team_key] = [match for match in self.matches[team_key] \
            if match['receiving_team']['name'] == TEAMS[team_key]['calendar_name'] and match['datetime'] >= start_date and match['datetime'] <= end_date]
        return local_matches

    def get_results(self, period = DEFAULT_RESULTS_PERIOD, until_now = DEFAULT_RESULTS_UNTIL_NOW):
        results = {}
        start_date = datetime.today() - until_now
        end_date = start_date + period
        for team_key in TEAMS.keys():
            results[team_key] = [match for match in self.matches[team_key] if match['datetime'] >= start_date and match['datetime'] <= end_date]
        return results

    def scrap(self):
        for team_key in TEAMS.keys():
            if TEAMS[team_key]['calendar_url']:
                self.matches[team_key] = []
                html = requests.get(TEAMS[team_key]['calendar_url'])
                soup = BeautifulSoup(html.content, 'html.parser')
                match_tds = soup.find_all('td', string=re.compile('IMA.{4}$'))
                for match_td in match_tds:
                    tr = match_td.parent
                    match_dict = {
                        'receiving_team': {
                            'name': tr.find_all('td')[3].text
                        },
                        'visiting_team': {
                            'name': tr.find_all('td')[5].text
                        },
                        'datetime': datetime.strptime('{} - {}'.format(tr.find_all('td')[1].text, tr.find_all('td')[2].text), '%d/%m/%y - %H:%M')
                    }

                    # If the match has already happened
                    if tr.find_all('td')[8].text:
                        match_dict['scores'] = tr.find_all('td')[8].text
                        match_dict['receiving_team']['sets'] = int(tr.find_all('td')[6].text)
                        match_dict['visiting_team']['sets'] = int(tr.find_all('td')[7].text)
                    else:
                        match_dict['gym'] = tr.find_all('td')[8].text

                    self.matches[team_key].append(match_dict)

        return self.matches
