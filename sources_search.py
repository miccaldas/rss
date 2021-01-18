"""This module pertains to all searches that were generated in the main module"""
import click
import sqlite3

source = ''


def sources(source):
    """Getting its query from main, the function calls the db, and asks for rss_fts
       table, which has free text search enable."""
    with sqlite3.connect('rss.db') as db:
        cur = db.cursor()
        expression = 'SELECT * FROM rss_fts WHERE rss_fts MATCH ? ORDER BY date DESC'
        cur.execute(expression, (source,))
        record = cur.fetchall()
        for row in record:
            print(click.style(' 𝝵 ', fg='bright_magenta', bold=True),
                 (click.style(str(row[1]), fg='bright_magenta', bold=True)))
            print(click.style(' 𝞇 ', fg='bright_magenta', bold=True),
                 (click.style(str(row[2]), fg='bright_blue', bold=True)))
            print(click.style(' 𝝮 ', fg='bright_magenta', bold=True),
                 (click.style(str(row[3]), fg='bright_white', bold=True)))
            print('\n')


if __name__ == "__main__":
    sources(source)
