# 어떤 양의 정수 X의 각 자리가 등차 수열을 이룬다면, 그 수를 한수라고 한다.
# 등차수열 = 연속된 두 개의 수의 차이가 일정한 수열
# 1보다 크거나 같고, N보다 작거나 같은 한수의 개수를 출력하는 프로그램을 작성하시오.
# 한수의 개수 출력하기
N = int(input())
count = 0
for i in range(1, N+1):
    number = str(i)
    flag = True
    for j in range(len(number)-1):
        if j != 0:
            if difference == int(number[j])-int(number[j+1]):
                flag = True 
            else:
                flag = False 
                break
        difference = int(number[j])-int(number[j+1])
    if flag:
        count += 1
print(count)