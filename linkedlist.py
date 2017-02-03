class LinkedList:
	"""A singly linked list"""
	__slots__ = ("_tail", "_head")

	class Node:
		__slots__ = "_value", "_next"

		def __init__(self, v, n):
			self._value = v
			self._next = n

	def __init__(self):
		self._tail = self._head = None

	def __init__(self, list):
		self._tail = self._head = None
		for value in list:
			self.push(value)

	def push(self, value):
		if not self._tail or not self._head:
			self._tail = self._head = self.Node(value, None)
			return
		self._tail._next = self.Node(value, None)
		self._tail = self._tail._next

	def pop(self):
		i = self._head
		if i == self._tail:
			a = self._head._value
			self._tail = None
			self._head = None
			return a
		while i._next != self._tail:
			i = i._next
		i._next = None
		self._tail = i
		return self._tail

	def __iter__(self):
		current = self._head
		while current is not None:
			yield str(current._value)
			current = current._next

	def __str__(self):
		return ' '.join(list(iter(self)))

	def __len__(self):
		i = 0
		current = self._head
		while current:
			i += 1
			current = current._next
		return i

	def remove(self, value):
		"""Remove one occurrence of the given value from the list"""
		current = self._head
		while current._next._value != value:
			current = current._next
		if current._next._next != None:
			current._next = current._next._next


if __name__ == "__main__":
	a = LinkedList([1, 2, 3])
	print(a)
	a.pop()
	print(a)
	a.push(5)
	print(a)
	print(a.__len__())
