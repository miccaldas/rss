"""
Updates, chooses and collects feed data, asked by the user.
"""
from __future__ import unicode_literals

import sqlite3
import subprocess

import questionary

# import snoop
from questionary import Separator, Style

# from snoop import pp


# def type_watch(source, value):
#     return "type({})".format(source), type(value)


# snoop.install(watch_extras=[type_watch])

custom_style_monitor = Style(
    [
        ("qmark", "fg:#FFACAC bold"),
        ("question", "fg:#FFBFA9 bold"),
        ("answer", "fg:#FFEBB4"),
        ("pointer", "fg:#FBFFB1 bold"),
        ("highlighted", "fg:#CCD5AE bold"),
        ("selected", "fg:#E9EDC9 bold"),
        ("separator", "fg:#FEFAE0"),
        ("instruction", "fg:#E4CDA7"),
        ("text", "fg:#F8CBA6 bold"),
    ]
)


# @snoop
def update_query():
    """
    Asks the user if he wants to update the database.\n
    :command: Do you want to update the results?
    :command: python update.py
    """

    # Suggested by Sourcery. I had a confirmation question that resolved to
    # to True or False. If True, do the subprocess command. Sourcery changed
    # it to walrus operator that enables to assign inside a if statement.
    if updt := questionary.confirm(
        qmark="    [+]",
        style=custom_style_monitor,
        message=" Do you want to update the results?",
    ).ask():
        cmd = "/usr/bin/python /home/mic/python/rss/rss/newrss/update.py"
        subprocess.run(cmd, shell=True)


# @snoop
def choose_feeds():
    """
    Selects entries in the *name* column and displays the results.
    The user can choose, one, many or all.\n
    .. code-block:: sql

        SELECT DISTINCT name FROM rss

    :command: What feeds do you want to see?
    :returns: feedschoice
    """
    try:
        sqlite3.enable_callback_tracebacks(True)
        conn = sqlite3.connect("rss.db")
        cur = conn.cursor()
        query = "SELECT DISTINCT name FROM rss"
        cur.execute(query)
        records = cur.fetchall()
    except sqlite3.Error as e:
        print("Error connecting to the db", e)
    finally:
        if conn:
            conn.close()

    recs = [i for g in records for i in g]
    recs += ["All", "-----------------------", "Exit"]

    return questionary.checkbox(
        message=" What feeds do you want to see?",
        choices=recs,
        qmark="    [+]",
        pointer="   »»",
        style=custom_style_monitor,
        initial_choice="All",
    ).ask()


# @snoop
def get_feeds():
    """
    Gets the feed information for the publications chosen
    in the last function. It has different queries in case
    its various feeds, one feed, all feeds.\n
    .. code-block:: sql

        SELECT * FROM rss WHERE name IN <choices> ORDER BY RANDOM
        SELECT * FROM rss WHERE name = '{choices[0]}'
        SELECT * FROM rss

    :returns: records
    """
    update_query()
    chcs = choose_feeds()
    choices = tuple(chcs)

    try:
        sqlite3.enable_callback_tracebacks(True)
        conn = sqlite3.connect("rss.db")
        cur = conn.cursor()
        if choices[0] == "All":
            query = "SELECT name, title, link, time FROM rss ORDER BY RANDOM()"
            cur.execute(query)
        if choices[0] == "Exit":
            # Python was throwing an error whenever 'Exit' was used. This silences it.
            try:
                raise SystemExit
            except SystemExit:
                print(" ")
        if len(choices) > 1:
            query = f"SELECT name, title, link, time FROM rss WHERE name IN {choices} ORDER BY RANDOM()"
            cur.execute(query)
        if len(choices) == 1 and choices[0] not in ["All", "Exit"]:
            query = f"SELECT name, title, link, time FROM rss WHERE name = '{choices[0]}'"
            cur.execute(query)
        records = cur.fetchall()
    except sqlite3.Error as e:
        print("Error connecting to the db", e)
    finally:
        if conn:
            conn.close()
        return records


if __name__ == "__main__":
    get_feeds()
