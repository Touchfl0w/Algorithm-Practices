def decorator(f):
	def wrapper(*args, **kwargs):
		from time import time
		time1 = time()
		result = f(*args, **kwargs)
		time2 = time()
		print("the function {func_name} spend: ".format(func_name=f.__name__),time2-time1)
		return result
	return wrapper
