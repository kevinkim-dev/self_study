###########################
#  BaekJoon 1991번
#  by 김승현                
###########################

# Q. 트리 순회

def preorder(node):
    if node != '.':
        preo.append(node)
        preorder(childs[ord(node)-65][0])
        preorder(childs[ord(node)-65][1])
    return


def inorder(node):
    if node != '.':
        inorder(childs[ord(node)-65][0])
        ino.append(node)
        inorder(childs[ord(node)-65][1])
    return


def postorder(node):
    if node != '.':
        postorder(childs[ord(node)-65][0])
        postorder(childs[ord(node)-65][1])
        posto.append(node)
    return


preo, ino, posto = [], [], [] 

N = int(input())
childs = [[] for _ in range(N)]
for _ in range(N):
    node, left_child, right_child = input().split()
    childs[ord(node)-65] = (left_child, right_child)

preorder('A')
inorder('A')
postorder('A')

print(''.join(preo))
print(''.join(ino))
print(''.join(posto))



