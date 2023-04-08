"""
Module Docstring
"""
import random

import snoop
from blessed import Terminal

# from configs.config import Efs, tput_config
# import os
# import subprocess
from dotenv import load_dotenv
from snoop import pp


def type_watch(source, value):
    return "type({})".format(source), type(value)


snoop.install(watch_extras=[type_watch])

load_dotenv()


@snoop
def test():
    """"""
    term = Terminal()

    sources = [(87, 155, 177), (199, 233, 176), (255, 191, 169), (236, 229, 199)]

    starter = random.choice(sources)
    one = starter[0]
    two = starter[1]
    three = starter[2]

    print(term.color_rgb(one, two, three) + "This is the starter" + term.normal)

    name_text = term.color_rgb((one - 60), (two - 60), (three - 60))
    print(name_text + "This is text color" + term.normal)

    twenty = term.color_rgb((one + 20), (two + 20), (three + 20))
    print(twenty + "This is starter plus 20" + term.normal)

    fourty = term.color_rgb((one + 40), (two + 40), (three + 40))
    print(fourty + "This is starter plus 40" + term.normal)
    print(
        term.color_rgb((one + 60), (two + 60), (three + 60))
        + "This is starter plus 60"
        + term.normal
    )
    pp(one + 60)
    pp(two + 60)
    pp(three + 60)


if __name__ == "__main__":
    test()
