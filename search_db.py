"""This moodule is concerned with all searches to be done in db, that are
    defined by the user"""
import sqlite3
import click


def search():
    """Here we query the user about what he's looking for,
        and make a request for the fts table, as it is
        this table that has enabled the free text search"""
    query = input(click.style("What's your query? ", fg='bright_white', bold=True))
    with sqlite3.connect('rss.db') as db:
        cur = db.cursor()
        expression = 'SELECT * FROM rss_fts WHERE rss_fts MATCH ? ORDER BY strftime(date) DESC'   # 1
        cur.execute(expression, (query,))
        record = cur.fetchall()
        for row in record:
            print(click.style('', fg='bright_magenta', bold=True),
                (click.style(str(row[1]), fg='bright_magenta', bold=True)))
            print(click.style(' ', fg='bright_magenta', bold=True),
                (click.style(str(row[2]), fg='bright_blue', bold=True)))
            print(click.style(' ', fg='bright_magenta', bold=True),
                (click.style(str(row[3]), fg='bright_white', bold=True)))
            print('\n')


if __name__ == "__main__":
    search()


"""
NOTES:
1) - https://stackoverflow.com/questions/15234150/order-by-not-formatted-date-sqlite?rq=1
"""
