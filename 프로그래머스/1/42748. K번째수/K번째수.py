# 풀이 아이디어
# 1. 커맨드를 모두 순회하며 반복
# 2. 커맨드에서 i, j, k를 추출한다.
# 3. array에서 i부터 j까지 자른 후 정렬하고 k번째 원소를 answer에 append한다.

def solution(array, commands):
    answer = []
    for command in commands:
        tmp_arr = []
        i,j,k = command[0],command[1],command[2]
        for l in range(i-1,j):
            tmp_arr.append(array[l])
        tmp_arr.sort()
        answer.append(tmp_arr[k-1])
    
    return answer