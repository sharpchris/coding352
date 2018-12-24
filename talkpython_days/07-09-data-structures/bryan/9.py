#ref: https://github.com/talkpython/100daysofcode-with-python-course/tree/master/days/07-09-data-structures

us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}


states_list = ['Oklahoma',
               'Kansas',
               'North Carolina',
               'Georgia',
               'Oregon',
               'Mississippi',
               'Minnesota',
               'Colorado',
               'Alabama',
               'Massachusetts',
               'Arizona',
               'Connecticut',
               'Montana',
               'West Virginia',
               'Nebraska',
               'New York',
               'Nevada',
               'Idaho',
               'New Jersey',
               'Missouri',
               'South Carolina',
               'Pennsylvania',
               'Rhode Island',
               'New Mexico',
               'Alaska',
               'New Hampshire',
               'Tennessee',
               'Washington',
               'Indiana',
               'Hawaii',
               'Kentucky',
               'Virginia',
               'Ohio',
               'Wisconsin',
               'Maryland',
               'Florida',
               'Utah',
               'Maine',
               'California',
               'Vermont',
               'Arkansas',
               'Wyoming',
               'Louisiana',
               'North Dakota',
               'South Dakota',
               'Texas',
               'Illinois',
               'Iowa',
               'Michigan',
               'Delaware']

space = '+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+'

#print out the 10th item in each
def print_tenth_item(data):
    if isinstance(data, list):
        print(data[9])
    else:
        em_list = []
        for v in data.values():
            em_list.append(v)
        print(em_list[9])

print_tenth_item(states_list)
print_tenth_item(us_state_abbrev)
print(space)

#print out the 45th key in the dictionary
def print_fortyfifth_key(data):
    em_keys = []
    for k in data.keys():
        em_keys.append(k)
    print(em_keys[44])

print_fortyfifth_key(us_state_abbrev)
print(space)

#print out the 27th value in the dictionary
def print_twentyseventh_value(data):
    em_val = []
    for v in data.values():
        em_val.append(v)
    print(em_val[26])
    
print_twentyseventh_value(us_state_abbrev)
