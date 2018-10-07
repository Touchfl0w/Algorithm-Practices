#stack综合运用
#启发：stack不仅在入栈、出栈过程中可以做文章，比如筛选等操作，
#同时，不一定要全部元素入栈后再出栈，可以入一部分、出一部分、再入
from stack import Stack

def postpix(exp):
	opstack = Stack()
	out_list = []
	exp = exp.split(' ')
	for item in exp:
		if item in operator_bank:
			if opstack.isEmpty():
				opstack.push(item)
			elif operator_bank[opstack.peek()] <= operator_bank[item]:
				opstack.push(item)
			else:
				#当opstack非空，且peek优先值大于当前item,则将opstack'('之后所有操作符pop并添加到out_list,不包括左括号
				while not opstack.isEmpty():
					top = opstack.pop()
					if top == '(':
						opstack.push('(')
						break
					out_list.append(top)
				#别忘了先把当前item push进去
				opstack.push(item)
		#当遇到')'，将opstack中元素pop并添加到out_list,知道遇到‘（’,左括号也要pop
		elif item == ')':
			while not opstack.isEmpty():
				top = opstack.pop()
				if top == '(':
					break
				out_list.append(top)
		#当字符为操作数
		else:
			out_list.append(item)
	
	while(not opstack.isEmpty()):
		top = opstack.pop()
		out_list.append(top)
	return ''.join(out_list)


if __name__ == '__main__':
	operator_bank = {
		'(': 2,
		'*': 1,
		'/': 1,
		'+': 0,
		'-': 0,
	}
	operand_bank = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
	# print(postpix("A*B+C*D"))
	print(postpix("( A + B ) * C - ( D - E ) * ( F + G )"))