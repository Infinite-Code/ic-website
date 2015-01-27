=====
Setup
=====

Source code for our Infinite Code website.

Install python packages::

    $ virtualenv ~/virtualenv/ic-website
    $ source ~/virtualenv/ic-website/bin/activate
    $ pip install -r requirements.txt

Generate the website::

    $ cd ic-website
    $ complexity project/

Once you've done that, open a web browser to http://127.0.0.1:9090 to see the
newly generated static site.

Generate the website without running the server::

    $ complexity --noserver project/
