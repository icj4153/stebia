# 풀이 아이디어
# 1. 작업들은 큐를 통해 선입선출을 가능하게 한다
# 2. 작업이 다 없어질때까지 반복문을 수행한다
# 3. 반복문을 돌 때 각 작업들에 speed를 더해준다
# 4. 만약 큐의 첫번째 작업이 100 이상이 된다면, 작업들 내부를 for문으로 순회하며
#    100 이상인 것이 더 있는지 확인한다
# 5. 확인 후 작업과 해당 작업의 스피드를 제거하고 그 갯수를 answer 배열에 추가한다

def solution(progresses, speeds):
    answer = []
    # 2
    while progresses:
        cnt = 0
        
        #4
        while progresses and progresses[0] >= 100:
            progresses.pop(0)
            speeds.pop(0)
            cnt+=1

        for i in range(len(progresses)):
            progresses[i] = progresses[i] + speeds[i]
        
        if cnt:
            answer.append(cnt)
        
    return answer