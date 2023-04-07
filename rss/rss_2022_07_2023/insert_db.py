#!/usr/bin/env python
""" Module where  we'll clean the db of old entries and upload new ones"""
import subprocess

import feedparser
import isort  # noqa: F401
import mysql.connector as mc
import snoop
from dateutil.parser import parse
from mysql.connector import Error, connect

subprocess.run(["isort", __file__])


@snoop
def delete_old():
    """Opens a connection and erases all entries in the table 'rss'"""
    conn = connect(host="localhost", user="mic", password="xxxx", database="rss")
    cur = conn.cursor()
    inserir = "DELETE FROM rss;"
    cur.execute(
        inserir,
    ),
    conn.commit()


if __name__ == "__main__":
    delete_old()


@snoop
def get_rss():
    """Contains the code that defines the url of the rss, after we define what
    elements of the feed want."""

    # 6
    with open("/home/mic/python/rss/rss/url_list.txt") as f:
        urls = f.read().splitlines()

    index = 0

    try:
        conn = connect(host="localhost", user="mic", password="xxxx", database="rss")
        cur = conn.cursor()  # 1
        for url in urls:
            fp = feedparser.parse(url)
            nome = fp["feed"]["title"]
            print(nome)  # 2
            for index in range(len(fp.entries)):  # 3 # 4
                try:
                    titulo = fp.entries[index].title
                    titulo = str(titulo)
                    linque = fp.entries[index].link
                    linque = str(linque)
                    publi = fp.entries[index].published
                    publi = str(publi)
                    pub = parse(publi)
                    tempo = pub.strftime("%d/%m/%y")
                except KeyError:
                    try:
                        # 5
                        fp.entries[index].updated
                        publi = fp.entries[index].updated
                        publi = str(publi)
                        pub = parse(publi)
                        tempo = pub.strftime("%y/%m/%d")
                    except KeyError:
                        pass
                    except AttributeError:
                        pass
                    except mc.DataError:
                        pass
                    try:
                        fp.entries[index].pubDate
                        publi = fp.entries[index].pubDate
                        publi = str(publi)
                        pub = parse(publi)
                        tempo = pub.strftime("%y/%m/%d")
                    except KeyError:
                        pass
                    except AttributeError:
                        pass
                except AttributeError:
                    try:
                        fp.entries[index].updated
                        publi = fp.entries[index].updated
                        publi = str(publi)
                        pub = parse(publi)
                        tempo = pub.strftime("%y/%m/%d")
                    except KeyError:
                        pass
                    except AttributeError:
                        pass
                    try:
                        # 6
                        fp.entries[index].pubDate
                        publi = fp.entries[index].pubDate
                        publi = str(publi)
                        pub = parse(publi)
                        tempo = pub.strftime("%y/%m/%d")
                    except KeyError:
                        pass
                    except AttributeError:
                        pass
                inserir = "INSERT INTO rss (name, title, link, date) VALUES (%s, %s, %s, %s)"
                cur.execute(inserir, (nome, titulo, linque, tempo)),
                conn.commit()
    except Error as e:
        print("Error while connecting to db", e)
    finally:
        if conn:
            conn.close()
    print("Databse Updated")


if __name__ == "__main__":
    get_rss()

"""
NOTES:
1) - First we initialize the connection and the cursor. We then define the variable
name as the title of the feed attribute. This is done so we can get the name of
the publication.@bp.route("/login", methods=("GET", "POST"))
@snoop
def login():
    """
    Same pattern as before but for login.
    """

2) - Then we say that for each publication feed url in list 'urls', it should be
created a feedparser object.

3) - for each unique number that defines each content piece, we take out the
ones that have a item named 'title' and 'link' and turn them to strings

4) - As not all publications had the 'published' item, it was necessary to
place its extraction inside 'try/except' element, or the module would
stop with key and attribute errors.
Also, as it is a time element, the date format imported by the feed is not valid
in sqlite3. So it was necessary to change it to something more acceptable.
https://stackoverflow.com/questions/2265357/parse-date-string-and-change-format

5) - As the Reddit rss' don't have a published element, but have a updated one,
there was a need to create another if-exception block, so he could look on both

6) - How to read a file into a list.
See https://bit.ly/38TxQ4y
"""