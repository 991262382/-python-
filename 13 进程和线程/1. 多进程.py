import os
import random
import time
from multiprocessing import Pool


def long_time_task(name):
    print(f'运行任务{name}({os.getpid()})')
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print(f'任务{name}运行了{end - start}秒')


if __name__ == '__main__':
    print(f'父进程{os.getpid()}.')
    p = Pool(4)
    for i in range(5):
        p.apply_async(long_time_task, args=(i,))
    print('等待所有子进程结束...')
    p.close()
    p.join()
    print('所有子进程已经结束')


