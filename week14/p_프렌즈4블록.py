board= ["CCBDE", "AAADE", "AAABF", "CCBBF"]
n = 5
m = 4
def solution(m, n, board):
    board = [list(x) for x in board]
    print(board)
    matched =True
    while matched:
        matched = [] #한싸이클 돌 때 이전 쌍에 대해서는 처리가 됐으니까 다시 갱신
        print("2")
        for i in range(m-1):
            for j in range(n-1):
                if board[i][j] == \
                    board[i][j+1] ==\
                    board[i+1][j+1] ==\
                    board[i+1][j] != "#":
                    matched.append([i,j]) #4칸이 일치하면 그걸 matched안에 넣어서
                
        for i, j in matched:
            board[i][j] = board[i][j+1] = board[i+1][j+1]= board[i+1][j] = '#' ##으로 대체함으로써 사라졌다는 것을 의미
        for _ in range(m):
            for i in range(m-1):
                print(board)
                for j in range(n):
                    if board[i+1][j] == '#':
                        board[i+1][j], board[i][j] = board[i][j], '#' # 대체된 블록은 #로 위로 올려버리고(카운트 해야하니까) 위에있는건 내려버림
        print("1")
    return sum(x.count('#') for x in board)

print(solution(m,n,board))