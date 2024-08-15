# utils/fetch_news.py
from newsapi import NewsApiClient
import datetime

def fetch_articles(categories_list, api_key):
    newsapi = NewsApiClient(api_key=api_key)
    yesterday = (datetime.datetime.now() - datetime.timedelta(days=1)).strftime('%Y-%m-%d')
    today = datetime.datetime.now().strftime('%Y-%m-%d')

    articles_data = []
    for category in categories_list:
        all_articles = newsapi.get_everything(
            q=category,
            from_param=yesterday,
            to=today,
            language='en',
            sort_by='relevancy'
        )
        for article in all_articles['articles']:
            articles_data.append({
                'Category': category,
                'Source': article['source']['name'],
                'Author': article['author'],
                'Title': article['title'],
                'Description': article['description'],
                'Date Time': article['publishedAt'],
                'URL': article['url'],
                'Image': article['urlToImage']
            })
    
    return articles_data
