#YASHODEEP PAWAR USERID:2470
import datetime
s=input()
year,month,day=map(int,s.split(','))
a_date = datetime.date(year,month,day)
week_number = a_date.isocalendar()[1]
print(week_number)

'''
print(datetime.date(2015, 6, 16).isocalendar()[1])

#year,month,day=map(int,)

print(year,month,day)
'''
                   