import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

sys.setrecursionlimit(10**6)
num_list = []
while True:
    try:
        num = int(input())
        num_list.append(num)
    except:
        break

def postorder(first,end):
    if first > end:
        return
    mid = end+1   # 루트보다 큰 값이 존재하지 않을 경우를 대비   
    for i in range(first+1,end+1):
        if num_list[first] < num_list[i]: #num_list 의 first 값이 i 번째 값보다 작다면
            mid = i #mid 는 i로 재설정 
            break
    
    postorder(first+1, mid-1)
    postorder(mid, end)
    print(num_list[first])

postorder(0,len(num_list)-1)

# 루트/왼/오 로 되어 있는 것을 > 왼/오/루트 로 출력.
# 배열의 인덱스를 돌며 후위 순회 진행
# root = preorder [ start ]
# -> 루트노드로 설정
# 배열을 돌며 오른자식 노드의 위치(idx)를 찾는다.
# start = start + 1, end = idx // start = idx, end = end
# 새롭게 두 part 로 나눠서 재귀함수 호출.
# print(root) >> 후위 순회이므로 보내고 나서 루트노드 출력.
# if start>= end : return 배열을 모두 돌면 return