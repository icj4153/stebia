# 풀이 아이디어
# 1. 배열을 오름차순으로 정렬한다.
# 2. 배열에 아무것도 안남을 때까지 반복한다.
# 3. 만약 원소가 하나 남았다면 사람을 배에 바로 태우고 answer 1개 증가
# 4. 낮은 몸무게 부터 순회를 돌며 배열의 가장 큰 값부터 내려오면서 더해서 limit 이하 라면 
#   두 원소를 제거 후 answer을 1증가 시킨다.
# 5. 만약 모두 limit을 초과한다면 answer에 현재 사람의 수를 더해준다.


# limit 120
# 40 50 70 80

def solution(people, limit):
    # 1
    people.sort()
    answer = 0
    
    start = 0
    end = len(people) - 1
    
    while(start<=end):
        if(people[start]+people[end] <= limit):
            start += 1
            end -= 1
            answer += 1
        else:
            end -= 1
            answer += 1

    return answer

    # # 2
    # while people:
    #     # 3
    #     if len(people) == 1:
    #         people.pop()
    #         answer += 1
    #     # 4
    #     for i in range(len(people)-1,0,-1):
    #         if people[0] + people[i] <= limit:
    #             people.pop(i)
    #             people.pop(0)
    #             answer += 1
    #         # 5
    #         else:
    #             people.pop(-1)
    #             answer += 1