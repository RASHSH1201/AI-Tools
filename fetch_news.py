# fetchnews.py
import requests

def fetch_news(query, api_key):
    URL = f"https://newsapi.org/v2/everything?q={query}&language=en&apiKey={api_key}"
    response = requests.get(URL)
    data = response.json()

    headlines = []
    for article in data["articles"]:
        title = article.get("title") or "No Title"
        desc = article.get("description") or "No Description"
        headlines.append(title + " — " + desc)

    return headlines