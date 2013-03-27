# for python3
# 2012-06-13, Guoqiang Wu, www.isayme.org

import os
import time
import urllib.request
import platform

TOP_DIR = ""

def get_platform():
    return platform.system()

# get jpg function, and save
def get_bing_jpg() :
    url = r'http://www.bing.com'
    page = urllib.request.urlopen(url)
    if None == page:
        print('open %s error' % (url))
        return -1
    data = page.read()
    if not data:
        print ('read %s content error' % url)
        return -1
    page.close()

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
    localjpg = localpath + time.strftime('%d.jpg')

    print ("remote file : %s" % jpgurl)
    print ("local  file : %s" % localjpg)
    urllib.request.urlretrieve(jpgurl, localjpg) 
    
    return 0
    

if __name__ == "__main__":
    print ("start get bing day picture ...")
    while 1:
        if 0 == get_bing_jpg():
            print ("get picture ok")
            break;
        else:
            print ("get picture error")
            time.sleep(600)
