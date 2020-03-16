from collections import namedtuple

from bs4 import BeautifulSoup as Soup
import requests

PACKT = 'https://bites-data.s3.us-east-2.amazonaws.com/packt.html'
CONTENT = requests.get(PACKT).text

Book = namedtuple('Book', 'title description image link')


def get_book():
    """make a Soup object, parse the relevant html sections, and return a Book namedtuple"""
    soup = Soup(CONTENT, 'html.parser')
    title = soup.find('div', class_="dotd-title").get_text().strip()  # get title and strip whitespaces
    description = soup.find('div', class_="dotd-title").find_next("div").get_text().strip()
    link = soup.find('div', class_="dotd-main-book-image float-left").a.get('href')
    image = soup.find("img", class_="bookimage imagecache imagecache-dotd_main_image").get("src")
    return Book(title, description, image, link)
