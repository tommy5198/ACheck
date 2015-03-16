import urllib2
import os
import json

pset = {}

def ACheck():
    global pset
    uid = ""
    uname = []

    with open('uname.txt', 'r') as f:
        for username in f:
            uname.append(str(username))
            uid += str(json.load(urllib2.urlopen('http://uhunt.felix-halim.net/api/uname2uid/'  + username))) + ','

    result = json.load(urllib2.urlopen('http://uhunt.felix-halim.net/api/solved-bits/' + uid ))
    cnt = 0

    for user in result:
        print uname[cnt][:-1] + ': '
        total = 0
        for hw in pset.keys():
            count = 0
            for pid in pset[hw]:
                i = pid % 32
                j = (pid - i) / 32
                if len(user['solved']) > j:
                    count += (user['solved'][j] >> i) & 1
            print str(count) + ' '
            total += count
        cnt += 1
        print str(total)

def addPid():
    global pset
    filenames = [f for f in os.listdir('hw/')]
    for hw in filenames:
        pset[hw] = []
        with open('hw/' + hw, 'r') as f:
            for pnum in f:
                pset[hw].append(json.load(urllib2.urlopen('http://uhunt.felix-halim.net/api/p/num/' + pnum))['pid'])

addPid()
ACheck()
