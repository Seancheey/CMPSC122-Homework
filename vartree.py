class VarTree:
	class Node:
		__slots__ = ("_right", "_left", "_value", "key")

		def __init__(self, left, key, val, right):
			self._left = left
			self.key = key
			self._value = val
			self._right = right

		@property
		def value(self):
			return self._value

		@property
		def right(self):
			return self._right

		@property
		def left(self):
			return self._left

	__slots__ = "_root"

	def __init__(self):
		self._root = None

	def _search(self, here, key):
		if here is None or here.key == key:
			return here
		elif key < here.key:
			return self._search(here.left, key)
		else:
			return self._search(here.right, key)

	def _insert(self, here: Node, key, value):
		if here is None:
			return self.Node(None, key, value, None)
		elif here.key is None:
			return here
		elif key < here.key:
			return self.Node(self._insert(here.left, key, value), here.key, here.value, here.right)
		else:
			return self.Node(here.left, here.key, here.value, self._insert(here.right, key, value))

	def assign(self, key, value):
		self._root = self._insert(self._root, key, value)

	def lookup(self, var):
		return self._search(self._root, var).value

	def is_empty(self):
		return self._root is None

	def __len__(self):
		pass

	def __iter__(self):
		pass

	def _str(self, here):
		if here is None:
			return "null"
		return "(%s: %s --> %s, %s)" % (
			str(here.key), str(here.value), str(self._str(here.left)), str(self._str(here.right)))

	def __str__(self):
		return self._str(self._root)


if __name__ == "__main__":
	v = VarTree()
	v.assign("a", 15)
	v.assign("b", 20)
	print(v)
