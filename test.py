def solution(number,n,m):
    answer = 0
    for i in range(n,20,n):
        print(i)
        if number == i:
            print("found")
            break


    for i in range(m,20,m):
        print(i)
        if number == i:
            print("found")
            result += 0.5
            break
    return answer

result = solution(30,2,3)
print(result)