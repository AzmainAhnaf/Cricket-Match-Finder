import find_match

def findMatch(query):
    print('\n')
    return find_match.match_find(f'https://www.espncricinfo.com/team/{query}/match-schedule-fixtures')


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
        findMatch('australia-2')
    elif inp == 'afghanistan':
        findMatch('afghanistan-40')
    elif inp == 'bangladesh':
        findMatch('bangladesh-25')
    elif inp == 'ireland':
        findMatch('ireland-29')
    elif inp == 'england':
        findMatch('england-1')
    elif inp == 'namibia':
        findMatch('namibia-28')
    elif inp == 'india':
        findMatch('india-6')
    elif inp == 'nepal':
        findMatch('nepal-33')
    elif inp == 'new zealand':
        findMatch('new-zealand-5')
    elif inp == 'netherlands':
        findMatch('netherlands-15')
    elif inp == 'pakistan':
        findMatch('pakistan-7')
    elif inp == 'oman':
        findMatch('oman-37')
    elif inp == 'south africa':
        findMatch('south-africa-3')
    elif inp == 'papua new guinea':
        findMatch('papua-new-guinea-20')
    elif inp == 'sri lanka':
        findMatch('sri-lanka-8')
    elif inp == 'scotland':
        findMatch('scotland-30')
    elif inp == 'west indies':
        findMatch('west-indies-4')
    elif inp == 'uae':
        findMatch('united-arab-emirates-27')
    elif inp == 'zimbabwe':
        findMatch('zimbabwe-9')
    elif inp == 'usa':
        findMatch('united-states-of-america-11')
    elif inp == 'f':
        print('Welcome to the F world')
    else:
        print(f'there is no country named {inp.title()}')