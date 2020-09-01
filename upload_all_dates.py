import requests
import time
import datetime

start_date = datetime.date(2020, 1, 1)
end_date = datetime.date(2020, 9, 1)
delta = datetime.timedelta(days=3)

while start_date <= end_date:
    print(start_date)
    r = requests.get('http://192.168.99.104:8085/date/'+ str(start_date))
    print (r)
    start_date += delta
    time.sleep(3)
