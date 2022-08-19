function solution(left, right) {
    var answer = 0;
    
    for(let i = left; i<=right; i++){
        if(Number.isInteger(Math.sqrt(i)) === false){
            answer += i
        }
        else {
            answer -= i
        }
    }
    return answer;
}