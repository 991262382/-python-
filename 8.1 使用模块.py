'一个测试模块'  # 任何模块代码的第一个字符串都被视为模块的文档注释；
__author__ = 'YYZHU'

import sys


def test():
    args = sys.argv
    print(f'args:{args}')
    print(f'args的长度:{len(args)}')
    if len(args) == 1:
        print('你好')
    elif len(args) == 2:
        print(f'你好,{args[1]}')
    else:
        print('参数太多')


if __name__ == '__main__':
    test()
'''
(base) yyzhu@Mac:Code/廖雪峰python学习 ‹master*›$ python 8.1\ 使用模块.py
args:['8.1 使用模块.py']
args的长度:1
你好

(base) yyzhu@Mac:Code/廖雪峰python学习 ‹master*›$ python 8.1\ 使用模块.py yyzhu
args:['8.1 使用模块.py', 'yyzhu']
args的长度:2
你好,yyzhu

(base) yyzhu@Mac:Code/廖雪峰python学习 ‹master*›$ python 8.1\ 使用模块.py yyzhu fang
args:['8.1 使用模块.py', 'yyzhu', 'fang']
args的长度:3
参数太多
(base) yyzhu@Mac:Code/廖雪峰python学习 ‹master*›$ 
'''
