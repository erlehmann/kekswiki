Prerequisites
=============

Kekswiki requires [Pylons][1], [Dulwich][2] and [html5lib][3]. On a Debian-based system you can get all of these by issuing the following command as root:

    apt-get install python-pylons python-dulwich python-html5lib


Installation and Setup
======================

    paster setup-app development.ini
    paster serve --reload development.ini

Caution: Always set “debug = false” in configuration files for production sites and make sure your users do to.


Testing
=======

A rudimentary set of unit tests is available. Try it with:

    nosetests --with-pylons=test.ini


[1]: http://pylonshq.com/

[2]: http://samba.org/~jelmer/dulwich/

[3]: http://code.google.com/p/html5lib/
