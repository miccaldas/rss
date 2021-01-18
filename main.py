"""Here we concentrate all functionality of the app"""
import sys
import questionary

from questionary import Separator, Choice, prompt
from insert_db import delete_old, get_rss
from search_db import search
from show_rss import show_rss
from sources_search import sources


def main():
    question = questionary.select(
        'What do you want to do?',
        choices=[
                'See Hacker News',
                'See Hackaday',
                'See OSNews',
                'See Reddit Commandline',
                'See Reddit Europe',
                'See Roots of Progress',
                'See Slashdot',
                'See Slate Star Codex',
                'See Ars Technica',
                'See Hacker Noon',
                '--------------------',
                'Search the db',
                'Refresh db',
                'See db',
                '--------------------',
                'Exit',
                ],
    )
    answer = question.ask()
    print(answer)

    if answer == 'See Hacker News':
        # 1
        sources('Hacker News')
    if answer == 'See Hackaday':
        sources('hackaday')
    if answer == 'See OSNews':
        sources('osnews')
    if answer == 'See Reddit Commandline':
        sources('commandline')
    if answer == 'See Reddit Europe':
        sources('europe')
    if answer == 'See Roots of Progress':
        sources('rootsofprogress')
    if answer == 'See Slashdot':
        sources('slashdot')
    if answer == 'See Slate Star Codex':
        sources('slatestarcodex')
    if answer == 'See Ars Technica':
        sources('arstechnica')
    if answer == 'See Hacker Noon':
        sources('Hacker Noon')
    if answer == 'Search the db':
        search()
    if answer == 'Refresh db':
        delete_old()
        get_rss()
    if answer == 'See db':
        show_rss()
    if answer == 'Exit':
        sys.exit()


main()


"""
NOTES:
1) - It was needed to create a different search module for the choices in main, as oposed
to the module search_db, because the latter had a input field that was not needed when
you come from main, as the choice of action is already defined.
"""
