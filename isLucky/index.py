def solution(n):
    # change to a string and split into two
    n = [char for char in str(n)]
    lenth = len(n)
    left = [int(x) for x in n[:lenth // 2]]
    right = [int(x) for x in n[lenth // 2 :]]
    
    x =True if sum(left) == sum(right) else False
    return x

result = solution(134008)

print(result)
    
