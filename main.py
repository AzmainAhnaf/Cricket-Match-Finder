from bs4 import BeautifulSoup
from bs4.element import Declaration
import requests
import time_def

html_text = requests.get('https://www.espncricinfo.com/team/bangladesh-25/match-schedule-fixtures').text

soup = BeautifulSoup(html_text, 'lxml')

matches = soup.find_all('div', class_ = 'col-md-8 col-16')

for match in matches:
    # match date and match time
    date_time = match.find('div', class_ = 'status').span.text
    date_time = date_time.split(',')
    
    # weekly day of the match
    day = date_time[0]

    # date of the match
    date = date_time[1]

    # time of the match
    time = date_time[-1]
    
    description = match.find('div', class_ = 'description').text
    comma_splited_description = description.split(',')
    
    # match vs
    match_name = comma_splited_description[0][5:]
    
    match_type = comma_splited_description[2].split()
    
    # match type (e.g. ODI, T20I, 6th match etc)
    match_type = (f"{match_type[0]} {match_type[1]}")

    # tournament name
    tournament_name = (comma_splited_description[1])

    hour = time.split(':')[0]
    minute = time.split(':')[1][:2]
    meridian = time.split()[-1]

    # time
    time = time_def.add_six_hour(hour, minute, meridian)

    print(day)
    print("------------------------------------------------------------------------------------\n")

