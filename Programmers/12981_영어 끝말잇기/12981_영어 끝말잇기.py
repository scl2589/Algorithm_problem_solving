import math
def solution(n, words):
    word_list = set()
    for i, word in enumerate(words):
        # 탈락 (이미 말한 단어일때)
        if word in word_list or (i!=0 and words[i-1][-1] != word[0]):
            return [(i % n + 1), math.ceil((i+1) / n)]
        
        else:
            word_list.add(word)
    else:
        return [0, 0]
'''
T:15 
- 풀기는 쉬운데 인덱싱이 매 번 헷갈린다.
- 충분히 생각 후 modulo 사용하자
'''

'''
테스트 1 〉	통과 (0.01ms, 10.1MB)
테스트 2 〉	통과 (0.02ms, 10.2MB)
테스트 3 〉	통과 (0.01ms, 10.2MB)
테스트 4 〉	통과 (0.02ms, 10.3MB)
테스트 5 〉	통과 (0.03ms, 10.2MB)
테스트 6 〉	통과 (0.01ms, 10.2MB)
테스트 7 〉	통과 (0.02ms, 10.2MB)
테스트 8 〉	통과 (0.01ms, 10.2MB)
테스트 9 〉	통과 (0.02ms, 10.1MB)
테스트 10 〉	통과 (0.03ms, 10.2MB)
테스트 11 〉	통과 (0.03ms, 10.3MB)
테스트 12 〉	통과 (0.02ms, 10.2MB)
테스트 13 〉	통과 (0.01ms, 10.2MB)
테스트 14 〉	통과 (0.01ms, 10.2MB)
테스트 15 〉	통과 (0.01ms, 10.2MB)
테스트 16 〉	통과 (0.01ms, 10.1MB)
테스트 17 〉	통과 (0.01ms, 10.1MB)
테스트 18 〉	통과 (0.01ms, 10.1MB)
테스트 19 〉	통과 (0.01ms, 10.1MB)
테스트 20 〉	통과 (0.05ms, 10.2MB)
'''