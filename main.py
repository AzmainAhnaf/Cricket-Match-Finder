from bs4 import BeautifulSoup
from bs4.element import Declaration
import requests

html_text = requests.get('https://www.espncricinfo.com/team/bangladesh-25/match-schedule-fixtures').text

soup = BeautifulSoup(html_text, 'lxml')

matches = soup.find_all('div', class_ = 'col-md-8 col-16')

for match in matches:
    # match date and match time
    date_time = match.find('div', class_ = 'status').span.text
    
    description = match.find('div', class_ = 'description').text
    comma_splited_description = description.split(',')
    
    # match vs
    match_name = comma_splited_description[0][5:]
    
    match_type = comma_splited_description[2].split()
    
    # match type (e.g. ODI, T20I, 6th match etc)
    match_type = (f"{match_type[0]} {match_type[1]}")

    print(comma_splited_description)
    print("------------------------------------------------------------------------------------\n")

