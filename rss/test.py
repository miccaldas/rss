"""
Module Docstring
"""
# import os
# import subprocess
import feedparser
import snoop
from blessed import Terminal
from snoop import pp


def type_watch(source, value):
    return "type({})".format(source), type(value)


snoop.install(watch_extras=[type_watch])


@snoop
def test():
    """"""


term = Terminal()

yc = feedparser.parse("https://news.ycombinator.com/rss")
lb = feedparser.parse("https://lobste.rs/rss")

for entry in yc.entries:
    print(entry.title)
    print(entry.link)


if __name__ == "__main__":
    test()
