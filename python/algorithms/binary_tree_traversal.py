
"""
用递归方式遍历二叉树

思路说明

遍历二叉树的方法有广度优先和深度优先两类，下面阐述的是深度优先。

有四种方式：

前序遍历(PreorderTraversal,NLR):先访问根结点，然后遍历其左右子树
中序遍历(InorderTraversal,LNR):先访问左子树，然后访问根节点，再访问右子树
后序遍历(PostorderTraversal,LRN):先访问左右子树，再访问根结点
层序遍历(levelorderTraversal):按照从上到下的层顺序访问
"""
Node = namedtuple('Node', 'data, left, right')
tree = Node(1,
            Node(2,
                 Node(4,
                      Node(7, None, None),
                      None),
                 Node(5, None, None)),
            Node(3,
                 Node(6,
                      Node(8, None, None),
                      Node(9, None, None)),
                 None))



def preorder(node):
	if node is not None:
		print node.data
		preorder(node.left)
		preorder(node.right)


def inorder(node):
	if node is not None:
		inorder(node.left)
		print node.data
		inorder(node.right)

def postorder(node):
	if node is not None:
		postorder(node.left)
		postorder(node.right)
		print node.data


def levelorder(node, more=None):
	if node is not None:
		if more is None:
			more = []	

		more += [node.left, node.right]
		print node.data

	if more:
		levelorder(more[0], more[1:])
	

