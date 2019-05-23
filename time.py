import time

day = time.localtime().tm_wday
date = str(time.localtime().tm_mday)+'.'+str(time.localtime().tm_mon)+'.'+str(time.localtime().tm_year)
hour = str(time.localtime().tm_hour)+':'+str(time.localtime().tm_min)+':'+str(time.localtime().tm_sec)
dYear = str(time.localtime().tm_yday)
days = {
    0:'Monday',
    1:'Tuesday',
    2:'Wednesday',
    3:'Thursday',
    4:'Friday',
    5:'Saturday',
    6:'Sunday'
}
for d in days.keys():
    if d == day:
        print('Today is',days.get(d),', the',dYear,'day of year,',date,',',hour)

print(time.asctime())