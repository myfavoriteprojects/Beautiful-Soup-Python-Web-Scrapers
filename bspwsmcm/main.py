import requests
from bs4 import BeautifulSoup
import pandas as pd

headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:96.0) Gecko/20100101 Firefox/96.0'}

q_list = []

def getQuestions(tag, pg):
    url = f'https://stackoverflow.com/questions/tagged/{tag}?tab=Active&page={pg}&pagesize=50'
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, 'html.parser')
    questions = soup.find_all('div', {'class': 'question-summary'})
    for i in questions:
        question = {
        'tag': tag,
        'title': i.find('a', {'class': 'question-hyperlink'}).text,
        'link': 'https://stackoverflow.com' + i.find('a', {'class': 'question-hyperlink'})['href'],
        'votes': int(i.find('span', {'class': 'vote-count-post'}).text),
        'date': i.find('span', {'class': 'relativetime'})['title'],
        }
        q_list.append(question)
    return

for j in range(1, 3):
    getQuestions('java', j)


df = pd.DataFrame(q_list)
df.to_excel('stackOverFlowQuestions.xlsx', index=False)


