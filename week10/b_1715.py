import sys
import heapq as hq
sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())
cards = [int(input().rstrip()) for _ in range(N)]
cards.sort()
ans = 0
while len(cards) != 1:
    a = hq.heappop(cards)
    b = hq.heappop(cards)
    ans += a+b
    hq.heappush(cards, a+b)

print(ans)