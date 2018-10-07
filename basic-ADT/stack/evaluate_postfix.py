from stack import Stack

def _do_math(stack, operator):
	#先pop出的数字为第二个操作数！！！一定要注意顺序
	operand2 = int(stack.pop())
	operand1 = int(stack.pop())
	if operator == '+':
		return operand1 + operand2
	if operator == '-':
		return operand1 - operand2
	if operator == '*':
		return operand1 * operand2
	if operator == '/':
		return operand1 / operand2

def evaluate_postfix(exp):
	"""求后缀算数表达式的值"""
	operand_stack = Stack()
	exp_list = exp.split(' ')
	for item in exp_list:
		if item in operand_bank:
			operand_stack.push(item)
		else:
			temp = _do_math(operand_stack,item)
			operand_stack.push(temp)
	return operand_stack.pop()


if __name__ == '__main__':
	operand_bank = '123456789'
	print(evaluate_postfix('7 8 + 3 2 + /'))