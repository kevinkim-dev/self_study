#########################
#  SWEA number 11745
#  by 김승현                
#########################

# Q. 이진탐색트리 연산연습

class Node:
    
    def __init__(self, num):
        self.num = num
        self.left = None
        self.right = None

def insert(num):
    node = Node(num)
    if not root:
        root = node
    else:
        now_node = root
        while now_node:
            if now_node.num > num:
                now_node = now_node.left
            else:
                now_node = now_node.right
        now_node = node
    return


def delete(num):
    now_node = root
    while now_node.num != num or not now_node:
        if now_node.num > num:
            now_node = now_node.left
        else:
            now_node = now_node.right 
    if now_node.num == num:
        if now_node.right:
            min_node, parent = min_child(now_node.right, now_node)
            




def min_child(node, parent):
    if node.left:
        min_child(node.left, node)
    else:
        return node, parent


def max_child(node):
    if node.right:
        max_child(node.right)
    else:
        return node
    