function solution(board, moves) {
    var answer = 0;
    let arr = []
    for (move of moves){
        for(let i = 0 ; i < board.length-1; i++){
            if(board[i][move+1] != 0) {
                arr.push(board[i][move+1])
                board[i][move+1] = 0
                break
        }     
    }
    }
    console.log(arr)
        let newArr = [...arr]
        for(let i = arr.length-1; i== 0 ; i--){
            if(arr[i]==arr[i-1]){
                newArr.slice(0,arr[i-1]) 
                answer += 1
            }
        }
    // return answer;
}
// move 별로 [i-1,0][i-1,1][i-1,2]이런식으로 탐색해나감, 0이아닐때까지
// 숫자를 result에 넣음, result 전 숫자랑 비교햇을 때 같으면 count += 1
// 사라진 후에 남은 숫자들도 비교, 
