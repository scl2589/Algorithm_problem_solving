def solution(numbers):
    arr = []
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            if i != j:
                arr.append(numbers[i] + numbers[j])
    return sorted(list(set(arr)))