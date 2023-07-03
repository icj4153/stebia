# 조건에 맞게 수열 변환하기 2

def solution(arr):
    arr1 = arr
    arr2 = []
    answer = 0
    while True:
        for elem in arr1:
            if elem > 50 and elem % 2 == 0:
                arr2.append(elem//2)
            elif elem < 50 and elem % 2 == 1:
                arr2.append(elem*2+1)
        if arr1 == arr2:
            break
        else:
            arr1 = list(arr2)
            arr2 = []
            answer += 1
    return answer-1