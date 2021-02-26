# -*- coding: utf-8 -*-
import logging
import os
from logging import handlers

logPrivate = ['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL']

# 第一步，创建一个logger
Logger = logging.getLogger()
# Log等级总开关,控制控制台的日志级别
Logger.setLevel(logging.INFO)
# 第二步，创建一个handler，用于写入日志文件
root_dir = os.path.dirname(os.path.abspath('../environment'))
# print(root_dir)
# logfile = root_dir + '/myPython/commonLog/log.txt'
# print(logfile)
logfile = "/Users/logger/log.txt"
# print(logfile)
fh = logging.FileHandler(logfile, mode='a')  # open的打开模式这里可以进行参考
fh.setLevel(logging.INFO)  # 输出到file的log等级的开关
# 第三步，再创建一个handler，用于输出到控制台
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)  # 输出到console的log等级的开关
# 第四步，定义handler的输出格式
formatter = logging.Formatter("%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s")
fh.setFormatter(formatter)
ch.setFormatter(formatter)
# 第五步，将logger添加到handler里面
Logger.addHandler(fh)
Logger.addHandler(ch)

# # 日志
# Logger.debug('这是 logger debug message')
# Logger.info('这是 logger info message')
# Logger.warning('这是 logger warning message')
# Logger.error('这是 logger error message')
# Logger.critical('这是 logger critical message')