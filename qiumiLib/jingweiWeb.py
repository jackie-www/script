# -*- coding:utf-8 -*- #
# @time 2019/11/21 20:19
# author:wangpengda
from pprint import pprint
import requests

# web_base_url = 'http://118.190.76.10:3334'
# web_base_url = 'http://jw-api.ready.igoodgou.com'
# web_base_url = 'http://118.190.117.65:8080'
web_base_url = 'http://47.93.249.49:8080'
web_login_url = web_base_url + "/user/login.do"
web_outstanding_ticket_url = web_base_url + "/ticket/pending.do"
web_order_id_url = web_base_url + "/order/wait.do"
web_ticket_issue = web_base_url + "/order/handle.do"
web_deal_ticket = web_base_url + '/ticket/handle.do'
web_finish_list_url = web_base_url + "/ticket/finishTicketList.do"

class JingWeiWeb:

    def __init__(self):
        self.web_session = requests.Session()

    # 登录精卫后台
    def login_web(self, shop_id=43001):
        if shop_id == 6892:
            self.username = 'admin6892'
            self.passWord = '8ef791ecbbddaf61976da2bd8f0440f2'
            self.domain = 'zhejiangtestwasder.ready.igoodgou.com'
        elif shop_id == 41317:
            self.username = 'wpd'
            self.passWord = '33eb6d374d5d3711b213afc08377d04f'
            self.domain = 'zhejiangtestwasder.ready.igoodgou.com'
        elif shop_id == 43001:
            self.username = 'wpd_autotest'
            self.passWord = '33eb6d374d5d3711b213afc08377d04f'
            self.domain = 'shandongtestwasder.ready.igoodgou.com'

        payload = {"userName": f"{self.username}",
                   "passWord": f"{self.passWord}",
                   "domain": f"{self.domain}"}

        try:
            # print(web_outstanding_ticket_url)
            res = self.web_session.post(web_login_url, data=payload, timeout=10)
            assert res.status_code == 200, "登录列表接口状态码非200"
            res_dict = res.json()
            assert res_dict["status"] == 1, "登录接口status非1"
        except Exception as e:
            print("报错", e)

    # 获取未出票列表
    def get_outstanding_ticket_list(self):
        payload = {"pageNo": "1",
                   "pageSize": "60",
                   "dateSort": "",
                   "priceSort": '',
                   "userName": "",
                   "ticketId": '',
                   "domain": f"{self.domain}"}
        try:
            # print(web_outstanding_ticket_url)
            res = self.web_session.post(web_outstanding_ticket_url, data=payload, timeout=10)
            assert res.status_code == 200, "获取未出票列表接口状态码非200"
            res_dict = res.json()
            assert res_dict["status"] == 1, "获取未出票列表接口status非1"
            # print("web单号:", res_dict["data"]["pageList"][-1]["betId"])
            # return res_dict["data"]["pageList"][-1]["betId"]
            return res_dict["data"]["pageList"]
        except Exception as e:
            print("报错", e)
            # print(res.text)

    # 获取orderId
    def get_order_id(self, ticket_id):
        payload = {"pageNo": "1",
                   "pageSize": "30",
                   "ticketId": f"{ticket_id}"}
        try:
            res = self.web_session.post(web_order_id_url, data=payload, timeout=10)
            assert res.status_code == 200, "获取orderid接口状态码非200"
            res_dict = res.json()
            assert res_dict["status"] == 1, "获取orderid接口status非1"
            # print(res_dict["data"]["orders"]["pageList"][0]["applyid"])
            return res_dict["data"]["orders"]["pageList"][0]["applyid"]

        except Exception as e:
            print("报错", e)

    # 确认出票
    def ticket_issue(self, ticket_id, order_id):
        payload = {"orderIds": f"{order_id}",
                   "orderStatus": "3",
                   "ticketId": f"{ticket_id}",
                   "revocationReason": ""}
        try:
            res = self.web_session.post(web_ticket_issue, data=payload, timeout=10)
            assert res.status_code == 200, "确认出票接口状态码非200"
            res_dict = res.json()
            assert res_dict["status"] == 1, "确认出票接口status非1"
            # print(res_dict)

        except Exception as e:
            print("报错", e)

    # 订单处理
    def deal_ticket(self, ticket_id):
        payload = {
            'equipment': "6e8b36605e46",
            'equipmentCode': "96e79218965eb72c92a549dd5a330112",
            'equipmentType': '3',
            'ticketIds': f"{ticket_id}",
            'ticketStatus': "7",
            'revocationReason': "订单多，忙不过来"
        }
        try:
            res = self.web_session.post(web_deal_ticket, data=payload, timeout=10)
            assert res.status_code == 200, "撤单接口状态码非200"
            res_dict = res.json()
            assert res_dict["status"] == 1, "撤单接口status非1"
            assert res_dict["message"] == '订单操作成功', "撤单接口失败"
            # print(res_dict)

        except Exception as e:
            print("报错", e)

    # 获取已出票列表
    def get_finish_list(self, order_id):
        payload = {"pageNo": "1",
                   "pageSize": "30",
                   "licenseId": "",
                   "orderDate": "1",
                   "startDate": "",
                   "endDate": "",
                   "betId": f"{order_id}",
                   "userNick": ""}
        try:
            res = self.web_session.post(web_finish_list_url, data=payload)
            assert res.status_code == 200, "获取出票接口状态码非200"
            res_dict = res.json()
            assert res_dict["status"] == 1, "获取出票接口status非1"
            # print(res_dict)
        except Exception as e:
            print("报错", e)
            exit()

if __name__ == '__main__':
    ca = JingWeiWeb()
    # # print(ca.login('13261735737', "fb7396be1e095099fadb3afd4cf15d18"))
    # # print(ca.new_match())
    # ca.new_order('13261735737', "fb7396be1e095099fadb3afd4cf15d18")
    # time.sleep(2)
    # ca.login_web()
    ticket = ca.get_outstanding_ticket_list()
    print(f"web单号：{ticket}")
    order_id = ca.get_order_id(ticket)
    ca.ticket_issue(ticket, order_id)
    ca.get_finish_list(order_id)
    # ticket = ca.get_outstanding_ticket_list()
    pass

