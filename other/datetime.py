import datetime

a = datetime(2012, 9, 23)
a + timedelta(months=1)
b = datetime(2012, 12, 21)
d = b - a
d
datetime.timedelta(89)
d = relativedelta(b, a)
relativedelta(months=+2, days=+28)