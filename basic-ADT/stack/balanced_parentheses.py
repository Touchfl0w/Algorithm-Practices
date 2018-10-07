#经典使用stack的场景：平衡括号问题
from stack import Stack

def is_balance(mystr):
	s = Stack()
	#默认是对称的
	balance = True
	for item in mystr:
		if item == '(':
			s.push(item)
		elif item == ')':
			if s.isEmpty():
				#右括号多于左括号的情况
				balance = False
			s.pop()
	if not s.isEmpty():
		#左括号多于右括号的情况
		balance = False
	return balance

if __name__ == '__main__':
	print(is_balance('((()))'))
	print(is_balance('(()'))
