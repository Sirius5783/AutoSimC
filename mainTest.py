# -*- coding: utf-8 -*-
"""
@author: Sirius5783
@license: None
@contact: markdan@foxmail.com
@file: mainTest.py
@time: 2018/7/30 0030 3:35
@desc:Windows 10,Python3.6
"""
"""

"""
# import sys
# import time
#
# def outputt(x):
#     while x<8:
#         x += 1
#         print(x)
#         time.sleep(1)
#     return 444
#
# if __name__ == '__main__':
#     x = sys.argv[1]
#     outputt(int(x))
#     print("SUB OUT")

import subprocess
sub = subprocess.Popen("python stdTest.py"+" 5",shell=True,stdin = subprocess.PIPE, stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
for i in iter(sub.stdout.readline,'b'):
    print(i.decode(encoding='utf-8'),end='')
    print("MAIN OUT")
    quit()





