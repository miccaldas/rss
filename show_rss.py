"""This module shows the content of the db. Turned it to a module, so I can separate changing
the db and seeing it"""
import click
import sqlite3


def show_rss():
    """We open an access to sqlite db, then embelish the oputput"""
    with sqlite3.connect('rss.db') as db:
        cur = db.cursor()
        cur.execute('SELECT * FROM rss ORDER BY strftime(date) ASC')  # 1
        rows = cur.fetchall()
        for row in rows:
            print(click.style('Ж - ', fg='bright_blue', bold=True), click.style(str(row[1]), fg='bright_blue', bold=True))
            print(click.style('Щ - ', fg='bright_cyan', bold=True), click.style(str(row[2]), fg='bright_cyan', bold=True))
            print(click.style('Ÿ - ', fg='bright_blue', bold=True), click.style(str(row[3]), fg='bright_blue', bold=True))
            print(click.style('Ʞ -', fg='bright_cyan', bold=True), click.style(str(row[4]), fg='bright_cyan', bold=True))
            print('\n')


if __name__ == "__main___":
    show_rss()


"""
NOTES:
1) - https://stackoverflow.com/questions/15234150/order-by-not-formatted-date-sqlite?rq=1
"""
