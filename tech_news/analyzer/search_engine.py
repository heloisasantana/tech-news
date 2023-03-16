from tech_news.database import search_news
from datetime import datetime


# Requisito 7
def search_by_title(title):
    news = search_news({"title": {"$regex": f"{title}", "$options": "i"}})
    tuples = []
    for new in news:
        tuples.append((new["title"], new["url"]))
    return tuples


# Requisito 8
def search_by_date(date):
    try:
        formatted_date = datetime.fromisoformat(date)
        news = search_news({"timestamp": formatted_date.strftime("%d/%m/%Y")})
        tuples = []
        for new in news:
            tuples.append((new["title"], new["url"]))
        return tuples
    except ValueError:
        raise ValueError("Data inválida")


# Requisito 9
def search_by_category(category):
    by_category = {"category": {"$regex": f"{category}", "$options": "i"}}
    news = search_news(by_category)
    tuples = []
    for new in news:
        tuples.append((new["title"], new["url"]))
    return tuples
