# 1. answer이라는 스택에 arr에 pop을 하여 초기값을 넣는다
# 2. 스택에 있는 값과 arr의 값이 같으면 넣지 않는다.

def solution(arr):
    answer = []
    for num in arr:
        if not answer:
            answer.append(num)
        if num == answer[-1]:
            continue
        else:
             answer.append(num)
        
    return answer