#########################
#  Programmers problem kit 
#  스택 & 큐 # 01
#  by 김승현                
#########################

# Q. 다리를 지나는 트럭

# def solution(bridge_length, weight, truck_weights):
#     answer = 0
#     bridge = [0]*bridge_length
#     truck_weights.sort(reverse=True)
#     for i in range(len(truck_weights)):
#         if truck_weights[i] < weight:
#             break
#     answer += i*bridge_length
#     truck_weights = truck_weights[i:]
#     while truck_weights:
#         bridge.pop(0)
#         flag = 0
#         for truck in truck_weights:
#             if weight - sum(bridge) >= truck:
#                 bridge.append(truck)
#                 truck_weights.remove(truck)
#                 flag = 1
#                 break
#         if not flag:
#             bridge.append(0)
#         answer += 1
#     answer += len(bridge)
#     return answer

def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = [0]*bridge_length
    while truck_weights:
        bridge.pop(0)
        flag = 0
        truck = truck_weights[0]
        if weight - sum(bridge) >= truck:
            bridge.append(truck)
            truck_weights.remove(truck)
            flag = 1
        if not flag:
            bridge.append(0)
        answer += 1
    answer += len(bridge)
    return answer

bridge_length = 2
weight = 10
truck_weights = [7, 4, 5, 6]
print(solution(bridge_length, weight, truck_weights))