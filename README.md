metrics_talk
============

Gathering and visualizing metrics with ZeroMQ, Redis & Graphite

I gave this talk at PyCon Japan in September, 2012.

Video: http://youtu.be/FTGdLnx_ep0?t=3m25s


Server setup
============

These scripts were tested on Ubuntu server 12.04

Install prerequisites:

    $ sudo apt-get install python-redis redis-server
    $ sudo apt-get install memcached python-dev python-pip sqlite3 libcairo2 libcairo2-dev python-cairo pkg-config 
    $ sudo apt-get install supervisor  

Setting up Graphite
===================

I followed these instructions:
http://marcelo-olivas.blogspot.jp/2012/06/installing-graphite-on-ubuntu-1204.html


Also, the example glue scripts send data very frequently, so we need more granularity in the default Round-Robin databases.
Change /opt/graphite/conf/storage-scemas.conf:

    [default_5sec_for_1day]
    pattern = .*
    retentions = 5s:1d
~                           


