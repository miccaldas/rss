Modules
=======

Introduction
------------
For this update, there was a desire to simplify processes, and minimize the proliferation of modules. This means, as long as it makes makes sense, to have one module per functionality. Meaning: one module for deleting, another for adding and so on and so forth. But here I broke this rule with the *choice_feeds.py* module, It gets and treats all the feeds information. This, in principle, should be aggregated with the *show_feeds.py* module, but the truth is that there is a lot of user input regarding what feeds are used and when. Also these user choices have to be treated differently, as per the question or the answers. Taking into account the complexity that is involved in this step, it made sense to me that it should have its own module.

Add Feeds
---------
.. automodule:: rss.add_feed
.. autofunction:: add_feed

Delete Feeds
------------
.. automodule:: rss.delete_feed
.. autofunction:: delete_feed

Update Feeds
------------
.. automodule:: rss.update
.. autofunction:: delete_entries
.. autofunction:: upload_feed

Choose Feeds
------------
.. automodule:: rss.choice_feeds
.. autofunction:: update_query
.. autofunction:: choose_feeds
.. autofunction:: get_feeds

Show Feeds
----------
.. automodule:: rss.show_feeds
.. autoclass:: DecorateShowFeeds

    .. automethod:: records
    .. automethod:: pallettes
    .. automethod:: name_to_pallette
    .. automethod:: show_feeds

Main Module
-----------
.. automodule:: rss.main
.. autofunction:: main
