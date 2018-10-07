from queue import Queue
from random import randrange

class Printer():
	def __init__(self, pagerate):
		#参数1：当前处理任务剩余秒数；参数2：当前任务对象；参数3：每分钟打印张数
		self.seconds_ramianing = 0
		self.current_task = None
		self.pagerate = pagerate

	def start_task(self,task):
		self.current_task = task
		self.seconds_ramianing = task.get_page()* 60/self.pagerate

	def tick(self):
		#减小一个点数；消耗一秒
		if self.current_task != None:
			self.seconds_ramianing -= 1
			if self.seconds_ramianing == 0:
				self.current_task = None

	def busy(self):
		return self.current_task != None

class Task():
	def __init__(self, current_time):
		self.page = randrange(1,21)
		self.timestamp = current_time

	def wait_time(self,current_time):
		return current_time - self.timestamp

	def get_page(self):
		return self.page

def task_appear():
	#随机发生器，看能否在【1,180】内命中180，命中即判定该秒发生了一个task
	#该函数执行平均180次有一次成功
	num = randrange(1,181)
	return num == 180



def simulation(sum_seconds,pages_per_min):
	#参数1：总的模拟时间；参数2：打印机速率
	printer = Printer(pages_per_min)
	task_queue = Queue()
	wait_times = []
	for i in range(sum_seconds):
		#秒为最小模拟单位
		#模拟task是否产生
		if task_appear():
			newtask = Task(i)
			task_queue.enqueue(newtask)
		#模拟是否提交task队列中的task
		if not printer.busy() and not task_queue.isEmpty():
			current_task = task_queue.dequeue()
			wait_times.append(current_task.wait_time(i))
			printer.start_task(current_task)
		#printer计时也要减小
		printer.tick()

	#计算平均等待时间
	ave_wait_time = sum(wait_times)/len(wait_times)
	print('Average waiting time is {}, and {} tasks remaining!'.format(ave_wait_time,task_queue.size()))

if __name__ == '__main__':
	for i in range(10):
		simulation(3600, 5)
	print('*'*100)
	for i in range(10):
		simulation(3600, 10)
