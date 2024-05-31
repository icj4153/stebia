# 풀이 아이디어
# 1. 앞자리가 크면 숫자는 더 커지므로 첫번째 자리의 수부터 k보다 작을때까지 두번째 자리의 수보다 작으면 제거한다. 

def solution(number, k):
    answer = []
    for i in number:
        # 스택이 차있고, 스택의 맨 원소가 현재 넣을 값 보다 작은경우
        while k > 0 and answer and answer[-1] < i:
            answer.pop()
            k -= 1
        answer.append(i)
    
    if k > 0:
        answer = answer[:-k]
    answer = ''.join(answer)
    
    
    return answer
