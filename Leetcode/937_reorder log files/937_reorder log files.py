class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        # 문자로 구성된 로그가 숫자 로그보다 앞에 온다.
        # 식별자 (로그 가장 앞부분)는 문자가 동일할 경우 식별자 순으로 한다.
        # 숫자 로그는 입력 순서대로 한다.
        letters, digits = [], []
        for log in logs:
            if log.split()[1].isdigit():
                digits.append(log)
            else:
                letters.append(log) 
        
        letters.sort(key = lambda x : (x.split()[1:], x.split()[0]))
        return letters + digits 
    