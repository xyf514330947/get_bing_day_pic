# -*- coding=utf-8 -*-

##########################################################
#   Desc    :   Get PageRank of a Website, for Python2
#   Author  :   iSayme
#   E-Mail  :   isaymeorg@gmail.com
#   Website :   http://www.isayme.org
#   Date    :   2012-09-18
##########################################################

import os
import time
import urllib
import platform

TOP_DIR = ""
COUNTRY = "en-US"
def get_platform():
    return platform.system()

def get_bing_pic() :
    # bing url
    url = "http://www.bing.com/"

    urllib.urlcleanup()
    args = urllib.urlencode({"setmkt" : COUNTRY}, {"setlang" : "match"})
    
    # open bing url
    page = urllib.urlopen(url, args)
    if None == page:
        print('open %s error' % (url))
        return -1

    # get html souce code
    data = page.read()
    if not data:
        print ('read %s content error' % url)
        return -1
    page.close()

    # parse picture url
    posleft = data.find(b'g_img={url:')
    if -1 == posleft:
        print ('jpg url not found')
        return -1
    posright = data.find(b'\'', posleft + 12)
    if -1 == posright:
        print ('jpg url not found')
        return -1    
    jpgpath = data[posleft + 12 : posright].decode("ascii");
    
    if 0 == cmp('/', jpgpath[0:1]):
        jpgurl = url + jpgpath
    else:
        jpgurl = jpgpath

    # make local file dir
    if 0 == cmp('Windows', get_platform()):
        localpath = TOP_DIR + time.strftime('bing\\%Y\\%m\\')
    else:
        localpath = TOP_DIR + time.strftime('bing/%Y/%m/')

    if not os.path.exists(localpath):
        os.makedirs(localpath)

    # make local file path
    localjpg = localpath + time.strftime('%d.jpg')

    print ("remote file : %s" % jpgurl)
    print ("local  file : %s" % localjpg)

    # download jpg file
    urllib.urlretrieve(jpgurl, localjpg) 

    urllib.urlcleanup()
    
    return 0
    

if __name__ == "__main__":
    print ("start get bing day picture ...")
    while 1:
        if 0 == get_bing_pic():
            print ("get picture ok")
            break;
        else:
            print ("get picture error")
            time.sleep(60)
