import urllib2
import json

def ACheck():
    uid = ""
    uname = []

    with open('uname.txt', 'r') as f:
        for username in f:
uname.append(str(username))
        uid += str(json.load(urllib2.urlopen('http://uhunt.felix-halim.net/api/uname2uid/'  + username))) + ','

    result = json.load(urllib2.urlopen('http://uhunt.felix-halim.net/api/solved-bits/' + uid ))

    cnt = 0

    for user in result:
        count = 0
        for bits in user['solved']:
            while bits != 0:
                count += bits & 1
                bits = bits >> 1
        print uname[cnt][:-1] + ': ' + str(count)
        cnt += 1

def addPid(filename):

    psetf = open('pset.txt')
    for subset in psetf:
        pset.append(subset)
    with open(filename, 'r') as f:
        for pnum in f:
            out.write(json.load(urllib2.urlopen('http://uhunt/felix=halim.net/api/p/num/' + pnum))['num'] + ' ')
        
            
