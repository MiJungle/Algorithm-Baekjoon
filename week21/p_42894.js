
//사라질 수 있는 모형은 총 5가지가 존재한다. 
// 해당 모형들을 다 0 으로 바꾸는 작업을 반복한다. 맨위에서부터 차례로 

function solution(board) {
    let answer = 0;
    let searchedInfo = searchErasable(board);
    while(searchedInfo) {
      answer++;
      eraseBoard(board,searchedInfo);
      searchedInfo = searchErasable(board);
    }
    return answer;
  }
  //i 가 x축 j가 y축이라고 생각하면 됨. 
  function searchErasable(board) {
    for(let i = 0 ; i < board[0].length; i++) {
      for(let j = 0; j < board.length; j++) {
        if(board[j][i] > 0) {
          let blockNum = board[j][i];
          if( j >= 2 && i <= board[0].length - 1) { //check _l range
            if( board[j][i+1] === blockNum && board[j-1][i+1] === blockNum && board[j-2][i+1] === blockNum) { //check _l shape
              return { shape : '_l', x : j, y : i };
            }
          }
          if( j >= 2 && i >= 1) { //check l_ range
            if( board[j][i-1] === blockNum && board[j-1][i-1] === blockNum && board[j-2][i-1] === blockNum) { //check l_ shape
              return { shape : 'l_', x : j, y : i };
            }
          }
          if( j >= 1 && i <= board[0].length - 2 ) { //check ___l range
            if( board[j][i+1] === blockNum && board[j][i+2] === blockNum && board[j-1][i+2] === blockNum) { //check ___l shape
              for(let k = j - 1; k >= 0; k--) {
                if( board[k][i+1] > 0) break;
                if( k === 0) return { shape : '___l', x : j, y : i };
              }
            }
          }
          if( j >= 1 && i >= 1 && i <= board[0].length - 1 ) { //check l___ range
            if( board[j][i-1] === blockNum && board[j-1][i-1] === blockNum && board[j][i+1] === blockNum) { //check l___ shape
              for(let k = j - 1; k >= 0; k--) {
                if( board[k][i+1] > 0) break;
                if( k === 0)  return { shape : 'l___', x : j, y : i };
              }
            }
          }
          if( j >= 1 && i <= board[0].length - 2 ) { //check _l_ range
            if( board[j][i+1] === blockNum && board[j-1][i+1] === blockNum && board[j][i+2] === blockNum) { //check _l_ shape
              for(let k = j - 1; k >= 0; k--) {
                if( board[k][i+2] > 0) break;
                if( k === 0) return { shape : '_l_', x : j, y : i };
              }
            }
          }
          break;
        }
      }
    }
    return false;
  }
  
  function eraseBoard(board, info) {
    board[info.x][info.y] = 0;
    if(info.shape === '_l') {
      board[info.x][info.y + 1] = 0;
      board[info.x-1][info.y + 1] = 0;
      board[info.x-2][info.y + 1] = 0;
    } else if(info.shape === 'l_') {
      board[info.x][info.y - 1] = 0;
      board[info.x-1][info.y - 1] = 0;
      board[info.x-2][info.y - 1] = 0;
    } else if(info.shape === '___l') {
      board[info.x][info.y + 1] = 0;
      board[info.x][info.y + 2] = 0;
      board[info.x-1][info.y + 2] = 0;
    } else if(info.shape === 'l___') {
      board[info.x][info.y - 1] = 0;
      board[info.x-1][info.y - 1] = 0;
      board[info.x][info.y + 1] = 0;
    } else if(info.shape === '_l_') {
      board[info.x][info.y + 1] = 0;
      board[info.x-1][info.y + 1] = 0;
      board[info.x][info.y + 2] = 0;
    }
  }
  
// 검은 돌이 채워질 수 있는 조건?
// 직사각형이 되면 된다. 채워진
// 검은돌이 떨어질 수 있는 공간은 아래에 숫자가 있는 공간
// 반복문을 돌면서 0이아닌 숫자가 잇는 index를 찾는다.
// 그 인덱스를 기준으로 오른쪽 왼쪽은 0이면서 아래는 동일한 숫자인 것지 확인  
// 빈곳에 4를 넣었을때 그걸 기준으로 직사각형이 4로 채워지는지 확인 
// 채워지면 count 1. 해당 숫자는 0 으로 다 변경해준다. 
// 반복문을 계속 돈다 -> 언제까지? board.length까지 다 돌았을 때 
//[[0,0,0,0,0,0,0,0,0,0],
//[0,0,0,0,0,0,0,0,0,0],
//[0,0,0,0,0,0,0,0,0,0],
//[0,0,0,0,0,0,0,0,0,0],
//[0,0,0,0,0,0,4,0,0,0],
//[0,0,0,0,0,4,4,0,0,0],
//[0,0,0,0,3,0,4,0,0,0],
//[0,0,0,2,3,0,0,0,5,5],
//[1,2,2,2,3,3,0,0,0,5],
//[1,1,1,0,0,0,0,0,0,5]]
