from bs4 import BeautifulSoup

def find_offer_table_data(html):
    soup = BeautifulSoup(html, 'html.parser')
    promoted_offer_data = soup.find('div', attrs={'data-cy': 'search.listing.promoted'})
    organic_offer_data = soup.find('div', attrs={'data-cy': 'search.listing.organic'})
    