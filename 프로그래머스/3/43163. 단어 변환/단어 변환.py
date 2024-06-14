from collections import deque

# BFS를 사용하여 단어 변환의 최소 단계를 계산하는 함수
def bfs(begin, target, words):
    # 두 단어가 한 글자만 다른지 확인하는 함수
    def can_transform(word1, word2):
        return sum(a != b for a, b in zip(word1,word2)) == 1
    
    # BFS 탐색을 위한 큐 초기화, 시작 단어와 변환 횟수를 저장
    queue = deque([(begin, 0)])  # (현재 단어, 변환 단계 수)
    # 이미 방문한 단어를 추적하기 위한 
    # set을 사용하면 중복을 방지하고 탐색의 속도가 크게 개선됨 속도가 O(1)
    visited = set([begin])
    
    # 큐가 빌 때까지 반복
    while queue:
        # 현재 단어와 변환 단계를 큐에서 꺼내기
        current_word, steps = queue.popleft()
        
        # 현재 단어가 목표 단어와 같으면 변환 단계를 반환
        if current_word == target:
            return steps
        
        # 단어 리스트를 순회하며 현재 단어와 한 글자만 다른 단어를 찾음
        for word in words:
            # 방문하지 않았고 변환 가능한 단어인 경우
            if word not in visited and can_transform(current_word, word):
                # 방문한 단어로 표시
                visited.add(word)
                # 큐에 추가하며 변환 단계 증가
                queue.append((word, steps + 1))
    
    # 목표 단어에 도달할 수 없는 경우 0을 반환
    return 0

# 주어진 시작 단어, 목표 단어, 단어 리스트로 최소 변환 단계를 계산하는 함수
def solution(begin, target, words):
    # 목표 단어가 단어 리스트에 없으면 변환할 수 없음
    if target not in words:
        return 0
    
    # BFS 함수를 호출하여 최소 변환 단계를 반환
    return bfs(begin, target, words)
