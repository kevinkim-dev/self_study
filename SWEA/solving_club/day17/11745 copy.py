#########################
#  SWEA number 11745
#  by 김승현                
#########################

# Q. 이진탐색트리 연산연습

def insert(tree, node):
    if tree[1] > node:
        if tree[0]:
            insert(tree[0], node)
        else:
            tree[0] = [0, node, 0]
    else:
        if tree[2]:
            insert(tree[2], node)
        else:
            tree[2] = [0, node, 0]
    return


def delete(tree, node):
    print(tree)
    if tree[1] > node:
        delete(tree[0], node) if tree[0] else print('%d node가 없습니다.' %node)
    elif tree[1] < node:
        delete(tree[2], node) if tree[2] else print('%d node가 없습니다.' %node)
    else:
        if not tree[0] and not tree[2]:
            print('둘다 없음')
            tree = 0
            print(tree)
        elif not tree[2]:
            min_tree = find_min(tree)
            tree[1], min_tree = min_tree[1], 0
        else:
            max_tree = find_max(tree)
            tree[1], max_tree = max_tree[1], 0
    return


def find_min(tree):
    if tree[0]:
        find_min(tree[0])
    else:
        return tree


def find_max(tree):
    if tree[2]:
        find_max(tree[2])
    else:
        return tree



C, I, D = map(int, input().split())
node_list = list(map(int, input().split()))
# 좌, 나, 우
nodes = [0, node_list.pop(0), 0]
while node_list:
    insert(nodes, node_list.pop(0))
insert_node_list = list(map(int, input().split()))
while insert_node_list:
    insert(nodes, insert_node_list.pop(0))
delete_node_list = list(map(int, input().split()))
while delete_node_list:
    print(nodes)
    delete(nodes, delete_node_list.pop(0))