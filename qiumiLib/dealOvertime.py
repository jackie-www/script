# -*- coding:utf-8 -*- #
# @time 2020/3/16 13:49
# author:wangpengda
from qiumiLib.jingweiWeb import JingWeiWeb
from addData.Utils import get_current_time


def main():
    # 获取当前时间，以秒显示
    date_time, second_time = get_current_time()
    jw = JingWeiWeb()
    jw.login_web(43001)
    page_list = jw.get_outstanding_ticket_list()
    sum = 0
    # 撤单所有订单
    # while page_list:
    for page_info in page_list:
        race_date = page_info['endDate']
        # race_time = page_info['endSecond']
        # 撤掉预期订单
        if int(date_time) > int(race_date):
            ticket_id = page_info['betId']
            jw.deal_ticket(ticket_id)
            sum += 1
            print(f"撤单数量:{sum}")
        # page_list = jw.get_outstanding_ticket_list()  # 获取订单
    print(f"撤单{sum}单完成!")


if __name__ == '__main__':

    main()
