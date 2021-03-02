def solution(arr):
    if len(arr) >= 2:
        min_idx = arr.remove(min(arr))
        return arr
    else:
        return [-1]