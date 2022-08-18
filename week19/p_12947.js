function solution(x) {
    var answer = true;
    x = String(x)
    let num = 0
    for(let i=0; i <x.length; i++){
        num += Number(x[i])
    }
    if(Number(x)% num !==0){
        answer = false
    }
    
    return answer;
}