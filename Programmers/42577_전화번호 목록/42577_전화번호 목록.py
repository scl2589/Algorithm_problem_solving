def solution(phonebook):
    phonebook.sort()
    for a in range(len(phonebook)-1):
        if phonebook[a+1].startswith(phonebook[a]):
            return False
    return True