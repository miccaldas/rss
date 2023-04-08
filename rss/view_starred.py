"""Shows content of the 'starred' table."""
import isort
import snoop
from snoop import pp
import click
from mysql.connector import connect, Error


def type_watch(source, value):
    return "type({})".format(source), type(value)


snoop.install(watch_extras=[type_watch])


# @snoop
def view_starred():
    """
    Creates Mysql Query to show the
    'starred' table contents.
    """

    try:
        conn = connect(host="localhost", user="mic", password="xxxx", database="rss")
        cur = conn.cursor()
        query = "SELECT * FROM starred"
        cur.execute(query)
        conn.commit()

    except Error as e:
        print("Error while connecting to db", e)
    finally:
        if conn:
            conn.close()


if __name__ == "__main__":
    view_starred()
