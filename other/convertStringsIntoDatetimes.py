from datetime import datetime
text = '2012-09-20'
y = datetime.strtime(text, '%Y-%m-%d')
z = datetime.now()
diff = z - y
diff
datetime.timedelta(3, 77824, 177393)
