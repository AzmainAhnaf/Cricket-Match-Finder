from bs4 import BeautifulSoup
import requests

html_text = requests.get('https://www.espncricinfo.com/team/bangladesh-25/match-schedule-fixtures').text

soup = BeautifulSoup(html_text, 'lxml')

matches = soup.find_all('div', class_ = 'col-md-8 col-16')

for match in matches:
    date_time = match.find('div', class_ = 'status').span.text
    description = match.find('div', class_ = 'description').text
    temp_description = description.split(',')
    match_name = temp_description[0][5:]

    print(date_time, match_name)
    print("------------------------------------------------------------------------------------\n")

