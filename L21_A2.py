import random
import time
def get_rondom_date(startdate,enddate):
    print(f"Printing random date between {startdate} and {enddate}")
    random_generator=random.random()
    date_format="%m/%d/%Y"
    starttime=time.mktime(time.strptime(startdate,date_format))
    endtime=time.mktime(time.strptime(enddate,date_format))   
    random_time=starttime+random_generator*(endtime-starttime)
    random_date=time.strftime(date_format,time.localtime(random_time))
    return random_date
print("Random date = ",get_rondom_date("1/1/2023","12/12/2024"))

