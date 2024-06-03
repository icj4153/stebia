# 풀이 아이디어
# 1. 괄호를 스택에 넣는다
# 2. 스택에는 '('만 넣어두고 ')'이 들어오면 삭제 시킨다
# 3. 만약 빈 스택에 ')'이 바로 들어오면 false 리턴
# 4. for문을 다 돌고도 '(' 괄호가 남아있다면 false

def solution(s):
    answer = True
    stack = []
    # 1
    for i in s:
        if i == '(':
            stack.append('()')
        else:
            if stack == []:
                return False
            else:
                stack.pop()
    
    # 4
    if stack:
        return False
    
    return True
            