from dequeue import Dequeue

def pal_checker(mystr):
	"""检查字符串是否为回文字符串，即正序等于逆序字符串"""
	dq = Dequeue()
	mylist = [i  for i in mystr]
	indicator = True
	for item in mylist:
		dq.addRear(item)
	for i in range(dq.size()//2):
		fornt = dq.removeFront()
		rear = dq.removeRear()
		if fornt != rear:
			indicator = False
			break
	return indicator

if __name__ == '__main__':
	print(pal_checker("lsdkjfskf"))
	print(pal_checker("radar"))
