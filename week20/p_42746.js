function solution(numbers){
    let answer= ""
    numbers = numbers.map(number=> number +"")
    answer = numbers.sort((a,b)=> (b+a)-(a+b)).join('')
    
    return answer[0]==='0'?'0': answer
}
