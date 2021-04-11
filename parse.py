import re
import requests as rqs
import pandas as pd
from bs4 import BeautifulSoup

class ParseNews:
  
    def __init__(self):
        self.url = 'https://www.banki.ru/news/lenta/'
        self.page = 'page{id}'
        self.create_url = lambda target: url + self.page.format(id=target)
        self.data = None
        
    def extract(
        self, 
        page_start: int = 0, 
        page_end: int = 1) -> None:
        '''
        Parse banki.ru newsfeed
        Recommended to specify start and end page to parse 
        '''
        response = []
        for page_index in range(page_start, page_end):
            r = rqs.get(self.create_url(page_index))
            if r.status_code == 200:
                soup = BeautifulSoup(r.text)
                news_dates = list(map(lambda x: x.text, soup.select('.widget__date > span > time')))
                for news_index, block_news in enumerate(soup.select('.text-list')):
                    for each_news in block_news.select('li'):
                        try:
                            time = each_news.find(class_='text-list-date').text
                            content = each_news.find(class_='text-list-link').text
                            views = each_news.select('li > span')[2].text
                            link = each_news.find('a').get('href')
                            response.append([news_dates[news_index], time, content, views, link])
                        except BaseException as err:
                            print(f'{type(err).__name__}')
            self.data = response
            return self
        
    @property
    def news(self) -> pd.DataFrame:
        '''
        Prepare news for processing and wrap to DataFrame
        '''
        news = pd.DataFrame(self.data, columns=['date', 'time', 'text', 'views', 'link'])
        news['views'] = news['views'].str.replace('[^0-9]+', '')
        news['text'] = news['text'].str.replace('[^а-я0-9a-z ]+', '', flags=re.IGNORECASE)
        return news

# Example: 
      
ParseNews().extract(1, 3).news

# 	date	time	text	views	link
# 0	11.04.2021	18:53	АльфаБанк и X5 Retail Group запустили кнопку д...	303	/news/lenta/?id=10944599
# 1	11.04.2021	17:16	Держатели карт Халва смогут оплачивать топливо...	1249	/news/lenta/?id=10944597
# 2	11.04.2021	16:42	Банк Открытие будет возмещать премиальным клие...	1288	/news/lenta/?id=10944455
