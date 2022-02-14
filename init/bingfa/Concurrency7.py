import asyncio
import time
from random import random

import requests
from bs4 import BeautifulSoup


def main():
    url = "https://movie.douban.com/cinema/later/beijing/"

    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36"}

    init_page = requests.get(url, headers=header).content
    init_soup = BeautifulSoup(init_page, 'lxml')
    # init_soup = BeautifulSoup(init_page, 'html.parser').find()


    all_movies = init_soup.find('div', id="showing-soon")
    for each_movie in all_movies.find_all('div', class_="item"):
        all_a_tag = each_movie.find_all('a')
        all_li_tag = each_movie.find_all('li')

        movie_name = all_a_tag[1].text
        url_to_fetch = all_a_tag[1]['href']
        movie_date = all_li_tag[0].text

        response_item = requests.get(url_to_fetch, headers=header).content
        soup_item = BeautifulSoup(response_item, 'lxml')
        img_tag = soup_item.find('img')

        print('{} {} {}'.format(movie_name, movie_date, img_tag['src']))

start_time = time.time()
asyncio.run(main())
end_time = time.time()

print(end_time - start_time)

