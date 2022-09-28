
https://velog.io/@dlzagu/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EA%B0%80%EC%9E%A5-%ED%81%B0-%EC%A0%95%EC%82%AC%EA%B0%81%ED%98%95-%EC%B0%BE%EA%B8%B0-%EB%AC%B8%EC%A0%9C-%EC%9E%90%EB%B0%94%EC%8A%A4%ED%81%AC%EB%A6%BD%ED%8A%B8-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-h9q2qtqx
function solution(board)
{
    let answer = 0;
    let row = board.length;
    let col = board[0].length;
    
    // 행 또는 열이 1이면 정사각형의 넓이를 1로 반환.
    if(row < 2 || col < 2) return 1;
    
    // 그 외의 경우엔 루프를 돌며 계산을 수행
    for(let i = 1; i < row; i++) {
        for(let j = 1; j < col; j++) {
            // 만약 자신의 위치(현재 인덱스)의 값이 1이상일 경우
            if(board[i][j] !== 0) {
            	// 왼쪽상단(↖︎), 위쪽(↑), 왼쪽(←)의 최솟값을 구한 후 
                let min = Math.min(
                    board[i-1][j-1], 
                    board[i-1][j], 
                    board[i][j-1]
                );
                // 자신의 위치에 최솟값 + 1을 할당한다.
                board[i][j] = min + 1;
            }
            // 할당한 값의 최댓값을 answer에 할당해주고
            if(answer < board[i][j]) answer = board[i][j];
        }
    }
    // 정사각형의 넓이를 구한다.
    return answer * answer;
}
  //bfs?
  // dx= [-1,1,0,0] dy = [0,0, -1, 1]
  // ij = 1이면, i,j+1 =1 이고 i+1 j=1 이고 i+1 j+1 =1 이면 그 합을 answer로 업뎃
  // ij =1 i,j+1 =1 i,j+2 =1 인가
  //어떻게 숫자를 늘려나갈지 모르곘음,,, 
  // 만약 변의 길이가 4라면, i j ~ i j+4 가 1인지 확인하고 
  // 
  
  
  //bfs?