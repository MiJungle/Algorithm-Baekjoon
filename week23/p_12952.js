function solution(n) {
    let answer = 0;
    
    const dfs = (board, row) => {
      if(row === n) answer++;
      else {
        for(let i = 1; i <= n; i++) {
          board[row+1] = i;
          if(isValid(board, row+1)) dfs(board, row+1);
        }
      }
    }
    
    const isValid = (board, row) => {
      for(let i = 1; i < row; i++) {
        if(board[i] === board[row]) return false;
        if(Math.abs(board[i] - board[row]) === Math.abs(i - row)) return false;
      }
      return true;
    }
    
    for(let i = 1; i <= n; i++) {
      const board = new Array(n+1).fill(0);
      board[1] = i;
      dfs(board, 1);
    }
    
    return answer;
  }
    


// import sys

// input = sys.stdin.readline

// def dfs(x):
//     global result
//     if x == n:
//         result += 1
//     else:
//         for i in range(n):
//             row[x] = i
//             if check(x):
//                 dfs( x + 1 )

// def check(x):
//     for i in range(x):
//         if row[x] == row[i]:
//             return False
//         if abs(row[x]-row[i]) == x-i:
//             return False
//     return True

// n = int(input())
// row = [0] * n
// result = 0
// dfs(0)

// print(result)