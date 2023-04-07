"""Here we concentrate all functionality of the app"""
from __future__ import unicode_literals

import sys

import isort
import questionary

from delete_rss import delete_rss, read_rss
from insert_db import delete_old, get_rss
from search_db import search
from show_rss import show_rss
from shuffle import shuffle
from sources_search import sources
from view_starred import view_starred


def rss():
    question = questionary.select(
        "What do you want to do?",
        choices=[
            "See Hacker News",
            "See Reddit Commandline ",
            "See Reddit Linux",
            "See Reddit Europe",
            "See Slashdot",
            "See Linux Journal",
            "See Quanta Magazine",
            "See Lobsters",
            "--------------------",
            "Add a feed",
            "Delete a feed",
            "Search the db",
            "Refresh db",
            "See db",
            "Shuffle db",
            "View Starred",
            "--------------------",
            "Exit",
        ],
    )
    answer = question.ask()

    if answer == "See Hacker News":
        # 1
        sources("Hacker News")
    if answer == "See Reddit Commandline":
        sources("Command Line")
    if answer == "See Reddit Linux":
        sources("linux")
    if answer == "See Reddit Europe":
        sources("europe")
    if answer == "See Ars Technica":
        sources("Linux Journal")
    if answer == "See Slashdot":
        sources("Slashdot: Linux")
    if answer == "Quanta Magazine":
        sources("Quanta Magazine")
    if answer == "Lobsters":
        sources("Lobsters")
    if answer == "Delete a feed":
        read_rss()
        delete_rss()
    if answer == "Search the db":
        search()
    if answer == "Refresh db":
        delete_old()
        get_rss()
    if answer == "See db":
        show_rss()
    if answer == "Shuffle db":
        shuffle()
    if answer == "View Starred":
        view_starred()
    if answer == "Exit":
        sys.exit()


rss()


"""
NOTES:
1) - It was needed to create a different search module for the choices in main, as oposed
to the module search_db, because the latter had a input field that was not needed when
you come from main, as the choice of action is already defined.
"""
