# -*- coding: utf-8 -*

from bs4 import BeautifulSoup
import copy
from datetime import datetime
from datetime import timedelta
import locale
import requests

from config import DEFAULT_TOURNAMENTS_PERIOD, DEFAULT_TOURNAMENTS_FROM_NOW

locale.setlocale(locale.LC_ALL, 'fr_FR.UTF-8')

REGION_TOURNAMENTS_URL = 'http://www.accro-des-tournois.com/'
LOCALE_MONTHS = ['Janvier', 'Février', 'Mars', 'Avril', 'Mai', 'Juin', 'Juillet', 'Août', 'Septembre', 'Octobre', 'Novembre', 'Décembre']

def _guess_month(month_string):
        # We have to guess the correct month with just the first letters...
        remaining_months = copy.deepcopy(LOCALE_MONTHS)
        remaining_months = [rem_month for rem_month in remaining_months if rem_month.startswith(month_string)]
        return remaining_months[0]

def _guess_tournament_date(day, month):
    # Guess tournament date because year is not specified.
    #- We receive month as a %B string...
    month = datetime.strptime(_guess_month(month), '%B').month
    day = int(day)
    now = datetime.now()
    date_guess = datetime(now.year, month, day)
    if date_guess < now:
        date_guess = datetime(now.year+1, month, day)
    return date_guess

class TournamentsScraper:

    def __init__(self):
        self.tournaments = []

    def get_tournaments(self, period=DEFAULT_TOURNAMENTS_PERIOD, from_now=DEFAULT_TOURNAMENTS_FROM_NOW):
        start_date = datetime.today() + from_now
        end_date = start_date + period
        return [tournament for tournament in self.tournaments if tournament['datetime'] >= start_date and tournament['datetime'] <= end_date]

    def scrap(self):
        html = requests.post(REGION_TOURNAMENTS_URL, data={'searchregion': 17})
        soup = BeautifulSoup(html.content, 'html.parser')
        tournaments_lis = soup.find_all('li', {'class': 'elementtournoi'})

        for tournament_li in tournaments_lis:
            tournament_a = tournament_li.find('a')
            tournament = {
                "environment": tournament_a.attrs['class'][0],
                "link": tournament_a.attrs['href'],
                "datetime": guess_tournament_date(tournament_a.find('div', {'class': 'calendrierjour'}).text.encode('utf-8'), tournament_a.find('div', {'class': 'calendriermois'}).text.encode('utf-8')),
                "location": tournament_a.find('div', {'class': 'annucontent'}).find('h3').text.encode('utf-8'),
                "type": tournament_a.find('div', {'class': 'annucontent'}).find('div').text.encode('utf-8')
            }
            self.tournaments.append(tournament)

        return self.tournaments