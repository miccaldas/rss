"""This module shuffles the feed entries, so as to not present all the Reddit results in a row. They are many and it impoverishes the experience"""
import random
from mysql.connector import connect, Error
import click


def shuffle():
    """We open an access to sqlite db, shuffle it, then embelish the oputput"""
    try:
        conn = connect(
            host="localhost",
            user="mic",
            password="xxxx",
            database="rss")
        cur = conn.cursor()
        cur.execute('SELECT * FROM rss')
        rows = cur.fetchall()
        for row in rows:
            random.shuffle(list(row))   # https://tinyurl.com/yj9vahf7, 'row' is initially a tuple. We must change that. https://tinyurl.com/yzdk4e6y
            print(click.style(' - ', fg='bright_blue', bold=True), click.style(str(row[1]), fg='bright_blue', bold=True))
            print(click.style('  - ', fg='bright_cyan', bold=True), click.style(str(row[2]), fg='bright_cyan', bold=True))
            print(click.style('  - ', fg='bright_blue', bold=True), click.style(str(row[3]), fg='bright_blue', bold=True))
            print(click.style('  -', fg='bright_cyan', bold=True), click.style(str(row[4]), fg='bright_cyan', bold=True))
            print('\n')
    except Error as e:
        print("Error while connecting to db", e)
    finally:
        if(conn):
            conn.close()


if __name__ == "__main__":
    shuffle()


"""
NOTES:
1) - https://stackoverflow.com/questions/15234150/order-by-not-formatted-date-sqlite?rq=1
"""
