function solution(brown, yellow) {
    var answer = [];
    let whole = brown + yellow
    for (let i=1; i <=parseInt(Math.sqrt(whole))+1; i++){
        if((whole%i) === 0) {answer.push([ whole/i,i])}
    }
    let reversed = answer.reverse()
    for (nums of reversed){
        let [a,b] = nums
        if ((a-2)*(b-2)===yellow) return  [Math.max(a,b),Math.min(a,b)]
    }
}