// 채점 결과
// 정확성: 53.8
// 효율성: 0.0
// 합계: 53.8 / 100.0
https://velog.io/@tnehd1998/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%ED%8C%8C%EA%B4%B4%EB%90%98%EC%A7%80-%EC%95%8A%EC%9D%80-%EA%B1%B4%EB%AC%BC-JavaScript


function solution(board, skill) {
    let answer = 0;
    let arr = Array.from({ length: board.length + 1 }, () =>
      Array(board[0].length + 1).fill(0)
    ); // 밑과 옆으로 board보다 1을 증가시킨 배열을 생성
  
    for (let i = 0; i < skill.length; i++) {
      let current = skill[i];
      let attack = current[0] === 1 ? -1 : 1;
      arr[current[1]][current[2]] += current[5] * attack; // (x1, y1)
      arr[current[3] + 1][current[2]] += current[5] * attack * -1; // (x2+1,y1)
      arr[current[1]][current[4] + 1] += current[5] * attack * -1; // (x1,y2+1)
      arr[current[3] + 1][current[4] + 1] += current[5] * attack; // (x2+1,y2+1)
    }
  
    for (let i = 0; i < board.length; i++) {
      for (let j = 0; j < board[0].length; j++) {
        arr[i + 1][j] += arr[i][j]; // 해당 값을 누적하여 위에서 아래로 더한다
      }
    }
  
    for (let i = 0; i < board.length; i++) {
      for (let j = 0; j < board[0].length; j++) {
        arr[i][j + 1] += arr[i][j]; // 해당 값을 누적하여 왼쪽에서 오른쪽으로 더한다
      }
    }
  
    for (let i = 0; i < board.length; i++) {
      for (let j = 0; j < board[0].length; j++) {
        board[i][j] += arr[i][j]; // board에 해당 배열인 arr을 더해 최종 배열
      }
    }
  
    for (let i = 0; i < board.length; i++) {
      for (let j = 0; j < board[0].length; j++) {
        if (board[i][j] > 0) {
          answer++; // 해당 값 중 0보다 큰 위치의 수
        }
      }
    }
  
    return answer;
  }


  
function solution(board, skill) {
    var answer = 0;
    for(let s of skill){
        if (s[0]===1){
            let a1= s[1],  b1 = s[2]
            let a2 = s[3], b2 = s[4]
            for(let i= b1; i<=b2; i++ ){
                for(let j = a1; j<=a2; j++){
                    board[j][i] -= s[5]
                } 
                }
            }
        if (s[0]===2){
            let a1= s[1],  b1 = s[2]
            let a2 = s[3], b2 = s[4]
            for(let i= b1; i<=b2; i++ ){
                for(let j = a1; j<=a2; j++){
                    board[j][i] += s[5]
                } 
                }
            }        
        }
    
    for(let b of board){
        for(let i = 0; i< b.length; i++){
            if (b[i] >= 1) answer += 1
        }
    }
    
    
    
    return answer;
}
//[0]이 1일경우 [5]만큼 뺴고([1],[2]) ([3],[4])만큼에 범위에서
//[0]이 2일경우 [5]만큼 더함
// 돌면서 해당 숫자가 1보다 크면 result += 1
//[[1,0,0,3,4,4],[1,2,0,2,3,2],[2,1,0,3,1,2],[1,0,1,3,3,1]]
//좌표를 어떻게 계산하지 