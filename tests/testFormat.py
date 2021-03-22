# coding: utf-8
"""
# @Time    : 2020/4/26 13:41
# @Author  : Gina Gao
# @File    :
# @Software: PyCharm
# @Descript:
"""
dict_test = {'Name': 'Jas', 'num': {'first_num': '66', 'second_num': '70'}, 'age': '15'}
print(dict_test.get('num'))

print(dict_test.get('first_num', "hghg"))  # None

a = ('{:^20}'.format('@' * 10))
b = ('{:>20}'.format('@' * 10))
c = ('{:<20}'.format('@' * 10))
d = ('{}'.format('#' * 50))
print(a)
print(b)
print(c)
print(d, len(d))
print(dict_test.get('num').get('first_num'))  # 66


# tenant_info ="tenant_info"

def tenant_info():
    return "tenant_info"

AAA = "privacy_request_pulling"
BBB = AAA.format(**tenant_info)
print(BBB)

