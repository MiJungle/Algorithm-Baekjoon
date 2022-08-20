function solution(n) {
    
    let k = n-1
    for (let i = 2 ; i <= n; i++){
        for (let j = 2; j <= Math.sqrt(i); j++){
            if (i % j === 0 && i/j != 1){
                k -= 1;
                break;
            }
        }
  
    }
    
        return k
}


n = 10
console.log(solution(n))