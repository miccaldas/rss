"""
Module that deletes the database before updating it.
We keep only the latest results in storage.
"""
import multiprocessing
import pickle
import sqlite3
from datetime import datetime
from multiprocessing import Pool
from time import mktime

import feedparser

# import snoop
# from snoop import pp


# def type_watch(source, value):
#     return "type({})".format(source), type(value)


# snoop.install(watch_extras=[type_watch])


# @snoop
def delete_entries():
    """
    Deletes all entries in the database. We only care about the
    latest content.\n
    .. code-block:: sql

        DELETE FROM rss
    """
    try:
        sqlite3.enable_callback_tracebacks(True)
        conn = sqlite3.connect("rss.db")
        cur = conn.cursor()
        query = "DELETE FROM rss"
        cur.execute(query)
        conn.commit()
    except sqlite3.Error as e:
        print("Error connecting to the db", e)
    finally:
        if conn:
            conn.close()


if __name__ == "__main__":
    delete_entries()


# @snoop
def upload_feed(answers):
    """
    Parses all feeds and uploads them to the database.
    Uses multiprocessing to speed up the process.\n
    .. code-block:: sql

        INSERT INTO rss (name, title, link, time) VALUES (?1, ?2, ?3; ?4)
    """

    try:
        sqlite3.enable_callback_tracebacks(True)
        conn = sqlite3.connect("rss.db")
        cur = conn.cursor()
        query = "INSERT INTO rss (name, title, link, time) VALUES (?1, ?2, ?3, ?4)"
        cur.execute(query, answers)
        conn.commit()
    except sqlite3.Error as e:
        print("Error connecting to the db", e)
    finally:
        if conn:
            conn.close()


if __name__ == "__main__":
    with open("feedlst.bin", "rb") as v:
        feeds = pickle.load(v)
    answers = []
    for feed in feeds:
        fs = feedparser.parse(feed[1])
        name = fs.feed.title
        print(f"    {name}")
        for entry in fs.entries:
            title = entry.title
            link = entry.link
            time = datetime.fromtimestamp(mktime(entry.published_parsed))
            answer = [name, title, link, time]
            answers.append(answer)
    with Pool() as pool:
        pool.map(upload_feed, answers)
