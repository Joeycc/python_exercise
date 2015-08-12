class TestIterator(object):
	"""docstring for TestIterator"""
	def __init__(self):
		super(TestIterator, self).__init__()
		self.value = 0
	def next(self):
		self.value += 1
		if self.value > 10:
			raise StopIteration
		return self.value
	def __iter__(self):
		return self

def flatten(nested):
	try:
		try:
			nested + ''
		except TypeError:
			pass
		else:
			raise TypeError

		for sublist in nested:
			for element in flatten(sublist):
				yield element
	except TypeError:
		yield nested

print('hello world')
if __name__ == '__main__':
	#ti = TestIterator()
	#li = list(ti)
	#print(li)

	#print(ti)
	ar = [[1,2,3], [2, 3, [2,4], 'ewt', 4, 5, ['gewqt', 2, 3]]]
	for i in flatten(ar):
		print(i)

		