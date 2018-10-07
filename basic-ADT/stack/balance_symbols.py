#经典使用stack的场景：平衡括号问题
from stack import Stack

def is_balance(mystr):
	s = Stack()
	#默认是对称的
	balance = True

	for item in mystr:
		if item in sym_dict.keys():
			s.push(item)
		elif item in sym_dict.values():
			if s.isEmpty():
				#右括号多于左括号的情况
				balance = False
			elif sym_dict[s.peek()] == item:
				s.pop()
				
	if not s.isEmpty():
		#左括号多于右括号的情况
		balance = False
	return balance

if __name__ == '__main__':
	sym_dict = {
		'(': ')',
		'{': '}',
		'[': ']',
	} 
	print(is_balance('{{([][])}()}'))
	print(is_balance('[{()]'))
