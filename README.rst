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
    $ source ~/virtualenv/ic-website/bin/activate
    $ complexity project/

Once you've done that, open a web browser to http://127.0.0.1:9090 to see the
newly generated static site.

Generate the website without running the server::

    $ complexity --noserver project/


Publishing
----------

Setup the following environment variables to configure AWS:
 * AWS_ACCESS_KEY_ID
 * AWS_SECRET_ACCESS_KEY
 * refs http://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html

Just run the following command:

    $ ./publish-ic-website


Complexity
----------
Check here for more details on complexity:
 * https://github.com/audreyr/complexity
