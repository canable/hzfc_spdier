# _*_ coding:utf-8 _*_

import requests
import bs4
import re
import time
import random
import pickle,pprint

class hzfcSpider():
    def __init__(self):
        pass



    def getResp(self,url):
        cookie = {'Cookie':'PHPSESSID=km7c2bqs5v7mk2enmuuc21e0o3; _gscu_738743822=74538044lxbdnz83; _gscs_738743822=74538044o4dhi683|pv:25; _gscbrs_738743822=1'}

        header = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36',
                  'Referer':'http://www.hzfc.gov.cn/scxx/'
        }
        contents = []
        resp = requests.get(url,cookies = cookie,headers = header ).content.encode('utf-8')
        soup = bs4.BeautifulSoup(resp,'html.parser')
        contAll = soup.find_all('a',attrs = {'href':re.compile(r'.*lpid.*\d$')})
        for cont in contAll:
            if cont.string==None:
                content = cont.get_text()
                print content
                contents.append(content)
            else:
                contents.append(cont.string)
                print cont.string
        #time.sleep(random.uniform(1,5))
        time.sleep(1)
        return contents

    def main(self):
        titleList = []
        titles = self.getResp()
        for title in titles:
            print title
            #titleStr = titles.string
            #titleList.append(titleStr)
        #return titleList

    def pikData(self,dataUrl):
        dataFile = open(dataUrl,'rb')
        data = pickle.load(dataFile)
        pprint.pprint(data)
        dataFile.close()

if __name__ == '__main__':
    t1 = time.time()
    url='http://www.hzfc.gov.cn/scxx/xmcx_more.php'
    totolPage = 49
    i = 1
    contents = []
    stm = time.strftime('%Y%m%d%H%M%S',time.localtime())

    while i < totolPage+1:
        content = hzfcSpider().getResp(url)
        print 'getting page %d'%i
        contents.append(content)
        i +=1
        url = 'http://www.hzfc.gov.cn/scxx/xmcx_more.php?page='+str(i)+'&cqid=&key=&select_type='
    try:
        f = open(r'F:\\py\\pydemo\\hzfc\\'+stm+'.pkl','ab+')
        pickle.dump(contents,f)
        f.close()
    except IOError , e:
        print e
    t2 = time.time()
    print '用时 %ds'%(t2-t1)

    #test data
    #hzfcSpider().pikData(r'F:\\py\\pydemo\\hzfc\\20160923.pkl')