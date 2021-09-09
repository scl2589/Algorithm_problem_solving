def solution(weights, head2head):
    answer = []
    lst = []
    for idx, games in enumerate(head2head):
        win = 0
        weight_win = 0
        lose = 0
        for idx2, game in enumerate(games):
            if game == "W":
                win += 1
                if weights[idx] < weights[idx2]:
                    weight_win += 1 
            elif game == "L":
                lose += 1
        if win + lose == 0:
            percentage = 0
        else: 
            percentage = win/ (win + lose)
        lst.append([idx + 1, weights[idx], percentage, weight_win])
    answer_lst = sorted(lst, key = lambda x: (x[2],x[3], x[1], -x[0]), reverse = True)
    return list(zip(*answer_lst))[0]