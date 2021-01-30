N, K = map(int, input().split())
coins = sorted([int(input()) for _ in range(N)], reverse=True)
total = 0 

for coin in coins:
    if K >= coin:
        count =  K // coin
        total += count 
        K -= count * coin 
print(total)
