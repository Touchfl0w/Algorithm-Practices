from stack import Stack
from functools import reduce

def dec_to_any(num, base=2):
	s = Stack()
	symbol_bank = '0123456789ABCDE'
	#取余数，压入stack
	while num > 0:
		item = num % base
		s.push(item)
		#除法取整必须使用 //
		num = num // base

	#pop并拼凑出字符串
	result = ''
	for i in range(s.size()):
		result += symbol_bank[s.pop()]
	return result

def any_to_dec(num, base=2):
	s = Stack()
	symbol_bank = '0123456789ABCDE'
	result = 0
	i = 0
	for item in str(num):
		s.push(item)
	for i in range(s.size()):
		item = s.pop()
		result += symbol_bank.index(item) * base ** i
	return result

def conversion(num, from_base, to_base):
	temp = any_to_dec(num, from_base)
	return dec_to_any(temp, to_base)

if __name__ == '__main__':
	print(dec_to_any(25,2))
	print(dec_to_any(25,16))
	print(any_to_dec(11001,2))
	print(any_to_dec(19,16))
	print(conversion(11001,2,8))


