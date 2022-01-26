"""This module is here because it's a bitch to take data from a db, put it
   in a file, and still keep it organized. So it's best just to handle it
   always as a virtual entity."""
import subprocess

import isort  # noqa: F401
import snoop
from loguru import logger
from mysql.connector import Error, connect

fmt = "{time} - {name} - {level} - {message}"
logger.add("../logs/info.log", level="INFO", format=fmt, backtrace=True, diagnose=True)
logger.add("../logs/error.log", level="ERROR", format=fmt, backtrace=True, diagnose=True)

subprocess.run(["isort", __file__])


@logger.catch
@snoop
def pylist():
    """We take out the links and the titles from the rss entries,
    to create a online rss app."""
    try:
        conn = connect(host="localhost", user="mic", password="xxxx", database="rss")
        cur = conn.cursor()
        cur.execute("SELECT title, link FROM rss")
        rows = cur.fetchall()
    except Error as e:
        print("Error while connecting to db", e)
    finally:
        if conn:
            conn.close()

    rows = [tuple(ele for ele in sub if ele != "Upgrading a motherboard’s BIOS/UEFI (the hard way)") for sub in rows]  # 1
    new_rows = [i for i in rows if len(i) == 2]  # Had to remove the other element of tuple. Condition is that tuple should have 2 elements.
    newest_rows = [index for (index, a_tuple) in enumerate(new_rows) if a_tuple[1] == "Show HN: Python decorator that enables arbitrarily-deep tail/non-tail recursion"]

    return newest_rows


if __name__ == "__main__":
    pylist()


# 1 - It was needed to remove an entry on the list, as Ididn't knew the index, I used a list comprehension.
# What it does is create a condition that said entry will necessarily fail.
