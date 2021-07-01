"""This module shows the content of the db. Turned it to a module, so I can separate changing
the db and seeing it"""
import click
from mysql.connector import connect, Error


def show_rss():
    """We open an access to db, then embelish the oputput"""
    try:
        conn = connect(
            host="localhost",
            user="mic",
            password="xxxx",
            database="rss")
        cur = conn.cursor()
        cur.execute('SELECT * FROM rss ORDER BY date ASC')  # 1
        rows = cur.fetchall()
        for row in rows:
            print(click.style(' ⟫ - ', fg='bright_blue', bold=True), click.style(str(row[1]), fg='bright_blue', bold=True))
            print(click.style(' ⟫ - ', fg='bright_cyan', bold=True), click.style(str(row[2]), fg='bright_cyan', bold=True))
            print(click.style(' ⟫ - ', fg='bright_blue', bold=True), click.style(str(row[3]), fg='bright_blue', bold=True))
            print(click.style(' ⟫ -', fg='bright_cyan', bold=True), click.style(str(row[4]), fg='bright_cyan', bold=True))
            print('\n')
    except Error as e:
        print("Error while connecting to db", e)
    finally:
        if(conn):
            conn.close()


if __name__ == "__main__":
    show_rss()


"""
NOTES:
1) - https://stackoverflow.com/questions/15234150/order-by-not-formatted-date-sqlite?rq=1
"""
