function solution(d, budget) {
    var answer = 0;
    let count = 0
     d.sort(function(a,b){
        return a-b;
    })
    for(let i = 0; i<d.length ; i ++){
        if (answer + d[i] <= budget){
            answer += d[i]
            count += 1
        }
}    
    return count;

}