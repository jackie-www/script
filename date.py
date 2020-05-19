# -*- coding:utf-8 -*- #
# @time 2019/11/28 20:47
# author:wangpengda
import datetime

cur = datetime.datetime.now()
current_year = cur.year
current_month = cur.month
current_day = cur.day
current_date = "{}{:0>2}{}".format(current_year, current_month, current_day)
print(current_date)
