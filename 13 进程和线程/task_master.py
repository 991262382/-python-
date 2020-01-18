import queue
import random
from multiprocessing.managers import BaseManager

# 发送任务的队列:
task_queue = queue.Queue()
# 接收结果的队列:
result_queue = queue.Queue()


# 从BaseManager继承的QueueManager:
class QueueManager(BaseManager):
    pass


# 把两个Queue都注册到网络上, callable参数关联了Queue对象:
QueueManager.register('get_task_queue', callable=lambda: task_queue)
QueueManager.register('get_result_queue', callable=lambda: result_queue)
# 绑定端口5000, 设置验证码'abc':
manager = QueueManager(address=('', 5000), authkey=b'abc')
# 启动Queue:
manager.start()
# 获得通过网络访问的Queue对象:
task = manager.get_task_queue()
result = manager.get_result_queue()

print('Try to put tasks...')
# 放几个任务进去:
for i in range(10):
    n = random.randint(0, 10000)
    print(f'Put Task [{n}]')
    task.put(n)

# 从result队列读取结果:
print('Try to get results...')
try:
    while True:
        r = result.get(timeout=20)
        print(f'Get Result: [{r}]')
except queue.Empty:
    print('Result queue is empty.')

# 关闭:
manager.shutdown()
print('master exit.')
