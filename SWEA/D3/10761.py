#########################
#  SWEA number 10761
#  by 김승현                
#########################

# Q. 신뢰


# index: 0번 작업순서 1번 목표위치 2번 현재위치 3번 turn
# 기계 움직임(True이면 버튼 누른것, False이면 아직 일 안끝난것)
def action(act):
    # 순서가 N과 같으면 이미 동작 끝난 것
    if act[0] == N:
        return False
    # 현재 위치가 목표위치와 다르면 해당 방향으로 이동
    if act[1] < act[2]:
        act[2] -= 1
    elif act[1] > act[2]:
        act[2] += 1
    # 현재 위치에 도달했고, 자기 순서면 True반환해서 버튼 눌렀음을 알림
    elif act[1] == act[2] and act[3]:
        return True
    return False



for t in range(1, int(input())+1):
    action_list = list(input().split())
    o_q, b_q = [], []
    N = int(action_list[0])
    for i in range(N):
        if action_list[2*i+1] == 'O':
            o_q.append([i, int(action_list[2*i+2])])
        else:
            b_q.append([i, int(action_list[2*i+2])])
    # 끝남을 알려줄 N+1번째 task 추가
    o_q += [[N, 0]]
    b_q += [[N, 0]]
    # task와 함께 [1]->시작위치, [0]->자기가 누를 순서인지 0, 1로 알려줌
    o_act, b_act = o_q.pop(0) + [1] + [0], b_q.pop(0) + [1] + [0]
    # 시작 순서 정하기
    if o_act[0] < b_act[0]:
        o_act[3] = 1
    else:
        b_act[3] = 1
    time = 0
    # 둘다 마지막에 [N, 0]을 뽑아오면 끝난 것
    while o_act[0] != N or b_act[0] != N:
        # 각자 action을 하고 True를 반환했으면 다음 task를 받기 위해 pop
        if action(o_act):
            o_act = o_q.pop(0) + [o_act[2]] + [0]
        if action(b_act):
            b_act = b_q.pop(0) + [b_act[2]] + [0]
        if o_act[0] < b_act[0]:
            o_act[3] = 1
        else:
            b_act[3] = 1
        time += 1
    print("#%d %d" %(t, time))





























# 1. B 와 O의 위치를 찾음
# 2. 먼저 있는 버튼 위치까지 가는데 걸리는 시간 +1 만큼 다른 애는 이동 가능

# for t in range(1, int(input())+1):
#     action_list = input().split()
#     b_done = 0
#     o_done = 0
#     b_find = 0
#     o_find = 0
#     b_pos = 1
#     o_pos = 1
#     b_idx = 0
#     o_idx = 0
#     b_go = 0
#     o_go = 0
#     done_idx = 0
#     time = 0
#     while done_idx < len(action_list)-1:
#         # B와 O가 각자 할 일을 찾음
#         for idx in range(done_idx+1, len(action_list)):
#             if action_list[idx] == 'B' and b_find == 0:
#                 b_find = 1
#                 b_go = int(action_list[idx+1])
#                 b_idx = idx
#             elif action_list[idx] == 'O' and o_find == 0:
#                 o_find = 1
#                 o_go = int(action_list[idx+1])
#                 o_idx = idx
#             if o_find == 0:
#                 o_done = 1
#                 o_idx = len(action_list)+1
#             if b_find == 0:
#                 b_done = 1
#                 b_idx = len(action_list)+1
#             if b_find + o_find == 2:
#                 break
#             # 누구 일이 먼저 인지 찾음
#         # b먼저
#         if b_idx < o_idx:
#             # b 이동 + 버튼누르기
#             time_spend = abs(b_go - b_pos) + 1
#             b_pos = b_go
#             time += time_spend
#             done_idx = b_idx + 1
#             b_find = 0
#             # time_spend만큼 O가 갈수있으면 간다.
#             if time_spend >= abs(o_go - o_pos):
#                 o_pos = o_go
#             else:
#                 if o_go > o_pos:
#                     o_pos += time_spend
#                 else:
#                     o_pos -= time_spend
#         else:
#             print(b_idx, o_idx)
#             time_spend = abs(o_go - o_pos) + 1
#             o_pos = o_go
#             time += time_spend
#             done_idx = o_idx + 1
#             o_find = 0
#             # time_spend만큼 b가 갈수있으면 간다.
#             if time_spend >= abs(b_go - b_pos):
#                 b_pos = b_go
#             else:
#                 if b_go > b_pos:
#                     b_pos += time_spend
#                 else:
#                     b_pos -= time_spend
#         print(b_pos, o_pos, done_idx, time)
#     print("#%d %d" %(t, time))
        

