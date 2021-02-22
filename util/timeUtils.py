# -*- coding: utf-8 -*-
import datetime
import time


# 生成带年月日时分秒的时间
# 2021年02月22日10时45分48秒
def get_time_date():
    dateline = datetime.datetime.now().strftime('%Y年%m月%d日%H时%M分%S秒')
    return dateline


# 生成带年月日时分秒的时间
# 2021-02-22 10:45:48.054009
def get_weekChinese_from_str(string):
    day = datetime.datetime.strptime(string, '%Y年%m月%d日%H时%M分%S秒').weekday()
    week_day_dict = {
        0: '周一',
        1: '周二',
        2: '周三',
        3: '周四',
        4: '周五',
        5: '周六',
        6: '周日',
    }
    return week_day_dict[day]


def get_weekChinese_from_date(date):
    day = date.weekday()
    week_day_dict = {
        0: '周一',
        1: '周二',
        2: '周三',
        3: '周四',
        4: '周五',
        5: '周六',
        6: '周日',
    }
    return week_day_dict[day]


# 生成13时间戳   eg:1557842280000
def get_time_stamp13(datetime_obj):
    datetime_str = datetime.datetime.strftime(datetime_obj, '%Y-%m-%d %H:%M:00')
    datetime_obj = datetime.datetime.strptime(datetime_str, '%Y-%m-%d %H:%M:00')
    # print(datetime_obj)
    # 10位，时间点相当于从1.1开始的当年时间编号
    date_stamp = str(int(time.mktime(datetime_obj.timetuple())))
    # 3位，微秒
    data_microsecond = str("%06d" % datetime_obj.microsecond)[0:3]
    date_stamp = date_stamp + data_microsecond
    return int(date_stamp)


if __name__ == "__main__":
    aaa = get_time_date()
    print(aaa)

    time1 = datetime.datetime.now()
    print(time1)
    print(type(time1))

    timeStamp = int(time.time())
    print(type(timeStamp))
    print(timeStamp)

    result = get_time_stamp13(time1)
    print(result)

    date = datetime.datetime.now() + datetime.timedelta(days=10)
    print(date)

    date = datetime.datetime.now() + datetime.timedelta(minutes=10)
    secKillTime = get_time_stamp13(date)
    print(secKillTime)

    print("觉得很费劲啊看回放")
    sss = get_weekChinese_from_str(aaa)
    print(sss)
    print("======")
    sss22 = get_weekChinese_from_date(time1)
    print(sss22)
