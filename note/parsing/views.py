from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
from django.http import HttpResponse


def index(request):
    url = 'https://lifehacker.ru/topics/technology/'

    response = requests.get(url)

    if response.status_code == 200:
        html = response.text

        soup = BeautifulSoup(html, 'html.parser')

        titles_list = []
        links_list = []

        for item in soup.find_all('div', class_='post__title'):
            title = item.find('a').text
            link = item.find('a').get('href')

            titles_list.append(title)
            links_list.append(link)

        return HttpResponse("Titles: {}\nLinks: {}".format(titles_list, links_list))
