"""Downloads the images of the rss articles."""
import os
import pdb
import subprocess

import isort  # noqa: F401
import snoop
from loguru import logger

fmt = "{time} - {name} - {level} - {message}"
logger.add("../logs/info.log", level="INFO", format=fmt, backtrace=True, diagnose=True)  # noqa: E501
logger.add("../logs/error.log", level="ERROR", format=fmt, backtrace=True, diagnose=True)  # noqa: E501

subprocess.run(["isort", __file__])


@logger.catch
@snoop
def image_downloader():
    """First we create folders to house the images per article, then we move the url
    list inside the new folder, change directory to it and get the pics through
    wget."""

    dir = "/home/mic/python/rss/rss/scrape_rss/pics"
    for filename in os.listdir(dir):
        cmd = f"mkdir {filename}_dir; mv {filename} {filename}_dir; cd {filename}_dir; wget -i {filename}"
        subprocess.run(cmd, cwd=dir, shell=True)


if __name__ == "__main__":
    image_downloader()
