n = int(input())
#n = 5
nums = list(map(int,input().split()))
#nums = [2,3,1,5]
checker = list(range(1,n+1))
for num in nums:
    if num in checker:
        checker.remove(num)
print(*checker)
