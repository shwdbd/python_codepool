#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   adapter.py
@Time    :   2021/12/27 17:00:36
@Author  :   Jeffrey Wang
@Version :   1.0
@Contact :   shwangjj@163.com
@Desc    :   适配器模式

AliPay, WxPay: pay
BankPay: fk

'''
from abc import ABCMeta, abstractmethod


# 抽象接口
class Payment(metaclass=ABCMeta):

    @abstractmethod
    def pay(self, amount):
        pass


class AliPay(Payment):

    def pay(self, amount):
        print("支付宝支付:{0}".format(amount))


class WexinPay(Payment):

    def pay(self, amount):
        print("微信支付:{0}".format(amount))


class CmbcPay:

    def zf(self, amount):
        print("民生银行支付:{0}".format(amount))


class CMBCPayAdapter(Payment, CmbcPay):
    # 类适配器，针对民生银行

    def pay(self, amount):
        self.zf(amount=amount)


# 对象适配器
class PaymentAdapter(Payment):

    def __init__(self, payment):
        self.payment = payment

    def pay(self, amount):
        self.payment.zf(amount)


if __name__ == "__main__":
    pay = AliPay()
    pay.pay(100)
    # 使用类适配器
    pay = CMBCPayAdapter()
    pay.pay(100)
    # 使用对象适配器
    cmbc_pay = CmbcPay()
    pay = PaymentAdapter(cmbc_pay)
    pay.pay(100)
