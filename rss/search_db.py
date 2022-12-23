"""This moodule is concerned with all searches to be done in db, that are defined by the user"""
import click
from mysql.connector import Error, connect
from rich import print
from rich.console import Console


def search():
    """Here we query the user about what he's looking for."""
    console = Console()
    query = input(click.style("What's your query? ", fg="bright_white", bold=True))
    try:
        conn = connect(host="localhost", user="mic", password="xxxx", database="rss")
        cur = conn.cursor()
        expression = "SELECT id, name, title, link, date FROM rss WHERE MATCH(name, title) AGAINST (%s)"
        cur.execute(expression, (query,))
        record = cur.fetchall()
        for row in record:
            id = row[0]  # noqa: F841
            name = row[1].upper()  # noqa: F841
            title = row[2]  # noqa: F841
            link = row[3]  # noqa: F841
            date = row[4]  # noqa: F841
            print(f"[bold #eac784] <+ {id} +>[/bold #eac784]")
            print(f"[bold #a39193] @ {name}[/bold #a39193]")
            print(f"[bold #eea990] @ {title}[/bold #eea990]")
            print(f"[bold #eea990] @ {date}[bold, #eea990]")
            print(f"[bold #ff6700] @ {link}[bold #ff6700]")
            print("\n")
            console.rule("[bold #66545e][+ + + +]")
            print("\n")
    except Error as e:
        print("Error while connecting to db", e)
    finally:
        if conn:
            conn.close()


if __name__ == "__main__":
    search()
