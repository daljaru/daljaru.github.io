
class Node:
    def __init__(self, key, value, left=None, right=None):
        self.key = key
        self.value = value
        self.left = left
        self.right = right

class BST:
    def __init__(self):
        self.root = None

    def get(self, key):
        return self.get_item(self.root, key)

    def get_item(self, node, key):
        if node == None:
            return None
        if node.key > key:
            return self.get_item(node.left, key)
        elif node.key < key:
            return self.get_item(node.right, key)
        else:
            return node.value

    def put(self, key, value):
        self.root = self.put_item(self.root, key, value)

    def put_item(self, node, key, value):
        if node == None:
            return Node(key, value)
        if node.key > key:
            node.left = self.put_item(node.left, key, value)
        elif node.key < key:
            node.right = self.put_item(node.right, key, value)
        else:
            node.value = value
        return node

    def min(self):
        if self.root == None:
            return None
        return self.minimum(self.root)

    def minimum(self, node):
        if node.left == None:
            return node
        return self.minimum(node.left)
    
    def delete_min(self):
        if self.root == None:
            print('tree is empty')
        self.root = self.del_min(self.root)

    def del_min(self, node):
        if node.left == None:gj
            return node.right
        node.left = self.del_min(node.left)
        return node

    def delete(self, key):
        self.root = self.del_node(self.root, key)

    def del_node(self, node, key):
        if node == None:
            return None
        if node.key > key:
            node.left = self.del_node(node.left, key)
        elif node.key < key:
            node.right = self.del_node(node.right, key)
        else:
            if node.right == None:
                return node.left
            if node.left == None:
                return node.right
            target = node
            node = self.minimum(target.right)
            node.right = self.del_min(target.right)
            node.left = target.left
        return node

    def preorder(self, n):
        if n != None:
            print(str(n.key), ' ', end='')
            if n.left:
                self.preorder(n.left)
            if n.right:
                self.preorder(n.right)

    def inorder(self, n):
        if n != None:
            if n.left:
                self.inorder(n.left)
            print(str(n.key), ' ', end='')
            if n.right:
                self.inorder(n.right)

    def postorder(self, n):
        if n!= None:
            if n.left:
                self.postorder(n.left)
            if n.right:
                self.postorder(n.right)
            print(str(n.key), ' ', end='')

    def levelorder(self, root):
        q = []
        q.append(root)
        while len(q) != 0:
            t = q.pop(0)
            print(str(t.key), ' ', end='')
            if t.left != None:
                q.append(t.left)
            if t.right != None:
                q.append(t.right)

    def height(self, root):
        if root == None:
            return 0
        return max(self.height(root.left), self.height(root.right)) + 1

if __name__=='__main__':
    t = BST()
    t.put(500, 'apple')
    t.put(600, 'banana')
    t.put(200, 'melon')
    t.put(100, 'orange')
    t.put(400, 'lime')
    t.put(250, 'kiwi')
    t.put(150, 'grape')
    t.put(800, 'peach')
    t.put(700, 'cherry')
    t.put(50, 'pear')
    t.put(350, 'lemon')
    t.put(10, 'plum')
    t.preorder(t.root)
    print('\n')
    t.inorder(t.root)
    print('\n')
    t.delete(200)
    t.preorder(t.root)
    print('\n')
    t.inorder(t.root)
    print('\n')
