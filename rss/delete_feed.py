"""
Module to delete feeds from the feed list.
"""
import os
import pickle

# import snoop
# from snoop import pp


# def type_watch(source, value):
#     return "type({})".format(source), type(value)


# snoop.install(watch_extras=[type_watch])


# @snoop
def delete_feed(dels):
    """
    Gets a feed or list of feeds to delete, builds new *feedlst.bin* file without them.
    """
    splitlst = []
    if type(dels) is str:
        feeds = [dels]
    if type(dels) is list:
        feeds = dels

    filelst = os.listdir(os.getcwd())

    if "feedlst.bin" in filelst:
        poplst = []
        with open("feedlst.bin", "rb") as f:
            feedlst = pickle.load(f)
        new = [i for i in feedlst if i[0] not in feeds]
        with open("feedlst.bin", "wb") as v:
            pickle.dump(new, v)
    else:
        print("There's no feedlst.bin file in this folder.")


if __name__ == "__main__":
    delete_feed()
