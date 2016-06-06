# -*- coding: utf-8 -*

from mailchimp3 import MailChimp
from jinja2 import Environment, FileSystemLoader

from config import MailChimpConfig
from scrapers.matches import MatchesScraper
from scrapers.tournaments import TournamentsScraper

matches_scraper = MatchesScraper()
tournaments_scraper = TournamentsScraper()
mailchimp_config = MailChimpConfig()

matches_scraper.scrap()
tournaments_scraper.scrap()

client = MailChimp('Keabard', mailchimp_config.apikey)
# print client.templates.all()

mailchimp_data = {
	# 'results': matches_scraper.get_results(),
	'matches': matches_scraper.get_local_matches(),
	'tournaments': tournaments_scraper.get_tournaments()
}

env = Environment(loader=FileSystemLoader('./templates'))
template = env.get_template('newsletter.html')
print template.render(**mailchimp_data)


#-- TODO
# Build un template à la MailChimp
# Créer le mécanisme qui va injecter les données dedans (Jinja 2 ?)

#-- Lors de l'envoi d'une newsletter
# Créer un template en envoyant le HTML grâce à l'API
# Créer une campagne
# Lancer la campagne