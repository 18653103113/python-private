import glob

glob.glob('*.py')

import datetime

#今天
today = datetime.date.today()
print(today)

#昨天
yesterday = today - datetime.timedelta(days=1)
print(yesterday)

#上个月
last_month = today.month - 1 if today.month - 1 else 12
print(last_month)

#datetime转字符串
today_str = today.strftime("%Y-%m-%d")
print(today_str)

#字符串转datetime
today = datetime.datetime.strptime(today_str, "%Y-%m-%d")
print(today)

#补时差
today + datetime.timedelta(hours=8)