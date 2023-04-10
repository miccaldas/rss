"""
Main module of *rss*. Initiates the application.
"""
import pickle

import questionary

# import snoop
from questionary import Separator, Style

from rss.add_feed import add_feed
from rss.delete_feed import delete_feed
from rss.show_feeds import DecorateShowFeeds

# from snoop import pp


# def type_watch(source, value):
#     return "type({})".format(source), type(value)


# snoop.install(watch_extras=[type_watch])


# @snoop
def main():
    """
    Collects user input about:\n
    1. What functionality to use.
    2. If it's *delete feeds*, what feeds to delete?
    3. If it's *add feeds*, what urls do you want to add?
    4. If it's *show feeds*, what feeds do you want to see?

    :command: What do you want to do?
    :command: What feeds do you want to delete?
    :command: What feeds do you want to add?
    """
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

    print("\n")
    query = questionary.select(
        message=" What do you want to do?",
        choices=[
            " See Feeds",
            " Delete Feeds",
            " Add Feeds",
            Separator(" --------------"),
            " Exit",
        ],
        qmark="    [+]",
        pointer="   »»",
        style=custom_style_monitor,
    ).ask()

    if query == " See Feeds":
        dec = DecorateShowFeeds()
        dec.records()
        dec.pallettes()
        dec.name_to_pallette()
        dec.show_feeds()

    if query == " Delete Feeds":
        with open("feedlst.bin", "rb") as f:
            feedlst = pickle.load(f)
        names = [i[0] for i in feedlst]
        names += [" ------------------------", "Exit"]
        dels = questionary.checkbox(
            message=" What feeds do you want to delete?",
            qmark="    [+]",
            choices=names,
            style=custom_style_monitor,
            multiline=True,
            pointer="   »»",
        ).ask()
        if query == "Exit":
            try:
                raise SystemExit
            except SystemExit:
                print(" ")
        else:
            delete_feed(dels)

    if query == " Add Feeds":
        adds = questionary.text(
            " Write the urls for the feeds you want to add.",
            qmark="    [+]",
            style=custom_style_monitor,
            multiline=True,
        ).ask()
        if "\n" in adds:
            feeds = adds.split("\n")
            add_feed(feeds)
        else:
            add_feed(adds)


if __name__ == "__main__":
    main()