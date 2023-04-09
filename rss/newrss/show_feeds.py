"""
Module to decorate the feed data and present it.
"""
import pickle
import random

# import snoop
from blessed import Terminal

from choice_feeds import get_feeds

# from snoop import pp


# def type_watch(source, value):
#     return "type({})".format(source), type(value)

# snoop.install(watch_extras=[type_watch])


class DecorateShowFeeds:
    """
    1.  Imports the data of chosen feeds.
    2.  Defines color pallettes to decorate each feed.
    3.  Alocates a pallette to a feed.
    4.  Shows feeds in terminal.
    """

    def __init__(self):
        pass

    # @snoop
    def records(self):
        """
        Runs *get_feeds* module to ask the user what information he wants to see.\n
        As *get_feeds* uses multiprocessing, it can't be imported traditioanlly, so
        we call it, through *subprocess*, with a *python* command.\n
        :command: python get_feeds.py
        """
        self.records = get_feeds()

    def pallettes(self):
        """
        Color pallettes to be atributed randomly to each chosen feed.
        Creates a list of pallettes that'll be used in the next method.
        """
        self.orange = {
            "bkgrd": (255, 96, 0),
            "text": (255, 230, 199),
            "title": (255, 96, 0),
            "time": (255, 96, 0),
        }
        self.brown_green = {
            "bkgrd": (171, 196, 170),
            "text": (103, 93, 80),
            "title": (171, 196, 170),
            "time": (171, 196, 170),
        }
        self.pink = {
            "bkgrd": (228, 147, 147),
            "text": (36, 89, 83),
            "title": (228, 147, 147),
            "time": (228, 147, 147),
        }
        self.acid_lemon = {
            "bkgrd": (210, 230, 3),
            "text": (62, 151, 139),
            "title": (210, 230, 3),
            "time": (210, 230, 3),
        }
        self.aquamarine = {
            "bkgrd": (0, 173, 181),
            "text": (238, 238, 238),
            "title": (0, 173, 181),
            "time": (0, 173, 181),
        }
        self.toasted_yellow = {
            "bkgrd": (255, 192, 105),
            "text": (74, 54, 58),
            "title": (255, 192, 105),
            "time": (255, 192, 105),
        }
        self.softgreens = {
            "bkgrd": (66, 133, 91),
            "text": (210, 215, 159),
            "title": (210, 215, 159),
            "time": (210, 215, 159),
        }
        self.lightblue = {
            "bkgrd": (160, 195, 210),
            "text": (247, 245, 235),
            "title": (160, 195, 210),
            "time": (160, 195, 210),
        }
        self.grey = {
            "bkgrd": (104, 121, 128),
            "text": (243, 189, 161),
            "title": (243, 189, 161),
            "time": (243, 189, 161),
        }
        self.brown = {
            "bkgrd": (202, 191, 171),
            "text": (65, 68, 75),
            "title": (202, 191, 171),
            "time": (202, 191, 171),
        }

        self.pallette_lst = [
            self.orange,
            self.brown_green,
            self.pink,
            self.acid_lemon,
            self.aquamarine,
            self.toasted_yellow,
            self.softgreens,
            self.lightblue,
            self.grey,
            self.brown,
        ]

    # @snoop
    def name_to_pallette(self):
        """
        Creates a list of tuples with a chosen feed name and a pallette.\n
        We want different pallettes for each publication. For this we need to ensure
        that, everytime that 'random' chooses a new pallette, there is only unused
        pallettes as options. To do this, we pop the used options out of the list of
        choices. It creates a *self.name_pallette* list, with tuples with the feed
        name and the its pallette.
        """
        rawnames = [i[0] for i in self.records]
        nms = set(rawnames)
        # We'll need, further along, to choose a name by index. That is not possible
        # in a set. So we need to turn it into a list.
        names = list(nms)
        self.name_pallette = []
        # This is the list that'll have its elements popped.
        chosen_pallettes = self.pallette_lst
        for i in range(len(names)):
            # Pallette choice.
            plt = random.choice(chosen_pallettes)
            # Append tuple with name of feed and its pallette.
            self.name_pallette.append((names[i], plt))
            # Get index of pallette in 'chosen_pallettes'.
            idx = chosen_pallettes.index(plt)
            # Remove it from list.
            chosen_pallettes.pop(idx)

    # @snoop
    def show_feeds(self):
        """
        Alocates pallette values to the feed content, using *Blessed* terminology.
        Shows the results.
        """
        term = Terminal()
        decoratedentries = []
        for i in self.records:
            for d in self.name_pallette:
                if i[0] == d[0]:
                    pub = (
                        term.bold
                        + term.on_color_rgb(d[1]["bkgrd"][0], d[1]["bkgrd"][1], d[1]["bkgrd"][2])
                        + term.color_rgb(d[1]["text"][0], d[1]["text"][1], d[1]["text"][2])
                        + i[0]
                        + term.normal
                    )
                    ttl = term.color_rgb(d[1]["title"][0], d[1]["title"][1], d[1]["title"][2]) + term.bold + i[1]
                    title = term.link(i[2], term.truncate(ttl, 100))
                    time = term.color_rgb(d[1]["time"][0], d[1]["time"][1], d[1]["time"][2]) + i[3]
                    decoratedentries.append((pub, title, time))
        for entry in decoratedentries:
            for line in entry:
                print("".join(term.wrap(line, width=250, initial_indent=" " * 30)))
            print("\n")
