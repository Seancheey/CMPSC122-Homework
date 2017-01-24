class OrderedPairs:
	"""Create a collection of ordered pairs, given lists of coordinates"""

	def __init__(self, xs, ys):
		self._xs = xs
		self._ys = ys
		self._xdim = len(xs)  # record list lengths
		self._ydim = len(ys)
		self._visited = 0
		self._i = 0

	def __getitem__(self, i):
		return self._xs[i // self._ydim], self._ys[i % self._ydim]

	def __next__(self):
		if self._i >= self._xdim * self._ydim:
			raise StopIteration()
		ans = self._xs[self._i // self._ydim], self._ys[self._i % self._ydim]
		self._i += 1
		return ans

	def __iter__(self):
		for x in self._xs:
			for y in self._ys:
				yield x, y


def pairsInRange(xs, ys, low, high):
	for x in xs:
		for y in ys:
			if low < x * y < high:
				yield x, y


def sieve(iterator, stop):
	"""Apply Erastothenes' Sieve to given list of integers
	stop when the given value is reached"""
	divisor = next(iterator)  # obtain the first given value
	if divisor < stop:  # display it, and
		yield divisor  # then remove its multiples
		yield from sieve((x for x in iterator if x % divisor != 0), stop)


def allnums():
	i = 1
	while (True):
		i += 1
		yield i


print(list(sieve(allnums(), 500)))  # run sieve for values up to 500
