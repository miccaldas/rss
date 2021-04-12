"""This module shuffles the feed entries, so as to not present all the Reddit results in a row. They are many and it impoverishes the experience"""
import random
import click
import sqlite3


def shuffle():
    """We open an access to sqlite db, shuffle it, then embelish the oputput"""
    with sqlite3.connect('rss.db') as db:
        cur = db.cursor()
        cur.execute('SELECT * FROM rss')
        rows = cur.fetchall()
        for row in rows:
            random.shuffle(list(row))   # https://tinyurl.com/yj9vahf7, 'row' is initially a tuple. We must change that. https://tinyurl.com/yzdk4e6y
            print(click.style('Ж - ', fg='bright_blue', bold=True), click.style(str(row[1]), fg='bright_blue', bold=True))
            print(click.style('Щ - ', fg='bright_cyan', bold=True), click.style(str(row[2]), fg='bright_cyan', bold=True))
            print(click.style('Ÿ - ', fg='bright_blue', bold=True), click.style(str(row[3]), fg='bright_blue', bold=True))
            print(click.style('Ʞ -', fg='bright_cyan', bold=True), click.style(str(row[4]), fg='bright_cyan', bold=True))
            print('\n')


if __name__ == "__main___":
    shuffle()


"""
NOTES:
1) - https://stackoverflow.com/questions/15234150/order-by-not-formatted-date-sqlite?rq=1
"""
