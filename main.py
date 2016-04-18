from mailchimp3 import MailChimp

from config import MailChimpConfig
from scrapers.matches.scrapers import MatchesScraper
from scrapers.tournaments.scrapers import TournamentsScraper

matches_scraper = MatchesScraper()
tournaments_scraper = TournamentsScraper()
mailchimp_config = MailChimpConfig()

MatchesScraper.scrap()
TournamentsScraper.scrap()

client = MailChimp('Keabard', mailchimp_config.apikey)
print client.templates.all()

mailchimp_data = {
	'results': matches_scraper.get_results(),
	'matches': matches_scraper.get_local_matches(),
	'tournaments': tournaments_scraper.get_tournaments()
}

#-- TODO
# Build un template à la MailChimp
# Créer le mécanisme qui va injecter les données dedans (Jinja 2 ?)

#-- Lors de l'envoi d'une newsletter
# Créer un template en envoyant le HTML grâce à l'API
# Créer une campagne
# Lancer la campagne