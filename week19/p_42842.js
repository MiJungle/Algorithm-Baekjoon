function solution(brown, yellow) {
    var answer = [];
    let whole = brown + yellow
    for(i= 1; i<=Math.sqrt(brown+yellow); i++){
        if (whole % i ===0){
            let div = whole /i
            answer.push([Math.max(div,i),Math.min(div,i) ] )
        }
    }
    for (num of answer){
        if (((num[0]-2)*(num[1]-2)) === yellow){
            return num
        }
    }
}
