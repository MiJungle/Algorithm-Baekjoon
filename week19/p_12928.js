function solution(n) {
    var answer = 0;
    let divisor = [] 
    if(n===0){
        return 0
    }
    for(let i =1 ; i<=n;i++){
        if(n%i===0){
            divisor.push(i)
        }
    }
    
    const reducer = (accumulator, curr) => accumulator + curr;
    answer = divisor.reduce(reducer)

    return answer;
}