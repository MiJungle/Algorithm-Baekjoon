#소스: https://bladejun.tistory.com/97
#two pointer로 가면 O(n)



import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline

N = int(input())
M = list(map(int, input().split()))
M.sort()

def closetozero():
    first = 0
    end = N-1
    answer = 2e+9+1 #2,000,000,001
    final = [] ##
    while first < end:
        M_first = M[first]
        M_end = M[end]

        total = M_first + M_end

        if abs(total) < answer:
            answer = abs(total)
            final = [M_first, M_end]

        if total < 0:
            first += 1
        else:
            end -= 1
    return final[0], final[1]
print(*closetozero(), sep=" ")