"""
https://docs.python.org/2/library/datetime.html
"""
from datetime import datetime, timedelta

# strptime(str, fmt)
# .strftime(fmt)
# timestamp
# fromtimestamp()
# data = datetime(2019, 4, 20, 10, 53, 20)
# print(data.strftime('%d/%m/%Y %H:%M:%S'))

data = datetime.strptime('20/07/2022 09:27:00', '%d/%m/%Y %H:%M:%S')
data = data + timedelta(days=5)
# print(data.strftime('%d/%m/%Y %H:%M:%S'))

d1 = datetime.strptime('20/07/2022 09:27:00', '%d/%m/%Y %H:%M:%S')
d2 = datetime.strptime('27/07/2022 09:10:00', '%d/%m/%Y %H:%M:%S')
dif = d1 - d2
print(dif)
