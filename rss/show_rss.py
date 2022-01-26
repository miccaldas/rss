"""This module shows the content of the db. Turned it to a module, so I can separate changing
the db and seeing it"""

from mysql.connector import Error, connect
from rich import print
from rich.console import Console


def show_rss():
    """We open an access to db, then embelish the oputput"""
    console = Console()
    try:
        conn = connect(host="localhost", user="mic", password="xxxx", database="rss")
        cur = conn.cursor()
        cur.execute("SELECT * FROM rss ORDER BY date ASC")  # 1
        rows = cur.fetchall()
        for row in rows:
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
    show_rss()


"""
NOTES:
1) - https://stackoverflow.com/questions/15234150/order-by-not-formatted-date-sqlite?rq=1
"""
