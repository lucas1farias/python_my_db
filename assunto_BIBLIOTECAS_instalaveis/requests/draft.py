

import requests

url = 'https://pathofexile.fandom.com/wiki/List_of_divination_cards'
rqst = requests.get(url)

string = rqst.text
print(string)
list_ = string.split('\n')
