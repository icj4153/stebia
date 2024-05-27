# 풀이 아이디어
# 1. 체육복 여벌이 있는 학생이 잃어버렸을 경우 lost와 reserve 배열에서 둘다 제거하자
# 2. lost 배열에서 원소를 꺼내서 앞번호를 먼저 reserve 배열에서 찾고 뒷번호를 찾는다.
#     찾는다면 lost 배열의 원소와 reserve 배열의 원소를 제거한다.
# 3. 최종 답은 n - len(lost) 


def solution(n, lost, reserve):
    
    lost.sort()
    reserve.sort()
    
    # 1. 
    for l in lost[:]:
        for r in reserve:
            if l == r:
                lost.remove(l)
                reserve.remove(r)
    # 2.
    for l in lost[:]:
        pre = l-1
        post = l+1
        
        if pre in reserve:
            reserve.remove(pre)
            lost.remove(l)
            continue
            
        if post in reserve:
            reserve.remove(post)
            lost.remove(l)
    
    # 3.
    answer = n - len(lost)
    
    return answer