from bs4 import BeautifulSoup
from bs4.element import Declaration
import requests
import time_def

def match_find(link):

    html_text = requests.get(link).text

    soup = BeautifulSoup(html_text, 'lxml')

    matches = soup.find_all('div', class_ = 'col-md-8 col-16')

    for match in matches:
        # match date and match time
        date_time = match.find('div', class_ = 'status').span.text
        date_time = date_time.split(',')
        
        # day of the match
        day = date_time[0]
        day = time_def.day_modify(day)

        # date of the match
        date = date_time[1]
        date = time_def.date_modify(date)

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

        # output the result
        if (date.strip()[-2:] == 'am' or date.strip()[-2:] == 'pm'):
            print(f'Series --> {tournament_name.strip()}')
            print(f'Match  --> {match_name.strip()} --> {match_type.strip()}')
            print(f'date   --> recent')
            print(f'day    --> Today or tomorrow')
            print(f'time   --> {time.strip()}')
            print("------------------------------------------------------------------------------------\n")
            continue
        

        print(f'Series --> {tournament_name.strip()}')
        print(f'Match  --> {match_name.strip()} --> {match_type.strip()}')
        print(f'date   --> {date.strip()}')
        print(f'day    --> {day.strip()}')
        print(f'time   --> {time.strip()}')
        print("------------------------------------------------------------------------------------\n")

match_find('https://www.espncricinfo.com/team/bangladesh-25/match-schedule-fixtures')
