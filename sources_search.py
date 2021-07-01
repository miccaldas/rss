"""This module pertains to all searches that were generated in the main module"""
import click
from mysql.connector import connect, Error


source = ''


def sources(source):
    """Getting its query from rss.py, the function calls the db."""
    try:
        conn = connect(
            host="localhost",
            user="mic",
            password="xxxx",
            database="rss")
        cur = conn.cursor()
        expression = 'SELECT * FROM rss WHERE MATCH (name, title) AGAINST (%s)'
        cur.execute(expression, (source,))
        record = cur.fetchall()
        for row in record:
            print(click.style('  ', fg='bright_magenta', bold=True),
                  (click.style(str(row[1]), fg='bright_magenta', bold=True)))
            print(click.style('  ', fg='bright_magenta', bold=True),
                  (click.style(str(row[2]), fg='bright_blue', bold=True)))
            print(click.style('  ', fg='bright_magenta', bold=True),
                  (click.style(str(row[3]), fg='bright_white', bold=True)))
            print('\n')
    except Error as e:
        print("Error while connecting to db", e)
    finally:
        if(conn):
            conn.close()


if __name__ == "__main__":
    sources(source)
