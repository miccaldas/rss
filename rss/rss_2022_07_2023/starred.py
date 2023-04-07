"""Allows to star a rss entry, saving it for later reading."""
import click
import isort
import snoop
from mysql.connector import Error, connect
from snoop import pp


def type_watch(source, value):
    return "type({})".format(source), type(value)


snoop.install(watch_extras=[type_watch])


@click.command()
@click.option("-a", "--add", type=int)
@click.option("-d", "--delete", type=int)
@click.option("--delete_all/--no_delete_all", default=False)
# @snoop
def starred(add, delete, delete_all):
    """
    To create a starred entry, the user inputs an id, and
    we copy the corresponding entry to the 'starred' table.
    We use MySQL commands to delete one/some or all entries.
    """

    if add:
        try:
            conn = connect(host="localhost", user="mic", password="xxxx", database="rss")
            cur = conn.cursor()
            query = f"INSERT INTO starred (id, name, title, link) SELECT id, name, title, link FROM rss WHERE id = {add}"
            cur.execute(query)
            conn.commit()
        except Error as e:
            print("Error while connecting to the db", e)
        finally:
            if conn:
                conn.close()
        print(f"The article with the id {add} was starred.")

    if delete:
        try:
            conn = connect(host="localhost", user="mic", password="xxxx", database="rss")
            cur = conn.cursor()
            query = f"DELETE FROM starred WHERE id = {delete}"
            cur.execute(query)
            conn.commit()
        except Error as e:
            print("Error while connecting to the db", e)
        finally:
            if conn:
                conn.close()
        print(f"The article with the id {add} was deleted.")

    if delete_all:
        try:
            conn = connect(host="localhost", user="mic", password="xxxx", database="rss")
            cur = conn.cursor()
            query = "DELETE FROM starred"
            cur.execute(query)
            conn.commit()
        except Error as e:
            print("Error while connecting to the db", e)
        finally:
            if conn:
                conn.close()
        print("All starred articles were deleted.")


if __name__ == "__main__":
    starred()
