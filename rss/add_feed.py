"""
Module to add feeds to the application.
"""
import os
import pickle

import feedparser

# import snoop
# from snoop import pp


# def type_watch(source, value):
#     return "type({})".format(source), type(value)


# snoop.install(watch_extras=[type_watch])


# @snoop
def add_feed(feeds):
    """
    Function is started with a string with an url or a list of urls.
    Each url is ran through *feedparser* to get the feed title.
    Creates a tuple of the feed title and its url. Adds it to the
    *feedlst.bin* file.
    """

    if type(feeds) is str:
        lst = [feeds]
    if type(feeds) is list:
        lst = feeds

    new_feeds = []
    for ls in lst:
        fs = feedparser.parse(ls)
        name = fs.feed.title
        tup = (name, ls)
        new_feeds.append(tup)

    cwd = os.getcwd()
    filelst = os.listdir(cwd)
    if "feedlst.bin" in filelst:
        with open("feedlst.bin", "rb") as f:
            feedlst = pickle.load(f)
        for tup in new_feeds:
            feedlst += [tup]
    else:
        feedlst = new_feeds

    with open("feedlst.bin", "wb") as f:
        pickle.dump(feedlst, f)


if __name__ == "__main__":
    add_feed()
