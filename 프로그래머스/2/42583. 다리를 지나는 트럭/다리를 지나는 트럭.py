# # 풀이 아이디어
# # 1. deque를 사용해(트럭의무게, 다리위에 올라간 시간(초)를 나타내자
# # 2. 트럭들이 다리를 건너는 동안 경과한 시간을 추척할 변수 time을 설정한다
# # 3. 매 초마다 다리 위에 있는 트럭들의 상태를 업데이트 하고, 트럭이 다리 끝에 도달하면 큐에서 제거한다
# # 4. 대기중인 트럭이 다리에 올라갈 수 있는지 확인한다. 다리에 새로운 트럭이 올라갈 수 있는지 확인하기 위해 다리 위의 트럭들의 총 무게와 현재 다리 위의 트럭 수를 고려한다.
# # 5. 모든 트럭이 다리를 건넜을 때 경과한 시간을 반환한다.

# from collections import deque

# def solution(bridge_length, weight, truck_weights):
#     time = 0
#     bridge = deque()
#     total_weight_on_bridge = 0
    
#     while truck_weights or bridge:
#         # 매번 초를 증가시킨다
#         time += 1
        
#         # 다리 위에 트럭이 있고, 다리의 끝에 도달했으면 트럭을 다리에서 내림
#         if bridge and bridge[0][1] == time:
        
#         # 다음 트럭이 다리에 올라갈 수 있는지 확인
#     return time

from collections import deque

def solution(bridge_length, weight, truck_weights):
    # 큐 초기화
    bridge = deque()
    time = 0
    total_weight_on_bridge = 0
    
    while truck_weights or bridge:
        time += 1
        
        # 다리 위에 트럭이 있고, 다리의 끝에 도달했으면 트럭을 다리에서 내림
        if bridge and bridge[0][1] == time:
            truck_weight, _ = bridge.popleft()
            total_weight_on_bridge -= truck_weight
        
        # 다음 트럭이 다리에 올라갈 수 있는지 확인
        if truck_weights:
            if total_weight_on_bridge + truck_weights[0] <= weight and len(bridge) < bridge_length:
                truck_weight = truck_weights.pop(0)
                total_weight_on_bridge += truck_weight
                bridge.append((truck_weight, time + bridge_length))
    
    return time

# 입출력 예시
print(solution(2, 10, [7, 4, 5, 6]))  # 8
print(solution(100, 100, [10]))  # 101
print(solution(100, 100, [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]))  # 110
