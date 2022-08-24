function solution(n) {
    const answer = []
    for(i=String(n).length-1; i>=0; i--){
        answer.push(Number(String(n)[i]))
    }
    return answer
}
console.log(solution("12345"))