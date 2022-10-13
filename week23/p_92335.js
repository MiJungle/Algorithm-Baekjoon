function solution(n, k) {
    var answer = 0 ;
    let new_n = n.toString(k)
    let m = new_n.split('0')
    for(let i = 0 ; i < m.length; i++){
        let count = 0
        for (let j =2 ; j <= Math.sqrt(Number(m[i])) ; j++){
            if(Number(m[i])%j ==0) count += 1
        }
        if(count ===0 && Number(m[i])>1 &&m[i]!="") answer += 1
    }
   
    return answer
}