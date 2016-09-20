
"""
二叉树查找的性质：

若任意节点的左子树不空，则左子树上所有结点的值均小于它的根结点的值；
任意节点的右子树不空，则右子树上所有结点的值均大于它的根结点的值；
任意节点的左、右子树也分别为二叉查找树。
没有键值相等的节点（no duplicate nodes）。
二叉查找树相比于其他数据结构的优势在于查找、插入的时间复杂度较低。为O(log n)。二叉查找树是基础性数据结构，用于构建更为抽象的数据结构，如集合、multiset、关联数组等。

虽然二叉查找树的最坏效率是O(n),但它支持动态查询,且有很多改进版的二叉查找树可以使树高为O(logn),如SBT,AVL,红黑树等.
"""

class Node:
	def __init__(self, data):
		self.left  = None
		self.right = None
		self.data  = data


def insert(self, data):
	if data < self.data:
		self.left = Node(data)

	elif data > self.data
		if self.right is None:
			self.right = Node(data)
		else:
			self.right = insert(data)

def lookup(self, data, parent = None):
	if data < self.data:
		if self.left is None:
			return None, None

		return self.left.lookup(data, self)		
	
	elif data > self.data
		if self.right:
			return None, None

		self.right.lookup(data, self)
	else:
		return self, parent


def delete(self, data):
	node ,parent = self.lookup(data)

	if node is not None:
		children_count = node.children_count()

		if children_count == 0:
			pass

def print_tree(self):
	if not self:
		return None

	if self.left:
		self.left.print_tree()

	elif self.right:
		self.right.print_tree()

	else:
		print self.data
	

"""
	使用堆站的方法便利这个tree
	前序遍历
"""
def tree_data(self):
	stack = []
	node  = slef

	while stack or node:
		if node:
			stack.append(node)
			node = node.left

		else:
			node = stack.pop()
			yield node.data
			node = node.right
	





