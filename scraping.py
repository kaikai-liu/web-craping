import requests
from bs4 import BeautifulSoup

URL = 'https://www.sandiegofishreports.com/landings/seaforth_sportfishing.php?landing_id=20&month=8&year=2019#historicals'
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'lxml')
# print(soup)
elms = soup.find_all('div', class_='col-lg-12 col-md-12 col-sm-12 col-xs-12')
# elements = soup.find_all('table',class_ = 'scale-table')
# elms = elms.find_all('tbody')
print(elms)
