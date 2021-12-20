"""This moodule is concerned with all searches to be done in db, that are defined by the user"""
from mysql.connector import connect, Error
import click


def search():
    """Here we query the user about what he's looking for,
        and make a request for the fts table, as it is
        this table that has enabled the free text search"""
    query = input(click.style("What's your query? ", fg='bright_white', bold=True))
    try:
        conn = connect(
            host="localhost",
            user="mic",
            password="xxxx",
            database="rss")
        cur = conn.cursor()
        expression = 'SELECT id, name, title, link, date FROM rss WHERE MATCH(name, title) AGAINST (%s)'
        cur.execute(expression, (query,))
        record = cur.fetchall()
        for row in record:
            print(click.style('都', fg='bright_magenta', bold=True),
                  (click.style(str(row[1]), fg='bright_magenta', bold=True)))
            print(click.style('都', fg='bright_magenta', bold=True),
                  (click.style(str(row[2]), fg='bright_blue', bold=True)))
            print(click.style('都', fg='bright_magenta', bold=True),
                  (click.style(str(row[3]), fg='bright_white', bold=True)))
            print('\n')
    except Error as e:
        print("Error while connecting to db", e)
    finally:
        if(conn):
            conn.close()


if __name__ == "__main__":
    search()
