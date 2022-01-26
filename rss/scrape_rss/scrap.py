"""The objective is to download images from the webpages linked by the
   rss app, so as to create a web version with pics."""
import subprocess

import isort  # noqa: F401
import requests
import snoop
from bs4 import BeautifulSoup
from loguru import logger

from pylist import pylist

fmt = "{time} - {name} - {level} - {message}"
logger.add("../logs/info.log", level="INFO", format=fmt, backtrace=True, diagnose=True)  # noqa: E501
logger.add("../logs/error.log", level="ERROR", format=fmt, backtrace=True, diagnose=True)  # noqa: E501

subprocess.run(["isort", __file__])


@logger.catch
@snoop
def scrap():
    """We import the list of links and titles, pass the pages
    thorugh a scraper to identify the sources of the pics.
    We then create files, identified by the title,"""
    links = pylist()
    for url in links:
        titles = [url[0]]
        try:
            page = requests.get(url[1])
            soup = BeautifulSoup(page.content, "html.parser")
            pics = soup.find_all("img")
            list_imgs = []
            for i in pics:
                list_imgs.append(i.get("src"))
                for tit in titles:
                    with open(f"/home/mic/python/rss/rss/scrape_rss/img_per_article/{tit}", "w") as f:
                        for img in list_imgs:
                            f.write(str(img))
                            f.write("\n")
        except KeyError:
            pass


if __name__ == "__main__":
    scrap()
