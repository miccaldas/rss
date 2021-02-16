""" Module to append new feeds to the app """
import click


def append_rss():
    """ This module is necessary because, in insert_db.py, the line 'fp = feedparser.parse(url)', wouldn't accept a function object,
    which is what happens if you imported the outcome of this module directly. So, it was necessary to assure that the url would be
    formatted as a string. Hence the passage to a text file. This has the added advantage of creating a record of all feeds in use. """
    new_rss = input(click.style(' What is the url you want to add? ', fg='magenta', bold=True))
    envio = open('url_list.txt', 'a')
    envio.write(new_rss)
    envio.close()


if __name__ == "__main__":
    append_rss()
