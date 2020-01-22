# -*- coding: utf-8 -*-

import urllib.request
udpaddr = '239.191.254.149:13343'
connect = urllib.request.urlopen ('http://proxytv.ru/iptv/php/onechan.php?=%s' % udpaddr)
udpxyaddr =  connect.read()
print (udpxyaddr)
