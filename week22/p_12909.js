//처음에 pop 했는데 어차피 경우의 수 1개니까 숫자로 바꿈.


// 채점 결과
// 정확성: 69.5
// 효율성: 0.0
// 합계: 69.5 / 100.0

function solution(s){
    var answer = true;
    let open = 0
    for(bracket of s){
        if(bracket == "\(") {
            open++
        } else {
            if(open!=0) {open--}
            else {return false}
        }
    }
    if(open!=0) return false
    else return true;
}

//pop 해서 )의 경우, close = [)]넣는다
// (의 경우, 닫혔음을 의미하기 때문에 close pop
//