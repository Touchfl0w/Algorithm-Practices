from queue import Queue

#热土豆/击鼓传花问题;从0开始数
def hot_potato(players, num):
	q = Queue()
	for player in players:
		q.enqueue(player)

	while q.size() > 1:
		for i in range(num):
			q.enqueue(q.dequeue())
		q.dequeue()

	#循环结束后，只剩下一个player
	return q.dequeue()

if __name__ == '__main__':
	print(hot_potato(["Bill","David","Susan","Jane","Kent","Brad"],7))

