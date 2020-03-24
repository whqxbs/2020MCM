
from aip import AipNlp
import time
import json
import pandas as pd

#API Information
APP_ID = 'xxx'
API_KEY = 'xxx'
SECRET_KEY = 'xxx'

client = AipNlp(APP_ID, API_KEY, SECRET_KEY)

def donlp(text):
    res=client.sentimentClassify(text);
    return res

print(donlp('变得非常热-我在金属炉rate和塑料主体上都烫过手。 使用后，我必须放在柜台上，因为它太热而无法收起。 它融化了2种不同的梳子，现在在使用过程中开始冒烟。 我的头发需要高温才能完全干燥并且不会卷曲，但这是不安全和荒谬的。 当我的新型号（不是该品牌）到货时，这一切将成为垃圾！'))
