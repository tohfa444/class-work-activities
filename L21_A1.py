from datetime import date,time,datetime
today=date.today()
print("Today's date is ",today)
now=datetime.now()
print("Correct date and time is ",now)
print("date components",today.year,today.month,today.day)