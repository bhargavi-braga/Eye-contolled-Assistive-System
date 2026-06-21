import requests
api_key = '9f1344e3bd764bd6ad26df9a8d2768dd'

def get_news():
  res = requests.get(f'https://newsapi.org/v2/top-headlines?country=in&apiKey={api_key}').json()
  news = []
  for i in res['articles']:
    news.append(i['title'])
  with open('news.txt','w',encoding='utf-8') as f:
    for idx,i in enumerate(news):
      f.write(f'{idx+1}. {i}\n')
  return news[:3]

if __name__ == '__main__':
  get_news()