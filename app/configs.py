'''
Description: 
Author: zhuohang li
Date: 2023-05-15 22:57:19
LastEditTime: 2023-05-15 23:06:06
LastEditors: zhuohang li
'''
# -*- coding:utf-8 -*-
import os
root_path = os.path.dirname(__file__)

configs = dict(
    debug=True,
    template_path=os.path.join(root_path,"templates"),
    static_path = os.path.join(root_path,"static")
)