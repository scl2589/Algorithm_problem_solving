T = int(input())
for tc in range(1, T+1):
    #H: 높이, W: 너비
    H, W = map(int, input().split())
    field = [list(input()) for _ in range(H)]
    num_of_cmd = int(input())
    cmd = list(input())

    current_i, current_j = 0, 0
    for i in range(H):
        for j in range(W):
            if field[i][j] in ['^','v', '<', '>']:
                current_i = i
                current_j = j
                tank = field[i][j]
                break
        if current_i:
            break

    for i in cmd:
        if i == 'U':
            if current_i - 1 >= 0 and field[current_i - 1][current_j] == '.':
                field[current_i - 1][current_j] = '^'
                field[current_i][current_j] = '.'
                current_i -= 1
            else:
                field[current_i][current_j]= '^'
            tank = '^'

        elif i == 'D':
            if current_i + 1 < H and field[current_i + 1][current_j] == '.':
                field[current_i + 1][current_j] = 'v'
                field[current_i][current_j] = '.'
                current_i += 1
            else:
                field[current_i][current_j] = 'v'
            tank = 'v'

        elif i=='L':
            if current_j - 1 >= 0 and field[current_i][current_j - 1] == '.':
                field[current_i][current_j - 1] = '<'
                field[current_i][current_j] = '.'
                current_j -= 1
            else:
                field[current_i][current_j] = '<'
            tank = '<'

        elif i=='R':
            if current_j + 1 < W and field[current_i][current_j + 1] == '.':
                field[current_i][current_j + 1] = '>'
                field[current_i][current_j] = '.'
                current_j += 1
            else:
                field[current_i][current_j] = '>'
            tank = '>'
        else:
            if tank == '^':
                for a in range(current_i, -1, -1):
                    if field[a][current_j] == '#':
                        break
                    elif field[a][current_j] == '*':
                        field[a][current_j] = '.'
                        break

            elif tank == 'v':
                for a in range(current_i, H):
                    if field[a][current_j] == '#':
                        break
                    elif field[a][current_j] == '*':
                        field[a][current_j] = '.'
                        break

            elif tank == '>':
                for a in range(current_j, W):
                    if field[current_i][a] == '#':
                        break
                    elif field[current_i][a] == '*':
                        field[current_i][a] = '.'
                        break

            elif tank == '<':
                for a in range(current_j, -1, -1):
                    if field[current_i][a] == '#':
                        break
                    elif field[current_i][a] == '*':
                        field[current_i][a] = '.'
                        break

    print('#{} '.format(tc), end='')
    for i in field:
        print(''.join(i))


