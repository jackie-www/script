# -*- coding:utf-8 -*- #
# @time 2020/2/26 15:54
# author:wangpengda
import datetime
import re
import sys
import random


def get_day_date():
    cur = datetime.datetime.now()
    current_year = cur.year
    current_month = cur.month
    current_day = cur.day
    event_date = "{}{:0>2}{:0>2}".format(current_year, current_month, current_day)
    return event_date


def str_to_tuple(str1):
    # str2 = str1.replace("(", "").replace(")", "").replace(",", "").replace(" ", "")
    return tuple(map(int, tuple(str1)))


def get_bet_code_seven(data_type=None):

    if data_type is None:
        return f"{random.randint(0, 9)}|{random.randint(0, 9)}|{random.randint(0, 9)}|{random.randint(0, 9)}|{random.randint(0, 9)}|{random.randint(0, 9)}|{random.randint(0, 9)}"
    else:
        if not isinstance(data_type, tuple):
            print("投注项参数格式输入错误!")
            sys.exit()
        if len(data_type) != 7:
            print("投注项参数数量错误!")
            sys.exit()
        return f"{data_type[0]}|{data_type[1]}|{data_type[2]}|{data_type[3]}|{data_type[4]}|{data_type[5]}|{data_type[6]}"


def get_bet_code_five(data_type=None):

    if data_type is None:
        return f"{random.randint(0, 9)}|{random.randint(0, 9)}|{random.randint(0, 9)}|{random.randint(0, 9)}|{random.randint(0, 9)}"
    else:
        if not isinstance(data_type, tuple):
            print("投注项参数格式输入错误!")
            sys.exit()
        if len(data_type) != 5:
            print("投注项参数数量错误!")
            sys.exit()
        return f"{data_type[0]}|{data_type[1]}|{data_type[2]}|{data_type[3]}|{data_type[4]}"


def get_child_play_three(child_play):
    child_play_type = {
        '直选': 500,
        '组三': 503,
        '组六': 506
    }
    child_play_parmars = []
    if child_play is None:
        # todo三种玩法都下单
        for one in child_play_type:
            bet_code = get_child_play_three(one)
            child_play_parmars.append(bet_code)
        return child_play_parmars
    elif child_play == '直选':
        bet_type = child_play_type['直选']
        bet_code = betting_content()
        return (bet_type, bet_code)
    elif child_play == "组三":
        bet_type = child_play_type['组三']
        bet_code = betting_content_three()
        return (bet_type, bet_code)
    elif child_play == "组六":
        bet_type = child_play_type['组六']
        bet_code = betting_content_six()
        return (bet_type, bet_code)
    else:
        print("子玩法不存在!")
        bet_type = None
        bet_code = None
        sys.exit()
        # return (bet_type, bet_code)


def betting_content_three():
    # random.randint(0,9)
    return f"{random.randint(0,9)},{random.randint(0,9)}"


def betting_content_six():
    # random.randint(0,9)
    return f"{random.randint(0,9)},{random.randint(0,9)},{random.randint(0,9)}"


def betting_content():
    # alist = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    # for i in range(1, 10):
    #     ilist = alist[:i]
    #     istr = ",".join(ilist)
    #     for j in range(1, 10):
    #         jlist = alist[:j]
    #         jstr = ",".join(jlist)
    #         for k in range(1, 10):
    #             klist = alist[:k]
    #             kstr = ",".join(klist)
        bet_code = f"{random.randint(0,9)}|{random.randint(0,9)}|{random.randint(0,9)}"
        return bet_code


if __name__ == '__main__':
    pass
