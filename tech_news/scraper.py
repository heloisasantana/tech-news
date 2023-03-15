import requests
import time
from parsel import Selector


# Requisito 1
def fetch(url):
    try:
        time.sleep(1)
        response = requests.get(url, headers={"user-agent": "Fake user-agent"})
        response.raise_for_status()
        return response.text
    except (requests.HTTPError, requests.ReadTimeout):
        return None


# Requisito 2
def scrape_updates(html_content):
    selector = Selector(text=html_content)
    links_list = selector.css(".entry-title a::attr(href)").getall()
    return links_list


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(text=html_content)
    next_link = selector.css(".next::attr(href)").get()
    return next_link


# Requisito 4
def scrape_news(html_content):
    selector = Selector(html_content)
    url = selector.css("link[rel='canonical']::attr(href)").get()
    title = selector.css(".entry-title::text").get().strip()
    timestamp = selector.css(".meta-date::text").get().strip()
    writer = selector.css(".author a::text").get().strip()
    reading_time = int(selector.css(".meta-reading-time::text").get()[0:2])
    summary_selector = selector.css(".entry-content > p:first-of-type *::text")
    summary = "".join(summary_selector.getall()).strip()
    category = selector.css(".label::text").get()
    return {
        "url": url,
        "title": title,
        "timestamp": timestamp,
        "writer": writer,
        "reading_time": reading_time,
        "summary": summary,
        "category": category,
        }


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
