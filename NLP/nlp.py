from aip import AipNlp
import time
import json
import pandas as pd
import hashlib
import requests
import xlwt

#API Information
APP_ID = 'xxx'
API_KEY = 'xxx'
SECRET_KEY = 'xxx'

client = AipNlp(APP_ID, API_KEY, SECRET_KEY)

def donlp(text):
    error = 'None'
    try:
        res=client.sentimentClassify(text);
        return res
    except:
        return error

def fy(q):
    error = 'None'
    salt = 'xxx'

    base = "https://api.fanyi.baidu.com/api/trans/vip/translate"
    appid = "xxx"
    key = "xxx"
    mid = appid+q+salt+key

    m = hashlib.md5()
    b = mid.encode(encoding='utf-8')
    m.update(b)
    ret = m.hexdigest()

    url = base+"?q="+q+"&from=aoto&to=zh&appid=20200303000392203&salt="+salt+"&sign="+ret

    midres = requests.get(url)
    midres.encoding='raw-unicode-escape'
    try:
        ff = midres.text
        ff1 = json.loads(ff)['trans_result'][0]['dst']
        return ff1
    except :
        return error

#begin
train=pd.read_csv('Result3.csv')
feel = xlwt.Workbook (encoding= 'utf-8') #创建表格
feels = feel.add_sheet('心情')
#file1 = open('Result.txt','w')

for i in range(18939):
    try:
        mid=train['review_body'].loc[i:i].values[0]
        midp='"'+mid+'"'
        mid1=fy(midp)
        a = donlp(mid1)["items"][0]['sentiment']
        #print(a)
        if a==2:
            #print("enthusiastic")
            #file1.write("enthusiastic\n")
            feels.write (i, 0, "enthusiastic")
        elif a==0:
            #print("disappointed")
            #file1.write("disappointed\n")
            feels.write (i, 0, "disappointed")
        elif a==1:
            #print("middle")
            #file1.write("middle\n")
            feels.write (i, 0, "middle")
        print(i)
        time.sleep(0.5)
    except:
        feels.write (i, 0, "None")
feel.save('心情.xls')
#test = "11111"11470
#a = donlp(test)["items"][0]['sentiment']
