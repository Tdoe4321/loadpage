#! /usr/bin/env python
import urllib2, time

while True:
    response = urllib2.urlopen('https://tylergragg.com/')
    html = response.read()
    print(html)
    time.sleep(2400)
