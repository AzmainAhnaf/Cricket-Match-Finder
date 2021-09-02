import find_match
print("Press (Q) to exit the application")
print("Press (A) for available country")
available_country_list = ['Australia', 'Afghanistan', 'Bangladesh', 'Ireland', 'England', 'Namibia' 'India', 'Nepal', 'New Zealand', 'Netherlands', 'Pakistan', 'Oman', 'South Africa', 'Papua New Guinea', 'Sri Lanka', 'Scotland', 'West Indies', 'UAE', 'Zimbabwe', 'USA']
while True:
    inp = input("Country name (or user input) --> ")
    inp = inp.lower()
    if inp == 'q':
        break
    elif inp == 'a':
        for country in available_country_list:
            print(country)
            print("---------------------------")
    elif inp == 'australia':
        print('\n')
        find_match.match_find('https://www.espncricinfo.com/team/australia-2/match-schedule-fixtures')
    elif inp == 'afghanistan':
        print('\n')
        find_match.match_find('https://www.espncricinfo.com/team/afghanistan-40/match-schedule-fixtures')
    elif inp == 'bangladesh':
        print('\n')
        find_match.match_find('https://www.espncricinfo.com/team/bangladesh-25/match-schedule-fixtures')
    elif inp == 'ireland':
        print('\n')
        find_match.match_find('https://www.espncricinfo.com/team/ireland-29/match-schedule-fixtures')
    elif inp == 'england':
        print('\n')
        find_match.match_find('https://www.espncricinfo.com/team/england-1/match-schedule-fixtures')
    elif inp == 'england':
        print('\n')
        find_match.match_find('https://www.espncricinfo.com/team/england-1/match-schedule-fixtures')
    elif inp == 'namibia':
        print('\n')
        find_match.match_find('https://www.espncricinfo.com/team/namibia-28/match-schedule-fixtures')
    elif inp == 'india':
        print('\n')
        find_match.match_find('https://www.espncricinfo.com/team/india-6/match-schedule-fixtures')
    elif inp == 'india':
        print('\n')
        find_match.match_find('https://www.espncricinfo.com/team/india-6/match-schedule-fixtures')
    elif inp == 'nepal':
        print('\n')
        find_match.match_find('https://www.espncricinfo.com/team/nepal-33/match-schedule-fixtures')
    elif inp == 'new zealand':
        print('\n')
        find_match.match_find('https://www.espncricinfo.com/team/new-zealand-5/match-schedule-fixtures')
    elif inp == 'netherlands':
        print('\n')
        find_match.match_find('https://www.espncricinfo.com/team/netherlands-15/match-schedule-fixtures')
    elif inp == 'pakistan':
        print('\n')
        find_match.match_find('https://www.espncricinfo.com/team/pakistan-7/match-schedule-fixtures')
    elif inp == 'oman':
        print('\n')
        find_match.match_find('https://www.espncricinfo.com/team/oman-37/match-schedule-fixtures')
    elif inp == 'south africa':
        print('\n')
        find_match.match_find('https://www.espncricinfo.com/team/south-africa-3/match-schedule-fixtures')
    elif inp == 'papua new guinea':
        print('\n')
        find_match.match_find('https://www.espncricinfo.com/team/papua-new-guinea-20/match-schedule-fixtures')
    elif inp == 'sri lanka':
        print('\n')
        find_match.match_find('https://www.espncricinfo.com/team/sri-lanka-8/match-schedule-fixtures')
    elif inp == 'scotland':
        print('\n')
        find_match.match_find('https://www.espncricinfo.com/team/scotland-30/match-schedule-fixtures')
    elif inp == 'west indies':
        print('\n')
        find_match.match_find('https://www.espncricinfo.com/team/west-indies-4/match-schedule-fixtures')
    elif inp == 'uae':
        print('\n')
        find_match.match_find('https://www.espncricinfo.com/team/united-arab-emirates-27/match-schedule-fixtures')
    elif inp == 'zimbabwe':
        print('\n')
        find_match.match_find('https://www.espncricinfo.com/team/zimbabwe-9/match-schedule-fixtures')
    elif inp == 'usa':
        print('\n')
        find_match.match_find('https://www.espncricinfo.com/team/united-states-of-america-11/match-schedule-fixtures')
    elif inp == 'f':
        print('\n')
        print('Welcome to the F world')
    else:
        print(f'there is no country named {inp.title()}')