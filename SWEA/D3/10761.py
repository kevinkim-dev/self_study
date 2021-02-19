#########################
#  SWEA number 10761
#  by 김승현                
#########################

# Q. 신뢰

# 1. B 와 O의 위치를 찾음
# 2. 먼저 있는 버튼 위치까지 가는데 걸리는 시간 +1 만큼 다른 애는 이동 가능

for t in range(1, int(input())+1):
    action_list = input().split()
    b_done = 0
    o_done = 0
    b_find = 0
    o_find = 0
    b_pos = 1
    o_pos = 1
    b_idx = 0
    o_idx = 0
    b_go = 0
    o_go = 0
    done_idx = 0
    time = 0
    while done_idx < len(action_list)-1:
        # B와 O가 각자 할 일을 찾음
        for idx in range(done_idx+1, len(action_list)):
            if action_list[idx] == 'B' and b_find == 0:
                b_find = 1
                b_go = int(action_list[idx+1])
                b_idx = idx
            elif action_list[idx] == 'O' and o_find == 0:
                o_find = 1
                o_go = int(action_list[idx+1])
                o_idx = idx
            if o_find == 0:
                o_done = 1
                o_idx = len(action_list)+1
            if b_find == 0:
                b_done = 1
                b_idx = len(action_list)+1
            if b_find + o_find == 2:
                break
            # 누구 일이 먼저 인지 찾음
        # b먼저
        if b_idx < o_idx:
            # b 이동 + 버튼누르기
            time_spend = abs(b_go - b_pos) + 1
            b_pos = b_go
            time += time_spend
            done_idx = b_idx + 1
            b_find = 0
            # time_spend만큼 O가 갈수있으면 간다.
            if time_spend >= abs(o_go - o_pos):
                o_pos = o_go
            else:
                if o_go > o_pos:
                    o_pos += time_spend
                else:
                    o_pos -= time_spend
        else:
            print(b_idx, o_idx)
            time_spend = abs(o_go - o_pos) + 1
            o_pos = o_go
            time += time_spend
            done_idx = o_idx + 1
            o_find = 0
            # time_spend만큼 b가 갈수있으면 간다.
            if time_spend >= abs(b_go - b_pos):
                b_pos = b_go
            else:
                if b_go > b_pos:
                    b_pos += time_spend
                else:
                    b_pos -= time_spend
        print(b_pos, o_pos, done_idx, time)
    print("#%d %d" %(t, time))
        

