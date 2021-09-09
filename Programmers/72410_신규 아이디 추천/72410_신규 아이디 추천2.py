import re
def solution(new_id):
    answer = ''
    # 1단계 
    new_id = new_id.lower()
    
    # 2단계
    temp = ''
    for i in new_id:
        if i.isalpha() == True or i.isnumeric() == True or i in ['-','_', '.']:
            temp += i
    
    # 3단계
    while True:
        new_id = temp.replace("..", ".")
        if new_id == temp:
            break
        temp = new_id 
    
    # 4단계 
    new_id = new_id.strip('.')
    
    # 5단계
    if not new_id:
        new_id = "a"
    
    #6 단계
    if len(new_id) >= 16:
        new_id = new_id[:15]
        new_id = new_id.strip('.')
    
    # 7단계
    if len(new_id) <= 2:
        while len(new_id) < 3:
            new_id += new_id[-1]
            
    return new_id
        