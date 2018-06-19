'''
日历

'''
import calendar


#返回指定某年某月的日历
print(calendar.month(2018,6))

#返回指定年的日历
print(calendar.calendar(2018))


#闰年返回True,佛则返回false
print(calendar.isleap(2000))


#返回某个月的weekday的第一天和这个月的天数
print(calendar.monthrange(2018,6))

#返回某个月以每一周为元素的列表
print(calendar.monthcalendar(2018,6))