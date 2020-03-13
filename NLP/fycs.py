import hashlib
import requests
import json

def fy(q):
    error = 'None'
    salt = '25498'

    base = "https://api.fanyi.baidu.com/api/trans/vip/translate"
    appid = "20200303000392203"
    key = "_rkEepOZdcXkL_DebWus"
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
    except KeyError:
        return error



q = "I really like this hairdryer. I haven't had it very long. But it's working well for me."

a = fy(q)

print(a)