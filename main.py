import pandas
import requests
from bs4 import BeautifulSoup
import pandas as pd
import pprint

response = requests.get('https://www.procyclingstats.com/rankings.php')
rankings = response.text

soup = BeautifulSoup(rankings, 'html.parser')
data = soup.select(selector='tr td a')

ranking = [num for num in range(1, 101)]
riders = [data[i].getText() for i in range(0, len(data), 3)]
teams = [data[i].getText() for i in range(1, len(data), 3)]
points = [data[i].getText() for i in range(2, len(data), 3)]

headers = ['Ranking', 'Rider', 'Team', 'Points']

df = pd.DataFrame(list(zip(*[ranking, riders, teams, points])))
df.to_csv('top_100_riders.csv', index=False)
top_100_riders = pd.read_csv('top_100_riders.csv', names=headers, skiprows=1, index_col='Ranking')
top_100_riders.to_csv('top_100_riders.csv')

pprint.pprint(top_100_riders)
